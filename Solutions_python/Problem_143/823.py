import fileinput

leggi=fileinput.input()
numCases=(int)(leggi.readline().strip())

for case in range(numCases):
    l=leggi.readline().strip().split()	
    a=int(l[0])
    b=int(l[1])
    k=int(l[2])
    l=[x&y for x in range(a) for y in range(b) if x&y < k]
    print("Case #"+str(case+1)+": "+str(len(l)),sep='')

   