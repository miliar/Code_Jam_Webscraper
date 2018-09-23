import sys
f = open('out17a.out','w')
T = int( sys.stdin.readline().strip())
case=0

def MinOnS( _S):
	return _S.count("-")
def Flipper( _S,_K):
	result = 0
	comps = 0
	lenS = len(_S)
	target = list("+"*lenS)
	while  _S != target :
		ix =0
		hSide = False
		while ix <=  (lenS-_K) :
			if _S[ix] == "-":
				# print(_S)
				# print(_S[ix:ix+_K])
				_S[ix:ix+_K] = [("+" if i == "-" else "-") for i in  _S[ix:ix+_K] ]
				comps +=1
			ix +=1
		if  MinOnS(_S) < _K and MinOnS(_S) > 0:
			return -1
	return comps

def FlipperTEST( _S,_K):
	result = 0
	comps = 0
	lenS = len(_S)
	target = list("+"*lenS)
	while  _S != target :
		ix =lenS
		hSide = False
		while ix > 0 :
			if _S[ix-1] == "-":
				_S[ix-_K:ix] = [("+" if i == "-" else "-") for i in  _S[ix-_K:ix] ]
				comps +=1
			ix -=1
		if  MinOnS(_S) < _K and MinOnS(_S) > 0:
			return -1
		break
	return comps

while( T>0 ):
	T-=1
	case+=1
	flips = 4
	readed = sys.stdin.readline().strip()
	S, K = map(list,readed.split() ) 
	outS, K = map(list,readed.split() ) 
	outSTEST, K = map(list,readed.split() ) 
	flips = Flipper(outS,int(''.join(K)))
	flipsTEST = FlipperTEST(outSTEST,int(''.join(K)))
	if flips != flipsTEST:
		print("WARNING caso",case," s: ",S, flips, "  -  ",flipsTEST )
	resp = flips if flips >=0 else "IMPOSSIBLE"
	key = "-"*5

	# print    ("Case #"+str(case)+": "+str(resp))
	f.write ("Case #"+str(case)+": "+str(resp)+"\n")
f.close();
