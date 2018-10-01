file_name='A-large.in'
f=open(file_name,'r')
n=eval(f.readline())
result=open('a.out','w')
for i in range(n):
	[s_max, s]=f.readline().split()
	s_max=eval(s_max)
	standing=0
	need=0
	for j in range(s_max+1):
		if standing<j:
			tmp=j-standing
			need+=tmp
			standing+=tmp
		standing+=eval(s[j])
	result.write('Case #'+str(i+1)+': '+str(need)+'\r')
f.close()
result.close()