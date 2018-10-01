from pprint import pprint

filein=open("B-large.in")
fichier = open("sortie.txt", "w")

nbCases=int(filein.readline())

def shift(l):
        item = l[0]
        del l[:1]
        return item
		
for i in range(0, nbCases):
	ligne=filein.readline()
	ligne=ligne.rstrip()
	tok=ligne.split(" ")
	#pprint(tok)
	tabConv={}
	tabOpp={}
	
	max=int(shift(tok))
	for j in range(0, max):
		elt=shift(tok)
		tabConv[elt[0:2]]=elt[2]
		tabConv[elt[1]+elt[0]]=elt[2]
		
	max=int(shift(tok))
	for j in range(0, max):
		elt=shift(tok)
		#pprint(elt)
		tabOpp[elt[0:2]]=0	
		tabOpp[elt[1]+elt[0]]=0
		
	#print "tabConv"
	#pprint(tabConv)
	#print "tabOpp"
	#pprint(tabOpp)	
	
	flow=shift(tok)
	flow=shift(tok)
	#print flow
	#pprint(flow) 

	#tabFlow=[]
	#for(k=0; k<len(flow); k++):
	#	tabFlow.append(flow[0])
	
	m=1
	while(m<len(flow)):
		#pprint(flow) 
		#for(m=1; m<len(flow); m++):
		
		if(flow[m-1:m+1] in tabConv):
			flow=flow[:m-1]+tabConv[flow[m-1:m+1]]+flow[m+1:]
			m=m-1
		
		m=m+1
		for b in range(0,m-1):
			if (flow[b]+flow[m-1]) in tabOpp:
				flow=flow[m:]
				m=0
				break;
		#if(flow[m-1:m+1] in tabOpp):
		#	flow=flow[m+1:]
		#	m=0
		#else:
			
	
	tab=[]
	for h in range(0, len(flow)):
		tab.append(flow[h])
		#print flow[i]
		#if i!=(len(flow)-1):
	fichier.write( "Case #%s"%(i+1)+": "+ "["+", ".join(tab)+"]\n")
	#pprint(flow)
		
		
	
	
fichier.close()
		
		
		