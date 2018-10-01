number_of_rows = 4
Final = ''
T = int(input())
for CaseID in range(1,T+1):
	Answer1 = int(input())
	rowA = [list(map(int,input().split())) for i in range(0,number_of_rows)]
	Answer2 = int(input())
	rowB = [list(map(int,input().split())) for i in range(0,number_of_rows)]
	Answer = set(rowA[Answer1-1]) & set(rowB[Answer2-1])
	if Answer == set():
		Answer = "Volunteer cheated!"
	elif len(Answer)>1:
		Answer = "Bad magician!"
	else:
		Answer = str(Answer.pop())
	Final +="Case #" +str(CaseID) +": "+ Answer + "\n"
print(Final)