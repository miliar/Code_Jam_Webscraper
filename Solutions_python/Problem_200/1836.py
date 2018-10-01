def tidyNum(n):
	n = [int(d) for d in str(n)]
	if len(n) == 1:
		return ''.join([str(d) for d in n])
	else:
		for i in range(len(n))[:0:-1]:
			if n[i] < n[i-1]:
				n[i-1] = n[i-1]-1
				n[i:] = [9]*(len(n)-i)
				# for j in range(i,len(n)):
				# 	n[j] = 9
				if n[i-1] == 0 and i == 1:
					del(n[i-1])
				
		return int(''.join([str(d) for d in n]))

def main():
	t = int(raw_input())
	for i in xrange(1, t+1):
		n = int(raw_input())
		print "Case #{}: {}".format(i, tidyNum(n))

		#n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  		#print "Case #{}: {} {}".format(i, n + m, n * m)
  	# check out .format's specification for more formatting options

main()