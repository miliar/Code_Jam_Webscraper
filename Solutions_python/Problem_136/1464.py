#!/usr/local/bin/python3
op = open("op.txt", "w");
T = int(input());
for t in range(1,T+1):
  c, f, x = input().split();
  c = float(c);
  x = float(x);
  f = float(f);
  
  oIdx = 0;
  oBase = 0;
  oNextF = c/2;
  oFinal = x/2;
  
  while(5 > 3):
    nIdx = oIdx+1;
    nBase = oNextF;
    nNextF = nBase + c/(2+nIdx*f);
    nFinal = nBase + x/(2+nIdx*f);
    
    if(nFinal > oFinal):
      y = oFinal;
      break;
    
    oIdx = nIdx;
    oBase = nBase;
    oNextF = nNextF;
    oFinal = nFinal;
  
  strng = "Case #"+ str(t)+': '+"%.7f"%y+'\n';
  op.write(strng);

op.close();
