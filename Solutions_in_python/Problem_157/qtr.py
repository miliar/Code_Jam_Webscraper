
tr= {
	(1,1) : 1,
	(1,2) : 2,
	(1,3) : 3,
	(1,4) : 4,

	(2,1) : 2,
	(2,2) : -1,
	(2,3) : 4,
	(2,4) : -3,

	(3,1) : 3,
	(3,2) : -4,
	(3,3) : -1,
	(3,4) : 2,

	(4,1) : 4,
	(4,2) : 3,
	(4,3) : -2,
	(4,4) : -1
}

ma = {
	'1' : 1,
	'i' : 2,
	'j' : 3,
	'k' : 4
 }
def calc(i,j):
	ii = abs(i)
	jj = abs(j)

	v = (i/ii) * (j/jj) * tr[(ii,jj)]
	return v


def trans(c):
	return ma[c]

def print_result(t, s):
	print "Case #" + str(t) + ": " + s

t = int(raw_input())

for tt in range(1,t+1):
	(n,k) = map(int, raw_input().split(' '))

	s = raw_input()

	arr = map(trans , s*k)

	l = len(arr)
	#print arr
	forward = [0] *l
	back = [0]*l

	forward[0] = arr[0]
	for i in range(1,l):
		forward[i] = calc(forward[i-1], arr[i])

	back[l-1] = arr[l-1]

	for i in range(l-2,-1,-1):
		back[i] = calc( arr[i], back[i+1])

	#print forward, back

	chk = False
	for i in range(1,l-1):
		#print i
		if forward[i] == 4 and back[i+1] ==4:
			#print i,
			for j in range(0,i):
				if forward[j] == 2:
					#print_result(tt, "YES")
					chk = True
					break

		if chk:
			break

	if chk:
		print_result(tt, "YES")
	else:
		print_result(tt, "NO")


