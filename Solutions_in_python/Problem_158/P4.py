import sys

def calculate(lineSplitted):
	X=int(lineSplitted[0])
	R=int(lineSplitted[1])
	C=int(lineSplitted[2])
	if X==3 and C==3 and R==1:
		return False
	if X==3 and C==1 and R==3:
		return False
	if (R*C)%X != 0:
		return False
	if X==1:
		return True
	elif X==2:
		return R*C%2==0
	elif X==3:
		if R<3 and C<3:
			return False
		else:
			return min(R, C)>1
	elif X==4:
		if R<4 and C<4: return False
		else:
			noCuatro=min(R, C)
			return noCuatro>=3
	else:
		print "X ES MAYOR A 4!!!"		

if __name__ == "__main__":
    with open(sys.argv[1], "r") as file:
    	file.readline()
    	case=1
    	for line in file.readlines():
    		if not line.strip(): continue
    		result = calculate(line.strip().split(" "))
    		if result:
    			name="GABRIEL"
    		else:
    			name="RICHARD"
    		print "Case #"+str(case)+": "+name
    		case+=1