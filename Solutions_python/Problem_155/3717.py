f_in = open('A-small-attempt1.in', 'r')
f_out = open('codejam_0.out','w')
no_case = int(f_in.readline())
n =0
a =1
answer = []
while n<no_case:
	in_str= f_in.readline()
	l=in_str.split(" ")
	
	s_max=l[0]
	min_frnds = 0
	audiance= 0
	m=1
	s_levels= list(l[1])
	while m<=int(s_max):
		 
		 audiance = audiance + int(s_levels[m-1])
		  
		 
		 if int(s_levels[m])!=0:
			 if audiance < m:
				 min_frnds = min_frnds + m - audiance
				 audiance = audiance + min_frnds
			 
		 
		 m=m+1
	answer.append(min_frnds)
	n= n+1
	

for i in range(0,no_case):
	out = "Case #"+str(a)+": "+str(answer[i])+"\n"
	f_out.write(out)
	a=a+1
f_out.close()

