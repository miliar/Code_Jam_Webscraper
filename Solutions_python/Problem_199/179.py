import string 

T = int(raw_input())

flip = string.maketrans('+-','-+')

def process(s, K):
	ans, current = 0, 0
	while current + K <= len(s):
                 if s[current] == '+' : current+=1
                 else : 
                     s = s[:current] + s[current:(current+K)].translate(flip) + s[(current+K):]
                     ans+=1
                     current+=1
    	return "IMPOSSIBLE" if '-' in s else str(ans) 

for test in xrange(T):
	S, K =  raw_input().split()
	tmp = process(S, int(K))
	print "Case #%d: %s"%(test+1, process(S, int(K)))   
