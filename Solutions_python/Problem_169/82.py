import numpy.testing as npt               
        
def Next(N, V, X, s):
        # N == 2
        if N == 1:
                #print s[0][1], X
                if X == s[0][1]:
                        return V/s[0][0]
                else:
                        return 'IMPOSSIBLE'
        else:
                R0, C0 = s[0]
                R1, C1 = s[1]
                if C0 == C1:
                        t = [[R0+R1, C0]]
                        return Next(1, V, X, t)
                if X == C0:
                        return V/R0
                if X == C1:
                        return V/R1
                V0 = (V*X-C1*V)/(C0-C1)
                if V0 < 0: return 'IMPOSSIBLE'
                V1 = V-V0
                #print V1
                if V1 < 0: return 'IMPOSSIBLE'
                T0 = V0/R0
                T1 = V1/R1
                return max(T0,T1)

####		

input = open(r'./B-small-attempt0.in')
#input = open(r'./B-large.in')
#input = open(r'./sample.in')

X = list(input)
C = int(X[0])
Y = [[float(j) for j in x.split()] for x in X[1:]]
#print Y

sol = []



j = 0

#C=10
for i in xrange(C):
	N, V, X = Y[j]
	N = int(N)
	s = Y[j+1: j+N+1]
	sol += [Next(N,V,X, s)]
	j += N+1
	print 'case ', i, 'done'
	#if not i % 100: print 'case ', i+1, 'done'

tofile = True
if tofile:
        with open(r'./outputA.txt', 'w') as output:
                for i in range(len(sol)):
                        output.write('Case #%s: %s\n' % (i+1, sol[i]))
else:
        print sol

	
	
