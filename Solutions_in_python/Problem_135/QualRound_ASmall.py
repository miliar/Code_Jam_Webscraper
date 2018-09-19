'''
Created on Apr 12, 2014

@author: ahmed
'''

inFile=open("A-small-attempt1.in","r")

outFile=open("QualRound_ASmall.out","w")


Lines=inFile.readlines()
TestCaseNo=int(Lines[0])
print TestCaseNo
Lines=Lines[1:]            
for i in range(TestCaseNo):
    index=i*10
    print index, Lines[index]
    L1=int(Lines[index])
    FirstLine=set(Lines[L1+index].split())
    L2=int(Lines[index+5])
    SecondLine=set(Lines[L2+index+5].split())
    print "f", FirstLine , L1
    print "S", SecondLine, L2
    OutSet=SecondLine.intersection(FirstLine)
    Out_Len=len(OutSet)
    if Out_Len==1:
        print>>outFile,"Case #%s: "%(i+1),OutSet.pop()
        continue
    if Out_Len>0: 
        print>>outFile,"Case #%s: "%(i+1), "Bad magician!"
        continue
    if Out_Len==0: 
        print>>outFile,"Case #%s: "%(i+1), "Volunteer cheated!"
        continue