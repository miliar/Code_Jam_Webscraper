#!/usr/bin/python
f = open("D-large.in", "r")
testcase = int(f.readline())
for i in range(testcase): #i is testcase
    ans1 = 0
    ans2 = 0
    row1 = []
    row2 = []
    row3 = []
    row4 = []
    numofstone=int(f.readline())
    splitline = f.readline().split(' ')
    row1=splitline
    splitline = f.readline().split(' ')
    row2=splitline
    if numofstone==1:
        row1[0] = row1[0].rstrip('\n')
        row2[0] = row2[0].rstrip('\n')
    else:
        row1[len(row1)-1] = row1[len(row1)-1].rstrip('\n')
        row2[len(row2)-1] = row2[len(row2)-1].rstrip('\n')
    row3=list(row1)
    row4=list(row2)
    #liar
    for j in range(numofstone):
        if min(row1)>max(row2):
            ans1+=numofstone-j
            break
        elif min(row2)>max(row1):
            break
        if max(row1)<max(row2):
            del row1[row1.index(min(row1))]
            del row2[row2.index(max(row2))]
        else:
            del row1[row1.index(max(row1))]
            del row2[row2.index(max(row2))]
            ans1+=1
    #stupid
    for j in range(numofstone):
        if min(row4)>max(row3):
            break
        elif min(row3)>max(row4):
            ans2+=numofstone-j
            break
        if max(row3)<max(row4):
            del row3[row3.index(max(row3))]
            del row4[row4.index(max(row4))]
        else:
            del row3[row3.index(max(row3))]
            del row4[row4.index(min(row4))]
            ans2+=1
    print('Case #'+str(i+1)+': '+str(ans1)+' '+str(ans2))
    del row1[0:len(row1)]
    del row2[0:len(row2)]
