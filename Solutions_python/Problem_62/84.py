#!/usr/bin/env python3
T=int(input());
for Case in range(1,T+1):
  N=int(input());
  Ropes=[tuple(map(int,input().split())) for i in range(N) ];
  Ans=0;
  for Num,(Left1,Right1) in enumerate(Ropes):
    for Left2,Right2 in Ropes[Num+1:]:
      if (Left1-Left2)*(Right1-Right2)<0 :
        Ans=Ans+1;
  print('Case #{Case}: {Ans}'.format(**locals()));
