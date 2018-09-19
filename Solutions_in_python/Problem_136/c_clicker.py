import sys
fopen=open('/Users/subodhyadav/Desktop/B-large.in.txt','r')
fout=open('/Users/subodhyadav/Desktop/B-large.out.txt','a')
for k in xrange(int(fopen.readline().strip())):
	c,f,x=map(float,fopen.readline().strip().split())
	multi,temp=2.0,0.0
	t_time=x/multi
	while True:
		cache=multi+f
		temp+=c/multi
		temp_time=temp+x/cache
		if temp_time<t_time:
			t_time=temp_time
			multi=cache
		else:
			break
	fout.write("Case #")
	fout.write(str(k+1))
	fout.write(": ")
	fout.write(str(t_time))
	fout.write("\n")
fout.close()
fopen.close()