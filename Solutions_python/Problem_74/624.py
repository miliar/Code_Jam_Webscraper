
class RobotGame(object):
    def __init__(self, tasks):
        '''
        @var task "count name nr name nr"
        '''
        self.tasks = self.parseLine(tasks)
        self.nextButton = 0
        self.steps = 0
        self.robots = {"O":1, "B":1}

    def parseLine(self, str):
        return zip(str.split()[1::2], [int(x) for x in str.split()[2::2]])

    def nextPos(self, robot):
        i = self.nextButton
        while i<len(self.tasks) and self.tasks[i][0]!=robot:
            i+=1
        if i>=len(self.tasks):
            return self.robotPos(robot)
        return self.tasks[i][1]
    
    def robotPos(self, robot):
        return self.robots[robot]

    def step(self, robot):
        buttonPress = False
        if self.nextPos(robot) == self.robotPos(robot):
            if self.tasks[self.nextButton][0] == robot:
                robotMove = "%s push button %d" % (robot, self.robotPos(robot))
                buttonPress = True
            else:
                robotMove = "%s stay at button %d" % (robot, self.robotPos(robot))
        else:
            self.robots[robot]+=(self.nextPos(robot)>self.robotPos(robot))*2-1
            robotMove = "%s move to button %d" % (robot, self.robots[robot])
        return (robotMove, buttonPress)

    def loop(self):
        while self.nextButton<len(self.tasks):
            #print "TODO: %s" % self.tasks
            #print "Step:%d, task: %d, Robos: %s" % (self.steps, self.nextButton, self.robots) 
            self.steps += 1
            actionO = self.step("O")
            actionB = self.step("B")
            #print "%2d | %20s | %20s" % (self.steps, actionO[0], actionB[0])
            if actionO[1] or actionB[1]:
                self.nextButton += 1
        return self.steps
if __name__ == "__main__":
    import sys
    cases = int(sys.stdin.readline())
    
    for case in range(cases):
        game = RobotGame(sys.stdin.readline())
        print "Case #%d: %d" % (case+1, game.loop())
            
