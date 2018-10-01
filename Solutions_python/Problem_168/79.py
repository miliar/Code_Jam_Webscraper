

def previously(x):
        #another fun
        return x
                
        
def Next(s):
        # Whatever needs to be done
        count = 0
        checkedrows = []
        checkedcols = []
        flame = False
        for i in range(R):
                for j in range(C):
                        if s[i][j] == '.':
                                pass
                        else:
                                for k in range(j):
                                        if s[i][k] != '.':
                                                break
                                else:
                                        flame = True
                                        if s[i][j] == '<':
                                                count += 1
                                for k in range(i):
                                        if s[k][j] != '.':
                                                flame = False
                                                break
                                else:
                                        if s[i][j] == '^':
                                                count += 1
                                for k in range(j+1, C):
                                        if s[i][k] != '.':
                                                flame = False
                                                break
                                else:
                                        if s[i][j] == '>':
                                                count += 1
                       
                                for k in range(i+1, R):
                                        if s[k][j] != '.':
                                                flag = False
                                                break
                                else:
                                        if s[i][j] == 'v':
                                                count += 1
                                        if flame == True:
                                                return 'IMPOSSIBLE'                      
        return count
        
####		

#input = open(r'./A-small-attempt0.in')
input = open(r'./A-large.in')
#input = open(r'./sample.in')

X = list(input)
C = int(X[0])
Y = [[j for j in x.split()] for x in X[1:]]
#print Y

sol = []



j = 0 #counter if needed

#C=10
for i in xrange(C):
	R,C= Y[j]
	#print R, C
	R = int(R)
	C = int(C)
	s= [list(t[0]) for t in Y[j+1:j+R+1]]
	#print s
	j += R+1
	sol += [Next(s)]
	#print 'case ', i+1, 'done'
	if i < 3: print 'case ', i+1, 'done'
	if not i % 10: print 'case ', i+1, 'done'

tofile = True
if tofile:
        with open(r'./outputA.txt', 'w') as output:
                for i in range(len(sol)):
                        output.write('Case #%s: %s\n' % (i+1, sol[i]))
else:
        print sol

	
	
	
	
	
	
	
	
	
	
