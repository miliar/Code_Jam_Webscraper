#!/usr/bin/python
t = int(input())
for i in range(1, t + 1):
        p, k = [s for s in raw_input().split(" ")]
	st=list(p)
	times=0
        for j in range(0,len(st)-int(k)+1):
                if st[j]=='+':
                        continue
		lastmin=0
		for f in range(0,int(k)):
			if st[j+f]=='+':
				st[j+f]='-'
				lastmin=1
			else:
				st[j+f]='+'
		times+=1
	if '-' in st:
                print("Case #{}: IMPOSSIBLE".format(i,times))
        else:
                print("Case #{}: {}".format(i,times))
