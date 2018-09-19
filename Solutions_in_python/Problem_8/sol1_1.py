
def CreateSeive(A,B,P):
        sieve=[x for x in range(2,B+1)]
        ns=[]
        primes=[]
        while (len(sieve)>0):
                cur = sieve[0]
                if cur>=P:
                        primes.append(sieve[0])
                ns = [x for x in sieve if (x%cur > 0)]
                sieve = ns
        return primes        


def Solve(A,B,P):
        l = [[] for i in range(A,B+1)]
        primes = CreateSeive(A,B,P)
        for i in primes:
                if A%i == 0:
                        # A
                        st = 0
                else:
                        st = i-A%i
#                st = i-A%i
                h = st
                while (A+h<B+1):
                        l[h].append(i)
                        h += i
        l1 = [set(x) for x in l]
      #  print l1
        sofar=[]
        for x in l1:
               # print repr(x)+'...'+repr(sofar)
                s1=[]
                s2=x
                for y in sofar:
                     if y&s2 == set():
                            s1.append(y)
                     else:
                        s2 = s2|y
         #       print repr(s1)+'    '+repr(s2)
                sofar = s1
                sofar.append(s2)
        return len(sofar)
                        
#--------------------

f=open('c:\\Python25\\Scripts\\inputfile.txt','r')
fout=open('c:\\Python25\\Scripts\\outputfile1.txt','w')
N=int(f.readline())
print N
for i in xrange(1,N+1):
        l = f.readline()
        l=l.split()
        A=long(l[0])
        B=long(l[1])
        P=long(l[2])
        result = Solve(A,B,P)	
	fout.write('Case #'+repr(i)+': '+repr(result)+'\n')
	print 'Case #'+repr(i)+': '+repr(result)+'\n'
f.close()
fout.close()
