
t = int(input())
for i in range(1, t + 1):
	s = input().split(" ")
	n = (int(s[1]))
	d = (int(s[0]))
	tm = 0.0;
	for j in range(n):
		s = input().split(" ")
		ki = (int(s[1]))
		si = (int(s[0]))
		ti = (d-si)/ki
		tm = max(tm,ti)
	print("Case #{}: {}".format(i, d/tm))
	
