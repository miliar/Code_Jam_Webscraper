import sys
#import iterator

def main():
    case = 1
    for test, turn_list in parse_file():
        calculate(test, turn_list, case)
        case += 1
        #sys.exit()
        
    
def calculate(details, turn_list, case):
    #print details
    o = Robot('O', details['O'])
    b = Robot('B', details['B'])
    time = 1
    turn = 0

    o_done = False
    b_done = True
    pushed = False
    while (True):
        #print "Time period: %s" % time
        
        for r in [o,b]:
            if r.done:
                continue

            if r.pos < r.targets[r.i]:
                r.pos += 1
                #print "Moving %s to %s" % (r.name, r.pos)
            elif r.pos == r.targets[r.i] and turn_list[turn] == r.name:
                #print "Pushing button. %s" % r.name
                r.i += 1
                pushed = True
                if r.i == len(r.targets):
                    r.done = True
            elif r.pos > r.targets[r.i]:
                r.pos -= 1
                #print "Moving %s to %s" % (r.name, r.pos)
                
        if pushed:
            turn += 1
            pushed = False
                
                    
        # Check blue
        if o.done and b.done:
            break
            
        time += 1
    print "Case #%s: %s" % (case, time)


class Robot():
    def __init__(self, name, targets):
        self.name = name
        self.targets = targets
        self.pos = 1
        self.i = 0
        self.done = False
        
        if not self.targets:
            self.done = True
        

        
def parse_file():
    it = iter(sys.stdin.readlines())
    it.next()
    for line in it:
        details = {'O':[],
                    'B':[]}
        
        lit = iter(line.split())
        
        lit.next() # burn the number of items
        turn_list = []
        while(True):
            try:
                robot = lit.next()
                position = lit.next()

                details[robot].append(int(position))

                turn_list.append(robot)
            except StopIteration:
                break
        
        #print details
        yield (details, turn_list)

        
            
            
        
        
if __name__ == '__main__':
    main()