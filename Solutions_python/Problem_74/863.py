import sys
from bisect import bisect

cases=int(sys.stdin.readline())

for j in range(0, cases):
   inst=sys.stdin.readline().split()
   total=int(inst[0])
   o_pos=1
   o_move=0
   b_pos=1
   b_move=0
   time=0
   for i in range (1, total*2, 2):
      if(inst[i]=='O'):
         dis=max(abs(int(inst[i+1])-o_pos)-o_move, 0)+1
         b_move+=dis
         time+=dis
         o_move=0
         o_pos=int(inst[i+1])
      else:
         dis=max(abs(int(inst[i+1])-b_pos)-b_move, 0)+1
         o_move+=dis
         time+=dis
         b_move=0
         b_pos=int(inst[i+1])
      #print "Time: %d, o_pos: %d o_move: %d, b_pos: %d, b_move: %d"%(time, o_pos, o_move, b_pos, b_move)
   print "Case #%d: %d"%(j+1, time)
