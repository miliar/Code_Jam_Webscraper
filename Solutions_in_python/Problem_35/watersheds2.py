from jaminput import *

f=open('C:\B-large.in','r')
fo=open('C:\B-large.out','w')

ncases=getint(f)
for i in range(ncases):
	(h,w)=getarr(f)
	inmap=[]
	for j in range(h):
		inmap.append(getarr(f))
	outmap=[]
	for j in range(h):
		outmap.append(['0']*w)
	
	curcat=97
	for j in range(h):
		for k in range(w):
			if outmap[j][k]!='0':
				continue
			pts=[]
			next=[j,k]
			ch='0'
			while next!=[-1,-1]:
				pts.append(next)
				cur=next
				(x,y)=cur
				val=inmap[x][y]
				next=[-1,-1]
				if x!=0:
					if inmap[x-1][y]<val:
						if outmap[x-1][y]!='0':
							ch=outmap[x-1][y]
							val=inmap[x-1][y]
						else:
							next=[x-1,y]
							val=inmap[x-1][y]
				if y!=0:
					if inmap[x][y-1]<val:
						if outmap[x][y-1]!='0':
							ch=outmap[x][y-1]
							val=inmap[x][y-1]
						else:
							next=[x,y-1]
							val=inmap[x][y-1]
							ch='0'
				if y!=w-1:
					if inmap[x][y+1]<val:
						if outmap[x][y+1]!='0':
							ch=outmap[x][y+1]
							val=inmap[x][y+1]
						else:
							next=[x,y+1]
							val=inmap[x][y+1]
							ch='0'
				if x!=h-1:
					if inmap[x+1][y]<val:
						if outmap[x+1][y]!='0':
							ch=outmap[x+1][y]
							val=inmap[x+1][y]
						else:
							next=[x+1,y]
							val=inmap[x+1][y]
							ch='0'
				if ch!='0': break
			if ch=='0':
				ch=chr(curcat)
				curcat+=1
			while len(pts)>0:
				(x,y)=pts.pop()
				outmap[x][y]=ch
			
	
	
	fo.write('Case #%d:\n' % (i+1))
	for j in range(h):
		for k in range(w):
			fo.write(outmap[j][k]+' ')
		fo.write('\n')
f.close()
fo.close()
