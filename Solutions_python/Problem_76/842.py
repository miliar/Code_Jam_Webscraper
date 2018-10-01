import math
def D2B(n,m):
    '''convert denary integer n to binary string bStr'''
    bStr = ''
    if n == 0: return '0'
    while n > 0:
        bStr = str(n % 2) + bStr
        n = n >> 1
    while len(bStr)<m:
        bStr='0'+bStr
    return bStr

f = open('C-small-attempt0.in','r')
lines=f.readlines()
T = int(lines[0] )
for i in range(0,T):
        #print(lines[i])
        N = int(lines[2*i+1])
        line=[int(x) for x in lines[2*i+2].split()]
        #print(Denary2Binary(line[0]))
        
        maxx=0
        
        for j in range(1,int(math.pow(2,N))-1):
                b=D2B(j,N)
                #print(b)
                ssum=0
                Sean=0
                Patrick=0
                for k in range(0,N):
                        if(b[k]=='1'):
                                ssum+=line[k]
                                Sean=Sean^line[k]
                                #print(Sean)
                        else:
                                Patrick=Patrick^line[k]
                #print('p: ' , (Patrick))
                #print('sum: ',ssum)
                #print('max: ',maxx)
                if(Sean==Patrick and ssum>maxx):
                        maxx=ssum
        if(maxx==0):
                print('Case #%d: NO' % (i+1))
        else:
                print('Case #%d: %d' % (i+1,maxx))
