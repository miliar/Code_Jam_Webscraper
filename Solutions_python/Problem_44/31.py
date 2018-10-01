#!/usr/bin/python
import math
import os

t=input()
for q in range(t):
	n=input()
	x=0
	cx = 0
	cy = 0
	cz = 0
	cvx = 0
	cvy = 0
	cvz = 0

	time = 0.0
	for i in range(n):
		s=raw_input()
		#print "s",s
		[x,y,z,vx,vy,vz]=s.split(' ')
		#print x,y,z,vx,vy,vz
		cx = cx + 1.0 * (float(x)/n)
		cy = cy + 1.0 * (float(y)/n)
		cz = cz + 1.0 * (float(z)/n)
		cvx = cvx + 1.0 * (float(vx)/n)
		cvy = cvy + 1.0 * (float(vy)/n)
		cvz = cvz + 1.0 * (float(vz)/n)
#	print "WWW",cx,cy,cz,cvx,cvy,cvz
	if((cvx*cvx+cvy*cvy+cvz*cvz) < 10e-9):
		time = 0.0
	else:
		time = -(cx*cvx+cy*cvy+cz*cvz)/(cvx*cvx+cvz*cvz+cvy*cvy)
	if(time < 0):
		time = 0.0
	fx = cx + cvx*time
	fy = cy + cvy*time
	fz = cz + cvz*time
	print "Case #"+str((q+1))+": %.8f" % math.sqrt(fx*fx+fy*fy+fz*fz),"%.8f"%time
			
