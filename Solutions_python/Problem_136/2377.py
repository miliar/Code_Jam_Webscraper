Input = open(raw_input("Enter Input Path:"))
InputList = []
for line in Input:
    InputList.append(line[:-1])

Input.close()
T=int(InputList[0])
InputList.pop(0)
OutputList = []
for case in range(T):
    C=float(InputList[case].split()[0])
    F=float(InputList[case].split()[1])
    X=float(InputList[case].split()[2])
    rate=2.0
    time=0
    reachX=False
    while reachX == False:
        timeToC=C/rate
        timeToX=X/rate
        rate+=F
        timeToCX=timeToC+(X/rate)
        if timeToX < timeToCX:
            time+=timeToX
            OutputList.append("Case #"+str(case+1)+": "+str(time))
            reachX=True
        else:
            time+=timeToC

Output = open(raw_input("Enter Output Path:"), "wb")
for caseline in OutputList:
    Output.write(caseline + "\r\n")

Output.close()