#!/usr/bin/env python

import sys

def RPI(teams):
	WP = []
	WPc = []
	OWP = []
	OWPc = []
	OOWP = []
	OOWPc = []

	for team in teams:
		s = 0.0
		cnt = 0
		for t in team:
			if t >= 0:
				s += float(t)
				cnt += 1
		if cnt > 0:
			WP.append(float(s) / cnt)
		else:
			WP.append(0.0)
		WPc.append(cnt)

	for team in teams:
		s = 0.0
		cnt = 0
		for i, t in enumerate(team):
			if t >= 0:
				if t == 0:
					if WPc[i] - 1 > 0:
						s += float(WP[i] * WPc[i] - 1.0) / float(WPc[i] - 1.0)
						cnt += 1
					#else:
						#s += float(WP[i] * WPc[i]) / float(WPc[i] - 1.0)
				else:
					s += float(WP[i] * WPc[i]) / float(WPc[i] - 1.0)
					cnt += 1
		if cnt > 0:
			OWP.append(float(s) / cnt)
		else:
			OWP.append(0.0)
		OWPc.append(cnt)
	
	for team in teams:
		s = 0.0
		cnt = 0
		for i, t in enumerate(team):
			if t >= 0:
				s += float(OWP[i])
				cnt += 1
		if cnt > 0:
			OOWP.append(float(s) / cnt)
		else:
			OOWP.append(0.0)
		OOWPc.append(cnt)

	RPI = []
	for i in range(len(teams)):
		#print WP[i], OWP[i], OOWP[i]
		RPI.append(0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i])

	return RPI
		

def main():
	#f = file("test.in")
	#f = file("A-small-0.in")
	f = file("A-large.in")
	T = int(f.readline())
	for i in range(T):
		N = int(f.readline().strip())
		data = []
		for j in range(N):
			l = f.readline().strip()
			d = []
			for x in l:
				if x == '.': s = -1
				else: s = int(x)
				d.append(s)
			data.append(d)
		#print data
		ans = RPI(data)
		print "Case #%s:" % (i + 1)
		for a in ans:
			print a
		

if __name__ == "__main__": main()
