import sys
import fileinput
MaxCaseNum=0
CaseNum=0

CurInStr=""
CurInStrSplit=();

MinReqPlants=0
ShyMax=0
ActiveAud=0
for line in fileinput.input():

    if MaxCaseNum==0:
        MaxCaseNum=int(line)
        continue
    CaseNum+=1
    CurInStr=str(line)
    CurInStrSplit=CurInStr.partition(" ")
    MinReqPlants=0
    ActiveAud=0
    ShyMax=int(CurInStrSplit[0])
    #print "Init CaseNum %d, ShyMax %d, InStr %s" % (CaseNum, ShyMax, (CurInStrSplit[2]),)
    for index in range(0, ((len(CurInStrSplit[2])-1) ) ):
        if (ActiveAud+MinReqPlants)>=ShyMax:
            #print " Breaking CaseNum%d: ActiveAud %d index%d indVal%d MRP %d" % (CaseNum, ActiveAud, index, int((CurInStrSplit[2])[index]), MinReqPlants)
            break
        if((ActiveAud+MinReqPlants)>=index):
            ActiveAud+=int((CurInStrSplit[2])[index])
            #print " NoIncrem CaseNum%d: ActiveAud %d index%d indVal%d MRP %d" % (CaseNum, ActiveAud, index, int((CurInStrSplit[2])[index]), MinReqPlants)
        else:
            MinReqPlants+=(index-(ActiveAud+MinReqPlants))
            ActiveAud+=int((CurInStrSplit[2])[index])
            #print " Incremen CaseNum%d: ActiveAud %d  index %d  indVal %d  MRP %d" % (CaseNum, ActiveAud, index, int((CurInStrSplit[2])[index]), MinReqPlants)
    #print " Fin Case #%d: %d" % (CaseNum, MinReqPlants)
    #print "\n"    
    print "Case #%d: %d" % (CaseNum, MinReqPlants)


    
