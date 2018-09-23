# your code goes here
import sys


def flip_s_at(s, pos, k):
    st = s
    k = int(k)
    for i in range(pos,pos+k):
        print i
    return st.replace('-', '+', pos + k)


def flip_pancakes(s, k):
    loops = len(s) - int(k)
    scop = list(s)
    sout = ''
    flip_cnt = 0
    kint = int(k)
    pos = 0
    lpos = 0
    for p in range(loops):
        if scop[p] == '-':
            flip_cnt += 1
            for fi in range(kint):
                if scop[p+fi] == '-':
                    scop[p+fi] = '+'
                elif scop[p+fi] == '+':
                    scop[p+fi] = '-'

    for i in range(len(scop)):
        sout += scop[i]

    if '-' in scop:
        print "Case #" + str(count) + ": IMPOSSIBLE"
        # print "Case #" + str(count) + " s:" + s + k + " : <IMPOSSIBLE>: " + sout # Debugging
        # print "Case #" + str(count) + ": " + str(flip_cnt) # Debugging
    else:
        # print "Case #" + str(count) + " s:" + s + k ": " + sout # Debugging
        print "Case #" + str(count) + ": " + str(flip_cnt)

count = 0
for line in sys.stdin:
    if count == 0:
        num_tests = int(line)
        # print "num_tests: " + str(num_tests)
        count += 1
    else:
        p = line
        # print "pancakes: " + p
        s, k = p.split(' ')
        s = p[0:-2]
        flip_pancakes(s, k)
        count += 1




#
        # pos = s.find('-')
        # if pos > lpos:
        #     lpos = pos
        # scop = flip_s_at(scop, pos, kint)
        # print scop
        # flip_pancakes(scop, k)
        # print scop