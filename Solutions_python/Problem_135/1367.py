

def solve_case(case):
	answer1=case.pop(0)[0]
	answer2=case.pop(4)[0]
#	print answer1, answer2
	arr1=case[:4]
	arr2=case[4:]
	cards=filter(lambda x: x in arr2[answer2-1],arr1[answer1-1])
	if len(cards)==1: return str(cards[0])
	if len(cards)>1: return "Bad magician!" 
	if len(cards)==0: return "Volunteer cheated!"















import Code_Ninja_Contest_Utilities as cncu
numcases, cases=cncu.read_infile("in.txt",True)
cases=cncu.grouplist(cases,10)
cases=[[map(int,x) for x in z] for z in cases]
#print cases[0], "\n" ,cases[1]
ans=[solve_case(x) for x in cases]
print ans
cncu.write_outfile(ans,"out.txt")
