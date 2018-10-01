# coding: utf-8

import sys
import unittest


def simulate_moves(button_seq):
    o_buttons = []
    b_buttons = []
    o_pos = b_pos = 1

    for button in button_seq:
        if button[0] == 'B':
            b_buttons.append(button)
        else:
            o_buttons.append(button)

    turns = 0
    for button in button_seq:
        next_button = False
        while not next_button:
            turns += 1
            #print 'turn', turns
            if b_buttons:
                if button == b_buttons[0] and b_buttons[0][1] == b_pos:
                    b_buttons.pop(0)
                    next_button = True
                    #print 'b push button', button
                elif b_buttons[0][1] > b_pos:
                    b_pos += 1
                    #print 'b move to', b_pos
                elif b_buttons[0][1] < b_pos:
                    b_pos -= 1
                    #print 'b move to', b_pos
            if o_buttons:
                if button == o_buttons[0] and o_buttons[0][1] == o_pos:
                    o_buttons.pop(0)
                    next_button = True
                    #print 'o push button', button
                elif o_buttons[0][1] > o_pos:
                    o_pos += 1
                    #print 'o move to', o_pos
                elif o_buttons[0][1] < o_pos:
                    o_pos -= 1
                    #print 'o move to', o_pos
            #print '-' * 30

    return turns


class BotTrustTest(unittest.TestCase):

    def test_simulate_moves(self):
        moves = [('O', 2,),
                 ('B', 1,),
                 ('B', 2,),
                 ('O', 4,)]

        self.assertEqual(simulate_moves(moves), 6)

        moves = [('B', 2,),
                 ('B', 1,)]

        self.assertEqual(simulate_moves(moves), 4)

        moves = [('O', 5,),
                 ('O', 8,),
                 ('B', 100,)]

        self.assertEqual(simulate_moves(moves), 100)


def main():
    indata = open(sys.argv[1])
    outdata = open(sys.argv[2], 'w')
    t = int(indata.readline().strip())

    for i in range(t):
        button_seq = []
        line_args = indata.readline().strip().split(' ')
        n = int(line_args.pop(0))
        for j in range(n):
            x = j * 2
            button_seq.append((line_args[x], int(line_args[x + 1]),))
        res = simulate_moves(button_seq)
        outdata.write("Case #%d: %d\n" % (i + 1, res,))

    indata.close()
    outdata.close()


if __name__ == '__main__':
    main()
