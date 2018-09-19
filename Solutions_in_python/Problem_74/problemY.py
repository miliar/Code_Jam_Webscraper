# -*- coding: utf-8 -*-
def getPos(pos,tar,diff):
  if pos >= tar:
    return pos-diff
  else:
    return pos+diff

def ans(line):
  sLine = line.strip().split()
  num = int(sLine[0])
  if num==0:
    return 0
  butO =[]
  butB = []
  chance = 1
  #print sLine
  if sLine[1]=='B':
    chance = 2;  
  i = 1
  chanceL=[]
  while i<len(sLine):
    if sLine[i]=='B':
      chanceL.append(2)
      butB.append(int(sLine[i+1]))
    else:
      chanceL.append(1)
      butO.append(int(sLine[i+1]))
    i+=2
  curTarO = 0;#butO[0]
  curTarB= 0;#butB[0]
  curPosO=1;
  curPosB=1;
  step =0;
  indO=0;
  indB=0;
  chanceInd=0
  #print chanceL
  while chanceInd<len(chanceL):
    
    #print chanceInd,curPosO,curPosB,indO,indB
    chance = chanceL[chanceInd]
    if chance==1:
      curTarO = butO[indO]
      diff1 = abs(curTarO-curPosO)
      if indB<len(butB):
	curTarB = butB[indB]	
	diff2 = abs(curTarB-curPosB)
	if diff2 <= (diff1+1):
	  curPosB = curTarB;
	else:
	  curPosB = getPos(curPosB,curTarB,diff1+1)
      step+=diff1+1;
      
      curPosO = curTarO;
      chanceInd+=1
      indO+=1
    else:
      curTarB = butB[indB]
      diff1 = abs(curTarB-curPosB)
      if indO<len(butO):
	curTarO = butO[indO]
	diff2 = abs(curTarO-curPosO)
	if diff2<=(diff1+1):
	  curPosO = curTarO;
	else:
	  curPosO = getPos(curPosO,curTarO,diff1+1)
      step+=diff1+1;      
      curPosB = curTarB; 
      chanceInd+=1
      indB+=1
  return step
  

if __name__=="__main__":
  import sys
  line=sys.stdin.readline()
  M=int(line.strip())
  for caseI in range(1,M+1):
    print "Case #"+str(caseI)+": "+str(ans(sys.stdin.readline()));
    #line=sys.stdin.readline()
    