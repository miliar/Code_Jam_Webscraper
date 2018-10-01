import sys

def makecombs(c):
	cmb={}
	for i in range(len(c)):
		l = c[i]
		cmb[l[:-1]]=l[2]
		cmb[l[1]+l[0]]=l[2]
	return cmb	

def makeops(c):
	op = {}
	for i in range(len(c)):
		l = c[i]
		op[l[0]] = l[1]
		op[l[1]] = l[0]
	return op
			
			
def do(fila):
	#print "fila ",fila
	cmb = {}
	op = {}
	
	combinations = fila[1:int(fila[0])+1]
	cmb = makecombs(combinations)
	#print "combs: ",cmb
	del fila[0:int(fila[0])+1]
	
	opposite = fila[1:int(fila[0])+1]
	op = makeops(opposite)
	#print "ops:",op
	del fila[0:int(fila[0])+1]
	
	letters = int(fila[0])
	del fila[0]
	
	fila =  fila[0]
	invoke = ""
	listen = []
	for i in range(letters):
		next=fila[i]
		#print "invoke",invoke
		#print "next:",next
		if(len(invoke)>0):
			last = str(invoke[-1])+next
			#print "last 2:",last
			if(last in cmb):
				invoke = invoke[:-1]
				invoke += cmb[last]
				#print "-> ",invoke
				continue
			else:
				invoke+=next
		else:
			invoke+=next
		if next in op and op[next] in invoke:
			#print "clearing"
			invoke = ""
			listen = []
				
		
	#print "done: ",invoke
	return str(list(invoke)).replace('\'','')
#print sys.argv
if len(sys.argv)<2:
    #print "Faltan parametros"
    exit()


f = open(sys.argv[1],'r')
fileout = sys.argv[1][:-2]+"out"

o = open(fileout,'w')
ncasos = int(f.readline())

for i in range(1,ncasos+1):
	
	elems=f.readline().rstrip()
	
	resultado = do(elems.split(' '))
	
	o.write("Case #%d: "%i)
	o.write(str(resultado))
	o.write('\n')

f.close()
o.close()
raw_input("done")

