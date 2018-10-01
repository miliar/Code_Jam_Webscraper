#!/usr/bin/python
import sys

ifile=sys.argv[1]
lines=open(ifile).read().split("\n")
tc=lines[0]
lines=lines[1:]
case=1


def doWar(nb,kb):
	points=0
	for n in nb:
		if max(kb) < n:
			points+=1
			kb.remove(min(kb))
		else:
			betters=[]
			for k in kb:
				if k > n:
					betters.append(k)
			kb.remove(min(betters))
	return points


def doDwar(nb,kb):
	points=0
	while nb != []:
		maxK=max(kb)
		maxN=max(nb)
		if maxN < maxK:
			nchoice=min(nb)
#			print("Naomi used: "+str(nchoice))
			nb.remove(nchoice)
#			print("Ken used: "+str(maxK))
			kb.remove(maxK)
		else:
			nchoice=maxN
			nlie=maxK-0.0000001
			points+=1
			betters=[]
			for k in kb:
				if k > nlie:
					betters.append(k)
			if betters != []:
				kb.remove(min(betters))
#				print("Ken used: "+str(min(betters)))
			else:
#				print("Ken used: "+str(min(kb)))
				kb.remove(min(kb))
			nb.remove(nchoice)
#			print("Naomi used: "+str(nchoice))
	return points	


def doDwar2(nb,kb):
	points=0
	for k in kb:
	 	if nb == []:
			continue
		if max(nb) > k:
			points+=1
			nb.remove(min(nb))
		else:
			betters=[]
			for n in nb:
				if n > k:
					betters.append(k)
			if not betters == []:		
				nb.remove(max(betters))
	return points




while lines != [] and lines != ['']:
	nblocks=[float(i) for i in lines[1].split()]
	kblocks=[float(i) for i in lines[2].split()]
	nblocks2=list(nblocks)
	kblocks2=list(kblocks)
#	print("nblocks:" +str(nblocks))
#	print("kblocks:" +str(kblocks))
	lines=lines[3:]
	war=doWar(nblocks,kblocks)
	dwar=doDwar(nblocks2,kblocks2)
	output=str(dwar)+" "+str(war)
	print("Case #"+str(case)+": "+output)
	case+=1
	
	
