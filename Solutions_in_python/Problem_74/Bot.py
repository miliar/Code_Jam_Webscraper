import logging
log = logging.getLogger()
#log.setLevel(logging.DEBUG)

class Bot:
    """Bot from Portal"""

    def __init__(self, color, actions):
        self.color = color
        self.position = 1
        self.actions = actions

    def get_goal(self):
        if not self.actions.actions:
            return None
        for target in self.actions.actions:
            if target[0] == self.color:
                return target[1]
        # if there isn't anything to do anymore
        return None

    def take_action(self):
        goal = self.get_goal()

        if goal == None:
            # stay at the same position
            pass
        
        # if it is the turn of the robot and he is ready to push
        elif self.actions.actions[0][0] == self.color and self.actions.actions[0][1] == self.position :
           # press the button
           self.actions.push_top_button()
           logging.debug(self.color + 'pushed at '+ str(self.position))
        elif goal == self.position:
            # stay at the same position
            logging.debug(self.color + 'stayed at '+ str(self.position))
        else:
            self.go_towards_objective(goal)
            logging.debug(self.color + 'runned at '+ str(self.position))

    def go_towards_objective(self, goal):
        if goal < self.position:
            # move down
            self.position = self.position - 1
        else:
            # move up
            self.position = self.position + 1

class Actions:
    """List of all buttons to push, and by who"""

    def __init__(self, actions):
        self.actions = actions
        self.toPush = False

    def update(self):
        if self.toPush:
            self.push()
            self.toPush = False

    def push_top_button(self):
        self.toPush = True

    def push(self):
        logging.debug(self.actions)
        logging.debug(len(self.actions))
        if len(self.actions) == 1:
            self.actions = None
        else:
            self.actions = self.actions[1:]
        logging.debug(self.actions)

def go_push_the_buttons(n, actions):
    time = 0
    buttons_to_push = Actions(actions)
    blue = Bot('B', buttons_to_push)
    orange = Bot('O', buttons_to_push)

    while buttons_to_push.actions:
        time = time + 1
        logging.debug('time = ' + str(time))
        blue.take_action()
        orange.take_action()
        buttons_to_push.update()
        logging.debug('\n')

    print("Case #" + str(n) + ": " + str(time))
    logging.debug('\n\n')
