def flipk(p,k,f):
    i=f
    m = p[i:k+i] #minus k segment of series
    #print m
    #flip pancakes
    m = m.replace('+', '2').replace('-', '+').replace('2', '-')
    np = p[:i] + m + p[k + i:]
    return np

def checkAllNeg(p):
    if p == '-' * len(p):
        return True
    else:
        return False

def checkComplete(p):
    if p == '+' * len(p):
        return True
    else:
        return False

def cookPancakes(pc, k):
    lf = len(pc)-k+1
    #print lf
    s = pc
    m = 0
    for r in range(0, lf):
        if checkComplete(s) == True:
            return m
        #print 'r = '+ str(r)
        if r != (lf-1):
            if s[r] == '-':
                s = flipk(s, k, r)
                m = m +1
        else:
            if checkAllNeg(s[r:]) == True:
                return str(m+1)
            else:
                return 'IMPOSSIBLE'


k = 4
x = '-+-+-'
#flipk(x,3,0)
#print(cookPancakes(x, k))

# read input N
file = open("A-large.in", "r")
Testcases = int(file.readline())
#print Testcases

outfile = open("A-large.out","w")

for x in range(1, Testcases+1):
    val = file.readline()
    NewVal = val.split(' ')
    c = NewVal[0]
    k = int(NewVal[1])
    result = cookPancakes(c,k)
    #print result
    OutputText = "Case #" + str(x) + ": " + str(result)
    outfile.write(OutputText + '\n')

file.close()
outfile.close()