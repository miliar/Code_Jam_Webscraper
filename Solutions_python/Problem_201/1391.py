import operator
import math

def create_next_level(current_level):
    next_level=[]
    for i in range( len(current_level) ):
        next_level.insert(2*i, (current_level[i]-1)/2 )
        next_level.insert(2*i+1, (current_level[i])/2 )
    return next_level

def create_level( current_level, level):
    i=1
    next_level=current_level
    while i <= level:
        next_level=create_next_level(next_level)
        i +=1
    return next_level


rfile = open("C-small-2-attempt1.in.txt","r")
wfile =  open("C-small-2-out.txt", "w+")
T = int (rfile.readline()[:-1])
lineSplit=[]

for t in range(T):
    if t != (T-1):
        lineSplit = rfile.readline()[:-1].split(' ')
    else:
        lineSplit = rfile.readline().split(' ')

    #print lineSplit
    current_level = [long(lineSplit[0])]
    K = long(lineSplit[1])

    if current_level[0]==K:
        last_filled_stall = 1;
    else:
        level = math.frexp(K)[1]-1
        K_remaining = K - 2**(level) +1
        current_level = create_level(current_level, level)

        if  K_remaining == 2**level:
            last_filled_stall = min(current_level)
        else:
            current_level.sort()
            last_filled_stall = current_level[-K_remaining]

    #print last_filled_stall/2, (last_filled_stall-1)/2
    wfile.write("Case #%d: %d %d\n"%((t+1),last_filled_stall/2, (last_filled_stall-1)/2))

rfile.close()
wfile.close()