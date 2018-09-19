def sol():
    def rec(P, timer):
##        print P, timer
        if len(P)==0 or timer>=9:
            return 9
        solutions = []
        for i in range(1,(max(P)/2)+1):
            _P = P[:]
            _P.remove(max(P))
            _P.append(i)
            _P.append((max(P)-i))
            solutions.append(rec(_P, timer+1))
##            print _P, timer, solutions[-1]
        if (max(P)>0):
            _P = P[:]
            for i in range(len(_P)):
                _P[i]-=1
            solutions.append(rec(_P, timer+1))
        else:
            return timer
        return min(solutions)
    #read input
    global line_counter
    D = inp[line_counter].split(' ')
    line_counter+=1
    Pstr = inp[line_counter].split(' ')
    line_counter+=1
    #code
    myP = []
    for s in Pstr:
        myP.append(int(s))
    print myP
    return str(rec(myP,0))
    

##with open('lol.txt', 'r') as f:
with open('B-small-attempt2.in', 'r') as f:
##with open('B-large.in', 'r') as f:
    inp = f.readlines()
    f.close()
line_counter = 0
T = int(inp[line_counter])
line_counter+=1
data = ''
for i in range(T):
    data += 'Case #%d:' %(i+1) + ' ' + sol()+'\n'
with open('output.txt', 'w') as f:
    f.write(data)
    f.close()
print data
print 'done!'
