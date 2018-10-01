#cookieclicker

import math
import random

fin = open("cookieclicker.in","r")
fout = open("cookieclicker.out","w")

N = int(fin.readline())

'''def gettime(st, r, fc, fr, g, t):
	time1 = (g - st) / r
	time2 = (fc / r) + (g - st) / (r + fr)
	
	if time2 < time1:
		t += fc/r
		r += fr
		return gettime(st, r, fc, fr, g, t)
	else:
		return t + time1
'''
for i in range(N):
	stash = 0
	rate = 2
	farmcost, farmrate, goal = fin.readline().split()
	farmcost = float(farmcost)
	farmrate = float(farmrate)
	goal = float(goal)
	
	#time = gettime(stash, rate, farmcost, farmrate, goal, 0)
	
	time = 0
	while (True):
		time1 = (goal - stash) / rate
		time2 = (farmcost / rate) + (goal - stash) / (rate + farmrate)
	
		if time2 < time1:
			time += farmcost/rate
			rate += farmrate
		else:
			time = time + time1
			break
	
	fout.write("Case #" + str(i + 1) + ": " + "{0:.7f}".format(time) + "\n")
	
fin.close()
