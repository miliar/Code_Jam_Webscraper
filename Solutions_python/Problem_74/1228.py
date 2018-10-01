#!/usr/bin/env python

from optparse import OptionParser


def get_buttons(raw_str):
    """
    >>> raw_str = '2 B 2 B 1'
    >>> get_buttons(raw_str)
    [{'col': 'b', 'pos': 2}, {'col': 'b', 'pos': 1}]
    """
    items = raw_str.split()
    del items[0]
    assert len(items) % 2 == 0
    return [{'col': col.lower(), 'pos': int(pos)} for
            col, pos in zip(items[::2], items[1::2])]

class Robot():
    pos = 1
    def move(self, target):
        if self.pos < target:
            self.pos += 1
        elif self.pos > target:
            self.pos -= 1

def get_goal(buttons, colour):
    for button in buttons:
        if colour == button['col']:
            return button['pos']

class Hallway():

    timer = 0

    def __init__(self, buttons, debug=False, limit=500):
        self.buttons = buttons
        self.debug = debug
        self.limit = limit
        self.robots = {}
        for col in set([btn['col'] for btn in buttons]):
            self.robots.update({col: Robot()})

    def step(self):

        self.timer += 1

        actioned = []
        def try_to_press():
            first_col = self.buttons[0]['col']
            first_pos = self.buttons[0]['pos']
            if (first_col not in actioned and
                self.robots[first_col].pos == first_pos):
                if self.debug:
                    print 'Push {0} on {1} second'.format(self.buttons[0],
                                                              self.timer)
                del self.buttons[0]
                actioned.append(first_col)
                if self.buttons:
                    return True

        try_to_press()

        if not self.buttons:
            return

        for col in set(self.robots) - set(actioned):
            if self.debug:
                ptrn = ('Mov {col} from {rob.pos} toward {goal} on {time} '
                       'second')
                print ptrn.format(col=col, rob=self.robots[col],
                                  goal=get_goal(self.buttons, col),
                                  time=self.timer)
            self.robots[col].move(get_goal(self.buttons, col))

    def run(self):

        while True:
            if not self.buttons:
                break
            if self.timer > self.limit:
                print '{0} steps done, limit reached'.format(self.limit)
                break
            else:
                self.step()

        return self.timer

def test(raw_str, debug=False, limit=50000):
    buttons = get_buttons(raw_str)
    hallway = Hallway(buttons, debug, limit)
    return hallway.run()

def process_attempt(f_p, debug=False):
    with open('output.txt', 'w') as output:
        f_p.readline()
        case = 1
        for line in f_p.readlines():
            output.write('Case #{0}: {1}\n'.format(case, test(line, debug)))
            case += 1

def main():
    parser = OptionParser()
    parser.add_option('-d', '--debug')
    opts, args = parser.parse_args()
    debug = True if opts.debug else False
    with open(args[0]) as attempt:
        process_attempt(attempt, debug)

if __name__ == '__main__':
    main()
