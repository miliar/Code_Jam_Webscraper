import sys, io, os

filename = 'A-large.in'

def solver(filename):
    with io.open(filename, 'r') as file:
        N = int(file.readline())
        for case in range(N):
            line = file.readline()
            buttonOrderString = line.split(' ')
            pushes = int(buttonOrderString[0])
            i = iter(buttonOrderString[1:])
            buttonOrdersParsed = [(a, int(b)) for (a, b) in zip(i, i)]
            
            time = 0
            
            lastMove = {'O': 0, 'B': 0} #in time
            position = {'O': 1, 'B': 1} #in space
            for (c, p) in buttonOrdersParsed:
                time = time + 1 if lastMove[c] + abs(position[c] - p) <= time else lastMove[c] + abs(position[c] - p) + 1
                lastMove[c] = time
                position[c] = p
            
            print("Case #%s: %d"%(case+1, time))

solver(filename)