import math

def solve(N,K):


	if K > (N/1.5 +2):
		return "0 0"

	spaces = [N]


	for i in range(K-1):
		m = max(spaces)

		spaces.remove(max(spaces))

		if m%2 == 0:
			x =  int(math.floor(m/2)) 
			y = x -1
		else:
			x =  int(math.floor(m/2)) 
			y = x

		spaces.append(x)
		spaces.append(y) 

	if max(spaces)%2 == 0:
		x =  int(math.floor(max(spaces)/2)) 
		y = x -1

	else:
		x =  int(math.floor(max(spaces)/2)) 
		y = x

	return str(x) + " " +str(y)


def main():

	T = int(raw_input())
	responses = list()
	for t in xrange(T):

		N, K = map(int, raw_input().split())

		responses.append(solve(N,K))

	i = 0
	for r in responses:
		i+=1
		print "Case #"+str(i)+": "+str(r)

if __name__ == "__main__":
	main()