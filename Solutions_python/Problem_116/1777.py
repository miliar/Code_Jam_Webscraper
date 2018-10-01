Input = open(raw_input("Enter Input Path:"))
InputList = []
for line in Input:
    InputList.append(line[:-1])

Input.close()
T=int(InputList[0])
InputList.pop(0)
OutputList = []
for case in range(T):
    line1 = InputList[case*5]
    line2 = InputList[case*5+1]
    line3 = InputList[case*5+2]
    line4 = InputList[case*5+3]
    column1=line1[0]+line2[0]+line3[0]+line4[0]
    column2=line1[1]+line2[1]+line3[1]+line4[1]
    column3=line1[2]+line2[2]+line3[2]+line4[2]
    column4=line1[3]+line2[3]+line3[3]+line4[3]
    diag1=line1[0]+line2[1]+line3[2]+line4[3]
    diag2=line1[3]+line2[2]+line3[1]+line4[0]
    gotCase=False
    ##Horizontal
    if "T" in line1:
        listLine1=list(line1)
        listLine1.remove("T")
        line1a="".join(listLine1)
        if line1a == "XXX":
            OutputList.append("Case #" + str(case+1) + ": X won")
            gotCase=True
        elif line1a == "OOO":
            OutputList.append("Case #" + str(case+1) + ": O won")
            gotCase=True
    elif line1 == "XXXX":
        OutputList.append("Case #" + str(case+1) + ": X won")
        gotCase=True
    elif line1 == "OOOO":
        OutputList.append("Case #" + str(case+1) + ": O won")
        gotCase=True
    if gotCase == False:
        if "T" in line2:
            listLine2=list(line2)
            listLine2.remove("T")
            line2a="".join(listLine2)
            if line2a == "XXX":
                OutputList.append("Case #" + str(case+1) + ": X won")
                gotCase=True
            elif line2a == "OOO":
                OutputList.append("Case #" + str(case+1) + ": O won")
                gotCase=True
        elif line2 == "XXXX":
            OutputList.append("Case #" + str(case+1) + ": X won")
            gotCase=True
        elif line2 == "OOOO":
            OutputList.append("Case #" + str(case+1) + ": O won")
            gotCase=True
    if gotCase == False:
        if "T" in line3:
            listLine3=list(line3)
            listLine3.remove("T")
            line3a="".join(listLine3)
            if line3a == "XXX":
                OutputList.append("Case #" + str(case+1) + ": X won")
                gotCase=True
            elif line3a == "OOO":
                OutputList.append("Case #" + str(case+1) + ": O won")
                gotCase=True
        elif line3 == "XXXX":
            OutputList.append("Case #" + str(case+1) + ": X won")
            gotCase=True
        elif line3 == "OOOO":
            OutputList.append("Case #" + str(case+1) + ": O won")
            gotCase=True
    if gotCase == False:
        if "T" in line4:
            listLine4=list(line4)
            listLine4.remove("T")
            line4a="".join(listLine4)
            if line4a == "XXX":
                OutputList.append("Case #" + str(case+1) + ": X won")
                gotCase=True
            elif line4a == "OOO":
                OutputList.append("Case #" + str(case+1) + ": O won")
                gotCase=True
        elif line4 == "XXXX":
            OutputList.append("Case #" + str(case+1) + ": X won")
            gotCase=True
        elif line4 == "OOOO":
            OutputList.append("Case #" + str(case+1) + ": O won")
            gotCase=True
    ##Vertical
    if gotCase == False:
        if "T" in column1:
            listcolumn1=list(column1)
            listcolumn1.remove("T")
            column1a="".join(listcolumn1)
            if column1a == "XXX":
                OutputList.append("Case #" + str(case+1) + ": X won")
                gotCase=True
            elif column1a == "OOO":
                OutputList.append("Case #" + str(case+1) + ": O won")
                gotCase=True
        elif column1 == "XXXX":
            OutputList.append("Case #" + str(case+1) + ": X won")
            gotCase=True
        elif column1 == "OOOO":
            OutputList.append("Case #" + str(case+1) + ": O won")
            gotCase=True
    if gotCase == False:
        if "T" in column2:
            listcolumn2=list(column2)
            listcolumn2.remove("T")
            column2a="".join(listcolumn2)
            if column2a == "XXX":
                OutputList.append("Case #" + str(case+1) + ": X won")
                gotCase=True
            elif column2a == "OOO":
                OutputList.append("Case #" + str(case+1) + ": O won")
                gotCase=True
        elif column2 == "XXXX":
            OutputList.append("Case #" + str(case+1) + ": X won")
            gotCase=True
        elif column2 == "OOOO":
            OutputList.append("Case #" + str(case+1) + ": O won")
            gotCase=True
    if gotCase == False:
        if "T" in column3:
            listcolumn3=list(column3)
            listcolumn3.remove("T")
            column3a="".join(listcolumn3)
            if column3a == "XXX":
                OutputList.append("Case #" + str(case+1) + ": X won")
                gotCase=True
            elif column3a == "OOO":
                OutputList.append("Case #" + str(case+1) + ": O won")
                gotCase=True
        elif column3 == "XXXX":
            OutputList.append("Case #" + str(case+1) + ": X won")
            gotCase=True
        elif column3 == "OOOO":
            OutputList.append("Case #" + str(case+1) + ": O won")
            gotCase=True
    if gotCase == False:
        if "T" in column4:
            listcolumn4=list(column4)
            listcolumn4.remove("T")
            column4a="".join(listcolumn4)
            if column4a == "XXX":
                OutputList.append("Case #" + str(case+1) + ": X won")
                gotCase=True
            elif column4a == "OOO":
                OutputList.append("Case #" + str(case+1) + ": O won")
                gotCase=True
        elif column4 == "XXXX":
            OutputList.append("Case #" + str(case+1) + ": X won")
            gotCase=True
        elif column4 == "OOOO":
            OutputList.append("Case #" + str(case+1) + ": O won")
            gotCase=True
    ##Diagonal
    if gotCase == False:
        if "T" in diag1:
            listdiag1=list(diag1)
            listdiag1.remove("T")
            diag1a="".join(listdiag1)
            if diag1a == "XXX":
                OutputList.append("Case #" + str(case+1) + ": X won")
                gotCase=True
            elif diag1a == "OOO":
                OutputList.append("Case #" + str(case+1) + ": O won")
                gotCase=True
        elif diag1 == "XXXX":
            OutputList.append("Case #" + str(case+1) + ": X won")
            gotCase=True
        elif diag1 == "OOOO":
            OutputList.append("Case #" + str(case+1) + ": O won")
            gotCase=True
    if gotCase == False:
        if "T" in diag2:
            listdiag2=list(diag2)
            listdiag2.remove("T")
            diag2a="".join(listdiag2)
            if diag2a == "XXX":
                OutputList.append("Case #" + str(case+1) + ": X won")
                gotCase=True
            elif diag2a == "OOO":
                OutputList.append("Case #" + str(case+1) + ": O won")
                gotCase=True
        elif diag2 == "XXXX":
            OutputList.append("Case #" + str(case+1) + ": X won")
            gotCase=True
        elif diag2 == "OOOO":
            OutputList.append("Case #" + str(case+1) + ": O won")
            gotCase=True
    ##Draw or Unfinished
    if gotCase == False:
        if "." in line1:
            OutputList.append("Case #" + str(case+1) + ": Game has not completed")
            gotCase=True
        elif "." in line2:
            OutputList.append("Case #" + str(case+1) + ": Game has not completed")
            gotCase=True
        elif "." in line3:
            OutputList.append("Case #" + str(case+1) + ": Game has not completed")
            gotCase=True
        elif "." in line4:
            OutputList.append("Case #" + str(case+1) + ": Game has not completed")
            gotCase=True
        else:
            OutputList.append("Case #" + str(case+1) + ": Draw")
            gotCase=True

Output = open(raw_input("Enter Output Path:"), "wb")
for caseline in OutputList:
    Output.write(caseline + "\r\n")

Output.close()