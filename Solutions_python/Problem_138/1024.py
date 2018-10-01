#!/usr/bin/python

import sys



def readFile(dir):
	f=open(dir)
	lines=f.readlines()
	T=int(lines[0])
	rt=[]
	for i in range(T):
		naomi=[float(e) for e in lines[2+i*3].split()]
		ken=[float(e) for e in lines[3+i*3].split()]
		rt.append((naomi,ken))
	return rt


def playWar(naomi,ken):
	win=0
	naomi=list(naomi)
	ken=list(ken)
	naomi.sort()
	ken.sort()
	while len(naomi)>0:
		i=0
		while i<len(ken) and ken[i]<naomi[0]:
			i+=1
		if i<len(ken):
			ken.remove(ken[i])
		else:
			win+=1
			ken.remove(ken[0])
		naomi.remove(naomi[0])
	return win
		

def play(naomi,ken):
	naomi.sort()
	ken.sort()
	win=0
	while len(naomi)>0:
		if naomi[0]<ken[0]:
			naomi.remove(naomi[0])
			ken.remove(ken[len(ken)-1])
		else:
			naomi.remove(naomi[0])
			ken.remove(ken[0])
			win+=1
	return win

if __name__=="__main__":
        quizs=readFile(sys.argv[1])
        for i in range(len(quizs)):
		naomi=quizs[i][0]
		ken=quizs[i][1]
		w2=playWar(naomi,ken)
		w1=play(naomi,ken)
                print("Case #%s: %s %s"%(i+1,w1,w2))



