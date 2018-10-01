import math

def isFair(x):
    s=str(x)
    for i in xrange(0,len(s)):
	if s[i]!=s[len(s)-1-i]: return False
    return True


if __name__=="__main__":
    T=int(raw_input())
    for t in xrange(1,T+1):
	count=0
	A,B=[int(_) for _ in raw_input().split()]
	for i in xrange(A,B+1):
	   if (isFair(i) and math.sqrt(i).is_integer() and isFair(math.trunc(math.sqrt(i)))): count+=1
	print("Case #"+str(t)+": "+str(count))
