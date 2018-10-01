def Exist(s1,s2):
    s1=s1.split(" ")
    s2=s2.split(" ")
    num=0
    sol=0
    for i in s1:
        for j in s2:
            if(i==j):
                sol=i
                num+=1
    if(num==1):
        return sol
    if(num>1):
        return "Bad magician!"
    if(num==0):
        return "Volunteer cheated!"

with open ("A-small-attempt0.in", "r") as myfile:
    problem=myfile.read()
lines = problem.split('\n')
cases = int(lines[0])
for i in range(cases):
    index = i*10+1
    case=lines[index:index+11]
    first=int(case[0])
    second=int(case[5])
    firstLine=case[first]
    secondLine=case[second+5]
    result=Exist(firstLine,secondLine)
    caseNum=i+1
    print("case #"+str(i+1)+": " + result)
