fhand=open('B-large.in','r')
def orders(num):
	for i in range(len(num) - 1):
		if num[i] > num[i + 1]:
			return False
	return True
def solve(we):
	x=str(we)
	for i in range(len(x) - 1): 
		if x[i+1]<x[i]:
			we-=int(x[i+1:])+1
			break
	return we
t=int(fhand.readline())

fhand2=open('outputtt.txt','w')
for cases in xrange(1,t+1):

    	w=int(fhand.readline().rstrip())

	while orders(str(w))==False:
		w=solve(w)
  	fhand2.write ('Case #%d: ' %(cases))
	fhand2.write ('%d' %(w)+'\n')
