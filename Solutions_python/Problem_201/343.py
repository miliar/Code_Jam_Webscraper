#returns the number of people on each side if one guy enters a this-sized empty room
#given 8, returns (4,3)
def bisect(a):
	a -= 1
	r = a//2
	l = a-r
	return (l,r)

#simple, expensive solution
#the obvious one would be O(n^2) and use an array of [empty,empty,full,empty,empty], then look for empty runs
#but we'd rather store sizes of the holes [2, 2], both faster and easier
#lots of optimizations are possible, for example using priority queue rather than sorting after each step or removing size-0 holes,
#but there's no point, this is used only to verify the fast one
def f(s,p):
	l = [s]
	while p:
		hl,hr = bisect(l.pop())
		l.append(hl)
		l.append(hr)
		l = sorted(l) # we only ever want the largest element, this is overkill, but it's easy and it works
		p -= 1
		if p==0:
			return (hl,hr)

#but since the limit is 10^18, there must be a sub-linear algorithm:
#every time someone joins an empty room, he takes the middle stall, yielding two problems of half as many people and a half as big room
#if we can find how many people go to each room, we don't need to solve the other one
#if there's an even number of guys in total, there's an odd number after the current guy, so our final guy goes left; otherwise, right
#the other half can be discarded, yielding O(log n) runtime
def f2(s,p):
	while p>1:
		if p&1:
			_,s = bisect(s)
			p //= 2
		else:
			s,_ = bisect(s)
			p //= 2
	return bisect(s)

#test that both algorithms give same answer
#(can't prove this tester is below O(n^4 log n), don't care, n is low)
for a in range(32):
	a+=1
	for b in range(a):
		b+=1
		if f(a,b) != f2(a,b):
			print(a, b, f(a,b), f2(a,b))

for L in range(int(input())):
	(holes,pigeons) = [t(s) for t,s in zip((int,int),input().split())]
	
	l,r = f2(holes,pigeons)
	print("Case #"+str(L+1)+":", l, r)
