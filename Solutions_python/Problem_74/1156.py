from math import *
import sys

f=open(sys.argv[1],'r')
lines=f.readlines()

ntot=int(lines[0])
lines=lines[1:]
dne=0
for linest in lines:
	dne+=1
	line=linest.split(' ')
	ncases=int(line[0])
	line=line[1:]

	nlen=len(line)

	ind=0
	pos=[1,1]
	targ=[0,0]
	if 'O' in line[ind:]:
		targ[0]=int(line[line[ind:].index('O')+1])
	else:
		targ[0]=pos[0]
	if 'B' in line[ind:]:
		targ[1]=int(line[line[ind:].index('B')+1])
	else:
		targ[1]=pos[1]
	
	if line[ind]=='O':
		cur=0
	else:
		cur=1

	ncur=1-cur
	t=0

	done=0
	while done<ncases:
#		print "ncases:" ,ncases
		ind+=2
		dt=abs(pos[cur]-targ[cur])+1
		pos[cur]=targ[cur]


		diff=targ[ncur]-pos[ncur]
		if diff>0:
			pos[ncur]+=min(dt,diff)
		elif diff<0:
			pos[ncur]-=min(dt,-diff)
		else:
			zx=1

		done+=1

		t+=dt
		if done==ncases:
			break

		if 'O' in line[ind:]:
			targ[0]=int(line[line[ind:].index('O')+ind+1])
#			print "o at: ",targ[0]
		else:
			targ[0]=pos[0]
		if 'B' in line[ind:]:
			targ[1]=int(line[line[ind:].index('B')+ind+1])
#			print "b at: ",targ[1]
		else:
			targ[1]=pos[1]

		if line[ind]=='O':
			cur=0
		else:
			cur=1

		ncur=1-cur
		
#		if dne==4:
#			print "t: ",t
#			print "cur: ",cur
#			print "done: ",done
#			print "pos: ",pos
#			print "targ: ",targ
#	

	print "Case #%d: "%dne,t
