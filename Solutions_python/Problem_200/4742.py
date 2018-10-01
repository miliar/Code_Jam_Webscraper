
def tidy(N):
	s = str(N)
	for i in xrange(len(s)):
		if i < len(s)-1 and s[i+1] < s[i]:
			return False
		#end if
	#end for
	return True

def largest_tidy(l):
	s = ''
	for i in xrange(l):
		s += '9'
	return list(s)

# def next_tidy(s):
# 	print s
# 	for i in xrange(len(s)-1,0,-1):
# 		if s[i-1] == s[i]:
# 			s[i-1] = int(s[i])-1
# 			break
# 		elif 
# 		#end if 
# 	#end for
# 	return s

# last tidy number
# def last_tidy(N):
# 	n = largest_tidy(len(str(N)))
# 	while True:
# 		if n < N and tidy(n):
# 			break
# 		else:
# 			next_tidy(n)
# 		#end if
# 	#end
# 	return "".join(n)

def last_tidy(N):
	for i in xrange(N,0,-1):
		if tidy(i):
			return i
		#end if
	#end if
	return 1

if __name__ == "__main__":
	T = int(raw_input())
	for i in xrange(1,T+1,1):
		N = int(raw_input())
		print "Case #{0}: {1}".format(i,last_tidy(N))
	#end for
#end if