
import sys

def isON(snappers, snaps):
    return snaps != 0 and (snaps + 1) % pow(2,snappers) == 0

if len(sys.argv) > 1:
    input = open(sys.argv[1])
else:
    input = open(raw_input("input file: "))
    
input.readline()
lines = input.readlines()
for index in range(len(lines)):
    args = map(int, lines[index].split(" "))
    state = "OFF"
    if (isON(args[0], args[1])):
        state = "ON"
    
    print "Case #%i: %s" % (index + 1, state)