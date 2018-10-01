def convert_to_int( a ):
	temp=a.strip();
	ans = map(int,temp.split(' '))
	return ans


def display_answer(r1,r2,i):
	R1=convert_to_int(r1)
	R2=convert_to_int(r2)
	result=set(R1).intersection(R2)
	if len(result)==0:
		print 'Case #'+str(i)+': '+'Volunteer cheated!'
	if len(result)>1:
		print 'Case #'+str(i)+': '+'Bad magician!'
	if len(result)==1:
		print 'Case #'+str(i)+': '+str(result.pop())


	
	
fin=open("input.txt","r")
test_cases=[]
test_cases=fin.readlines()

no=int(test_cases[0][0:-1])
counter = 1

for i in range(1,no+1):
	
		
	first_no=int(test_cases[counter].strip())
	first_row = test_cases[counter+first_no]
	counter+=5
	
	second_no = int(test_cases[counter][0:-1])
	second_row =test_cases[counter+second_no]
	counter+=5
	display_answer(first_row,second_row,i)


