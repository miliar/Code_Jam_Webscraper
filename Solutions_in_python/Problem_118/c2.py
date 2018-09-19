from itertools import product

def palindromeNum(n):
   return [n*'%s'%tuple(list(i)+list(i[n*(n-1)/2%(n-1)-1::-1])) for i in product(*([range(1,10)]+[range(0,10)]*((n+1)/2-1)))]
#n>1

ppp = map(palindromeNum, [3,4,5,6,7])
pp=[]
for i in range(5):
    for j in ppp[i]:
        pp.append(int(j))

#print pp
p=[1, 4, 9, 121, 484]

for j in pp:
#    print j
    num = j*j;
    n = num;
    rev = 0;
    while (num > 0):
          dig = num % 10;
          rev = rev * 10 + dig;
          num = num / 10;
#    print rev, n
    if(rev==n):
        p.append(j*j)

#print p
                
with open('cc.txt','r') as f:
    n = int(f.readline())
    for i in range(n):
        ret = 0
#        line = f.readline()
        m,n = (f.readline()).split(' ')
        

        for j in p:
            if(j<=int(n) and j>=int(m)):
                ret = ret + 1
        
        print 'Case #'+str(i+1)+': ' + str(ret)
        
        
        