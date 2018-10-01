import sys

f=sys.stdin
fout=sys.stdout
case_num=int(f.readline())
#print case_num
for i in range(case_num):
	info=f.readline()
	#print info
	use=info.split()
	shy_level=int(use[0])
	digit=use[1]
	#print shy_level
	#print digit[0]
	num=0
	sum=0;
	for j in range(1,shy_level+1):
		sum=int(digit[j-1])+sum
		diff=j-sum
		if diff>0:
			sum=sum+diff
			num+=diff
	print "Case #"+str(i+1)+": "+str(num)

sys.stdout=fout
fout.close()



