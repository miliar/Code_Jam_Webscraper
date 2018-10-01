

def gobath(seat, num):
	l = [seat]
	#print l
	while num != 1:
		a = l.pop(0)
		if (a-1) % 2 == 0:
			l.append((a-1) / 2)
			l.append((a-1) / 2)
			l.sort(reverse = True)
		else:
			l.append(a / 2)
			l.append((a / 2) - 1)
			l.sort(reverse = True)
		num-=1
		#print l
		#print a
	a = l.pop(0)
	if (a-1) % 2 == 0:
		return ((a-1) / 2), ((a-1) / 2)
	else:
		return (a / 2), (a / 2) -1

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  ans1, ans2 = gobath(n, m)
  print "Case #{}: {} {}".format(i, ans1, ans2)
  # check out .format's specification for more formatting options