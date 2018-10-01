#!/usr/bin/env python
import sys, re, psyco

def read(filename):
	cases = []
	for i,l in enumerate(file(filename)):
		if i == 0: continue
		cases.append(l.strip())

	return cases

def calc(x):
	#p = 'welcome to code jam'
	z = 0
	l=len(x)
	for a in range(0,l-18):
		if x[a]=='w': 
			for b in range(a+1,l-17):
				if x[b]=='e': 
					for c in range(b+1,l-16):
						if x[c]=='l': 
							for d in range(c+1,l-15):
								if x[d]=='c': 
									for e in range(d+1,l-14):
										if x[e]=='o': 
											for f in range(e+1,l-13):
												if x[f]=='m': 
													for g in range(f+1,l-12):
														if x[g]=='e':
															for h in range(g+1,l-11):
																if x[h]==' ': 
																	for i in range(h+1,l-10):
																		if x[i]=='t': 
																			for j in range(i+1,l-9):
																				if x[j]=='o': 
																					for k in range(j+1,l-8):
																						if x[k]==' ': 
																							for t in range(k+1,l-7):
																								if x[t]=='c': 
																									for m in range(t+1,l-6):
																										if x[m]=='o': 
																											for n in range(m+1,l-5):
																												if x[n]=='d':
																													for o in range(n+1,l-4):
																														if x[o]=='e': 
																															for p in range(o+1,l-3):
																																if x[p]==' ': 
																																	for q in range(p+1,l-2):
																																		if x[q]=='j': 
																																			for r in range(q+1,l-1):
																																				if x[r]=='a': 
																																					for s in range(r+1,l):
																																						if x[s]=='m': z+=1
																																							

	return z

def main(argv):
	psyco.full()
	p = 'welcome to code jam'
	cases = read(argv[1])
	#print cases
	for number,c in enumerate(cases):
		res = ""
		for k in c:
			if k in p: res += k
		#print res
		n=calc(res)
		print "Case #%d: %04d" % (number+1, n%10000)

if __name__ == "__main__":
	main(sys.argv)
