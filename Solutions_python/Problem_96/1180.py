#Dancing.py
#Justin Roberts (tangofox10@gmail.com)
#Google Code Jam Qualification Round
#Problem: Dancing With the Googlers
#Written in Python

#Feeling pretty good about this.
#I relearned some Python basics in that last one.
#Haven't read the description for this yet, but I'm feeling like I want
#to go for the full 100 points.
#I'm also going to try to do the problems in order without looking ahead.
#Let's see how this goes.

#Ooh... don't quite understand the problem yet, but it looks like some
#combinatorics. Neato.

#Wait... I've got the output from the last problem sitting in my interpreter
#window and am just now reading it.

#you pissed off the chicken lady
#dafuq Google!?
#Nice Fibonacci sequence there for cases 14 and 15
#I want to post all of this shit on Facebook right now!!!
#But I'll wait. =(

#Oh, I'm supposed to be working on problem 2.

def read_int():
#read() until space, then return as int
#very sloppy work... not reusable in the least
    the_int = ''
    the_int += fin.read(1)
    buffer = fin.read(1)
    if buffer != ' ':
        the_int += buffer
        buffer = fin.read(1)
        if buffer != ' ':
            the_int += buffer
            buffer = fin.read(1)
    return int(the_int)


fin = open('B-large.in', 'r')
fout = open('DancingOut.txt', 'w')
#When I read the name of my input stream, I think of a fish
#You know... since fish have fins.
#What the hell is a fout though?

T = int(fin.readline())

for case in range(1,T+1):
    N = read_int()
    S = read_int()
    p = read_int()
    t = []
    result = 0
    s = 0
    for i in range(N-1):
        t.append(read_int())
    t.append(int(fin.readline()))
    #too lazy to augment the function read_int() to handle EOL instead of space
    if p == 0:
        result = N
    elif p == 1:
        for score in t:
            if score >= 1:
                result += 1
    else:
        for score in t:
            if score >= 3*p-2:
                result +=1
            elif s < S and score >= 3*p-4:
                s += 1
                result += 1
    fout.write('Case #%d: %d\n'%(case,result))
    print('Case #%d: %d'%(case,result))

#Wow, I've messed around way too much. It's getting late. After I get the large
#submission done, I'll go to bed. The rest can wait until tomorrow.

#And no, I won't even read the other problems until then.
#If I read them, then I'll just lie away thinking about them.
#Screw that. Sleep time is for sleep, not discrete math.