indent = 0
def recur(time, current_horse, horses, routes, start, end):
	global indent
	if start == end:
		return time
	#print(" "*indent + str(start) + " " + str(time))
	indent += 1
	swap = horses[start]
	if swap[0] >= current_horse[0] and swap[1] >= current_horse[1]:
		current_horse = swap
		best = recur(
			time + routes[start] / current_horse[1],
			[current_horse[0] - routes[start], current_horse[1]],
			horses, routes, start+1, end)

	elif swap[0] > current_horse[0] or swap[1] > current_horse[1]:
		if current_horse[0] >= routes[start]:
			noswap = recur(
				time + routes[start] / current_horse[1],
				[current_horse[0] - routes[start], current_horse[1]],
				horses, routes, start+1, end)
		else:
			noswap = float("INF")
		current_horse = swap
		if current_horse[0] >= routes[start]:
			withswap = recur(
				time + routes[start] / current_horse[1],
				[current_horse[0] - routes[start], current_horse[1]],
				horses, routes, start+1, end)
		else:
			withswap = float("INF")
		best = min(noswap, withswap)

	else:
		best = recur(
			time + routes[start] / current_horse[1],
			[current_horse[0] - routes[start], current_horse[1]],
			horses, routes, start+1, end)

	indent -= 1
	return best

def solve(N,Q,horses,routes,pairs):
	routes = [routes[i][i+1] for i in range(len(routes)-1)]
	pair = pairs[0]
	soln = recur(0, [-1, -1], horses, routes, pair[0]-1, pair[1]-1)
	if soln == float("INF"):
		print(horses, routes, pair)
	return soln

T = int(input())
for case in range(T):
	N,Q = map(int, input().split())
	horses = []
	for row in range(N):
		horses.append(list(map(int, input().split())))
	routes = []
	for row in range(N):
		routes.append(list(map(int, input().split())))
	pairs = []
	for row in range(Q):
		pairs.append(list(map(int, input().split())))
	print("Case #{}: {}".format(case+1, solve(N,Q,horses,routes,pairs)))