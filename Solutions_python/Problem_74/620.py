from tools import *
import sys

lines = read_file(sys.argv[1])
del lines[0]
for i in xrange(0, len(lines)):
    lines[i] = lines[i].split()
    del lines[i][0]
    tmp = []
    for j in xrange(0, len(lines[i]), 2):
        tmp.append((lines[i][j], lines[i][j + 1]))
    lines[i] = tmp

WAIT = 0
MOVE = 1
PUSH = 2
orange_action, blue_action = 0, 0

orange_pos, blue_pos = 1, 1
orange_dir, blue_dir = 1, 1
buttons_pushed = []
steps = 0

def move(m):
    """move"""
    global orange_pos, blue_pos, orange_dir, blue_dir, steps
    if orange_dir != 0:
        if orange_pos < orange_dir:
            orange_pos += 1
        elif orange_pos > orange_dir:
            orange_pos -= 1
        elif m[1] == orange_pos:
            steps += 1
            buttons_pushed.append(m)
    if blue_dir != 0:
        if blue_pos < blue_dir:
            blue_pos += 1
        elif blue_pos > blue_dir:
            blue_pos -= 1
        elif m[1] == blue_pos:
            steps += 1
            buttons_pushed.append(m)

for l in lines:
    for i in xrange(0, len(l)):
        l[i] = (l[i][0], int(l[i][1]))

result = []

for l in lines:
    print l
    steps = 0
    orange_pos, blue_pos = 1, 1
    orange_dir, blue_dir = 1, 1

    for i in xrange(0, len(l)):

        if l[i][0] == 'O':
            orange_dir = l[i][1]

            for j in xrange(i + 1, len(l)):
                if l[j][0] == 'B':
                    blue_dir = l[j][1]
                    break

        elif l[i][0] == 'B':
            blue_dir = l[i][1]

            for j in xrange(i + 1, len(l)):
                if l[j][0] == 'O':
                    orange_dir = l[j][1]
                    break

        while 1:
            steps += 1
            pushed = False

            if orange_pos < orange_dir:
                orange_pos += 1
            elif orange_pos > orange_dir:
                orange_pos -= 1
            elif l[i][1] == orange_pos and l[i][0] == 'O':
                pushed = True
                buttons_pushed.append(l[i])

            if blue_pos < blue_dir:
                blue_pos += 1
            elif blue_pos > blue_dir:
                blue_pos -= 1
            elif l[i][1] == blue_pos and l[i][0] == 'B':
                pushed = True
                buttons_pushed.append(l[i])

            if pushed:
                #print "B: %d O: %d Steps: %d" % (blue_pos, orange_pos, steps)
                break

    buttons_pushed = []
    #print steps
    result.append(str(steps))

write_file(insert_case(result), "out")
