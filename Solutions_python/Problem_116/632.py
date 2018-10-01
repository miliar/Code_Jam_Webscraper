
import sys, os

_debug_ = False

if 'debug' in sys.argv:
 _debug_ = True

def log(mesg):
 if _debug_ : print mesg

text = sys.stdin.read().strip()

cases=text.split("\n\n")

cases[0] = "\n".join(cases[0].split()[1:])

diags= {
		(0,0 + 4) : 8,
		(0,3 + 4) : 9,
		(1,1 + 4) : 8,
		(1,2 + 4) : 9,
		(2,1 + 4) : 9,
		(2,2 + 4) : 8,
		(3,0 + 4) : 9,
		(3,3 + 4) : 8
	}



casenum=0
for c in cases:
 log("c is:\n"+c)
 gameompleted=True
 casenum+=1
 xcombos=[ i for i in range(10) ]
 ocombos=xcombos[:]
 #print c
 k = 0
 for symbol in c:
   i = k/4
   j=k%4 + 4
   # i, j may be invalid dont forget
   if symbol == 'X':
     k+=1
     for d in ( i, j, diags.get((i,j))):
       try:
         if -1 < d < 10: ocombos.remove(d)
       except ValueError,e:
         #print e,d
	 pass
   elif symbol == 'O':
     k+=1
     for d in ( i, j, diags.get((i,j))):
       try:
         if -1 < d < 10: xcombos.remove(d)
       except ValueError,e:
         #print e,d
	 pass
   elif symbol == 'T':
     k+=1
   elif symbol == '.':
     gameompleted=False
     k+=1
     for d in ( i, j, diags.get((i,j))):
       if  d in xcombos:
         xcombos.remove(d)
	 #print 'removed %d'%d
       if d in ocombos:
         ocombos.remove(d)
	 #print 'removed %d'%d
   #print "After removing %d, %d, %d on k=%d: "%( i, j, diags.get((i,j),-1),k),
   #print xcombos, ocombos
 #print "cases done!!"
 #print xcombos, ocombos
 won = False
 if len(xcombos) > 0 or len(ocombos) ==  1 :
   won = True
   if len(xcombos) > 0: print "Case #%d: X won" %casenum
   #if len(xcombos) > 0: print "Case #%d: X won %d times" %(casenum,len(xcombos))
   if len(ocombos) > 0: print "Case #%d: O won"%casenum
   #if len(ocombos) > 0: print "Case #%d: O won %d times"%(casenum,len(ocombos))
 elif gameompleted==False:
   print "Case #%d: Game has not completed"%casenum
 else: print "Case #%d: Draw"%casenum


 

