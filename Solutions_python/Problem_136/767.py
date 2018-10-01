#!/usr/bin/env python

fo = open("B-large.in","r");
import sys
sys.stdout = open("B-large.out","w");
lines = fo.readlines();
#print lines[0]
k=0
t =0
for i in lines:
	k+=1
	
		
	#i = i.strip('\n')
	this = i.split()
	if k ==1:
		t = [int(x) for x in this]
		t = t[0]
		#print t
	else:
	
		this_f = [float(x) for x in this]
		j=0
		f =0
		for x in this_f:
			j+=1
			if j == 2:
				f = x
		c = this_f[0]
		'''y = this_f[1:2]
		y = str(y)
		y = y.strip(']')
		y = y.strip('[')'''
		#float(y)
		#c = float(y)
		x = this_f[-1]
		#print type(y)
		#print x,y,z
		
		total=0.0;tf=0.0;tft=0.0;tt=0.0;
		rate = 2.0;
		tfarm = 0.0;
		
		tt = x/rate;
		tf = c/rate;
		tft = x/(rate+f);
		tfarm = tf + tft;
		
		while tt > tfarm:
		
			total+=tf
			rate+=f
			tt = x/rate
			tf = c/rate
			tft = x/(rate+f)
			tfarm = tf + tft
			if tt <= tfarm:
				break
			
		print 'Case #%d: %.7f' %(k-1,tt+total)	
			

fo.close();
