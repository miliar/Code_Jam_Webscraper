import os
import itertools

t = 1
matches = []
with open('A-small-attempt0.in', 'rb') as text_file:
    first_line = text_file.readline().strip('\r\n')
    rnum = 1
    x_use = []
    y_use = []
    for line in text_file:
        if rnum == 1:
            x = int(line.strip('\r\n'))
        if rnum == 6:
            y = int(line.strip('\r\n'))
        if rnum == 2:
            x1 = line.strip('\r\n').split(' ')
        if rnum == 3:
            x2 = line.strip('\r\n').split(' ')
        if rnum == 4:
            x3 = line.strip('\r\n').split(' ')
        if rnum == 5:
            x4 = line.strip('\r\n').split(' ')
        if rnum == 7:
            y1 = line.strip('\r\n').split(' ')
        if rnum == 8:
            y2 = line.strip('\r\n').split(' ')
        if rnum == 9:
            y3 = line.strip('\r\n').split(' ')
        if rnum == 10:
            y4 = line.strip('\r\n').split(' ')
        rnum += 1
        if rnum == 11:
            if x == 1:
                for thing in x1:
                    x_use.append(thing)
            if x == 2:
                for thing in x2:
                    x_use.append(thing)
            if x == 3:
                for thing in x3:
                    x_use.append(thing)
            if x == 4:
                for thing in x4:
                    x_use.append(thing)
            if y == 1:
                for thing in y1:
                    y_use.append(thing)
            if y == 2:
                for thing in y2:
                    y_use.append(thing)
            if y == 3:
                for thing in y3:
                    y_use.append(thing)
            if y == 4:
                for thing in y4:
                    y_use.append(thing)
            for element in x_use:
                if element in y_use:
                    matches.append(element)
            if len(matches) == 0:
                print 'Case #' + str(t) + ': ' + 'Volunteer cheated!'
            if len(matches) == 1:
                print 'Case #' + str(t) + ': ' + str(matches[0])
            if len(matches) > 1:
                print 'Case #' + str(t) + ': ' + 'Bad magician!'
            rnum = 1
            matches = []
            x_use = []
            y_use = []
            t += 1
