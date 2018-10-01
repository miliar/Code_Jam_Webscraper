f = open("in.txt","rt")
t = int(f.readline())
for rr in range(0,t):
	n = 4
	ans1 = int(f.readline())
	a = []
	for i in range(0,n):
		a.append(map(int,f.readline().split()))
	ans2 = int(f.readline())
	b = []
	for i in range(0,n):
		b.append(map(int,f.readline().split()))
	a1 = [x for x in a[ans1-1]]
	a2 = [x for x in b[ans2-1]]
	b3 = [val for val in a1 if val in a2]
	if len(b3) == 0:
		print("Case #"+str(rr+1)+": Volunteer cheated!")
		continue
	if len(b3) > 1:
		print("Case #"+str(rr+1)+": Bad magician!")
		continue
	print("Case #"+str(rr+1)+": "+str(b3[0]))
	