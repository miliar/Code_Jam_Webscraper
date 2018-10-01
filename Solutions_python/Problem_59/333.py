s = file('a.txt').readlines()
k = 1
a = int(s[0])
sss = ""
for i in range(a):
	tem = s[k]
	m,n = map(int,tem.split())
	dic = []
	name = []
	k +=1
	y = 0
	for j in range(m):
		dic.append(s[k].replace('\n',''))
		k+=1
	for j in range(n):
		tem=s[k].replace('\n','')
		temp = tem.split('/')
		for kk in range(len(temp)+1):
			tt = '/'.join(temp[0:kk])
			if tt and tt not in dic:
				y+=1
				dic.append(tt)
		k+=1
        sss += "Case #"+str(i+1)+": "+str(y)+'\n'

w= open('out.txt','w')
w.write(sss)
w.close()
