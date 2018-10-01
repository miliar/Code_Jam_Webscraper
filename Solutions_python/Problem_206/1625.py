import sys

def checkIntersect(pos1,speed1,pos2,speed2,D):
	if pos1 > pos2:
		raise Exception("Not expected!")

	if speed2 >= speed1:
		return D

	deltaS = speed1 - speed2
	deltaP = pos2 - pos1 

	deltaT = deltaP / deltaS

	interPos = deltaT * speed1 + pos1

	return interPos


def solve(N,D,H):

	H.sort(key = lambda x: x[1])

	closer = H[0]


	H.sort(key = lambda x: (D - x[1]) / x[2])

	Htime = [0]*N

	time = 0
	pos = H[0][1]
	speed = H[0][2]

	# check time for closer horse
	time = 0
	pos = closer[1]
	speed = closer[2]
	for h in range(N):
		if H[h][1] >= pos:
			pos2 = checkIntersect(pos,speed,H[h][1],H[h][2],D)
			if pos2 < D:
				time += (pos2-pos) / speed
				pos = pos2
				speed = H[h][2]

	time += (D - pos) / speed
	
	# compute speed
	return D / time

t = int(raw_input())
for i in range(1, t + 1):
  D, N = [int(s) for s in raw_input().split(" ")] 

  H = []
  for h in range(N):
  	values = [int(s) for s in raw_input().split(" ")]
  	H.append((h, float(values[0]), float(values[1])))


  result = solve(N,float(D),H)
  
  print("Case #{}: {}".format(i, result))

