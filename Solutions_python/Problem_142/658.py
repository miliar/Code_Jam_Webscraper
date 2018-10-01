#!/usr/bin/python
f = open("A-small-attempt0.in", "r")
testcase = int(f.readline())
for qq in range(testcase): #i is testcase
    ans1 = 0

    testline = f.readline()

    splitline = f.readline().split()
    row1=splitline
    row1[len(row1)-1] = row1[len(row1)-1].rstrip('\n')

    splitline2 = f.readline().split()
    row2=splitline2
    row2[len(row2)-1] = row2[len(row2)-1].rstrip('\n')

    row3=[]
    row4=[]

    row5=[]
    row6=[]

    for i in range(len(row1[0])):
        if i == 0:
            row3.append(row1[0][0])
            row5.append(1)
        if i!=0 and row1[0][i]!=row3[-1]:
            row3.append(row1[0][i])
            row5.append(1)
        elif i!=0 and row1[0][i]==row3[-1]:
            row5[-1]+=1

    for i in range(len(row2[0])):
        if i == 0:
            row4.append(row2[0][0])
            row6.append(1)
        if i!=0 and row2[0][i]!=row4[-1]:
            row4.append(row2[0][i])
            row6.append(1)
        elif i!=0 and row2[0][i]==row4[-1]:
            row6[-1]+=1

    if(row3!=row4):
        print ('Case #'+str(qq+1)+': Fegla Won')
        continue;
    for i in range(len(row5)):
        ans1 += abs(row5[i]-row6[i])
    print('Case #'+str(qq+1)+': '+str(ans1))
    del row1[0:len(row1)]
    del row2[0:len(row2)]
    del row3[0:len(row3)]
    del row4[0:len(row4)]
    del row5[0:len(row5)]
    del row6[0:len(row6)]

