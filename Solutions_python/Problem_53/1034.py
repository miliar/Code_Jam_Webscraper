import math
# only toggle if have power


def dosnap(chain):
	l = len(chain)
	# p is the last snapper that has power
	p=-1
	while(p < l-1 and chain[p+1] == 1):
		p += 1
		
	#toggle everyone that has power plus the one after the last
	for i in range(p+1,-1,-1):
		if( i < l ):
			chain[i] = int(math.fabs(chain[i]-1))

	return p+1
	
def snaprun(chain,k):
	p = 0
	for i in range(k):
		p = dosnap(chain)
	return p
	
FILE = open('A-small-attempt0.in')
contents = FILE.readlines()
FILE.close()


FILE = open('1_output.txt','w')

runs = int(contents[0])
for j in range(runs):
	n,k = contents[j+1].split()
	chain = [0]*int(n)
	snaprun(chain,int(k))
	out = "Case #" + str(j+1) +": "
	p = 0
	while(p < len(chain) and chain[p] == 1):
		p += 1
	if( chain[-1] == 1 and p == len(chain) ):
		FILE.write( out + 'ON\n' )
	else:
		FILE.write( out + 'OFF\n' )
FILE.close()




