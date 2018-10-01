f = open("B-large.in","r").read().split('\n')
f2 = open("out2_l.txt","w")
C = 1
for i in f[1:]:
	if len(i) == 0: continue
	t = 0
	ans = []
	for j in range(1,len(i)):
		if i[j] == i[j-1]: continue
		if i[j] > i[j-1]: t = j
		else:
			for k in range(len(i)):
				if k < t: ans.append(i[k])
				elif k == t: ans.append(chr(ord(i[k])-1))
				else: ans.append('9')
			break
	r_ans = None
	if len(ans) == 0: r_ans = i
	else: r_ans = "".join(ans)
	f2.write("Case #{}: {}\n".format(C, int(r_ans)))
	C += 1
f2.close()
