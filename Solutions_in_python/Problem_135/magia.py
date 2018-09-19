import sys

def resuelve(tc,r1,r2):
	res = []
	for e1 in r1:
		try:
			#print e1
			r2.index(e1)
			res.append(e1)
			#print str(tc) + " => " + str(e1)
		except:
			pass
	#print str(tc) + "--" + str(r1) + str(r2) + " => " + str(res)
	
	if len(res) == 1:
		print "Case #"+str(tc)+": "+res[0]
	elif len(res) > 0:
		print "Case #"+str(tc)+": Bad magician!"
	else:
		print "Case #"+str(tc)+": Volunteer cheated!"		
	
def read_board():
	p = int(sys.stdin.readline().rstrip())
	g = []
	for j in range(4):		
		#print j
		line = sys.stdin.readline().rstrip()
		g.append(line.split(' '))
	#print g
	return (p,g)


	
#--------------------------------------------------	

T = int(sys.stdin.readline().rstrip())
for tc in range(T):
	(pos1,g1) = read_board()
	(pos2,g2) = read_board()
	resuelve(tc+1,g1[pos1-1],g2[pos2-1])
	
