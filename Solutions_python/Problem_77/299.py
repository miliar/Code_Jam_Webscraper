def get_cycles(p):
	p = [x-1 for x in p]
	visited = [0] * len(p)
	cycles = []
	while 0 in visited:
		start = visited.index(0)
		visited[start] = 1
		cycle_l = 1
		x = start
		while(p[x] != start):
			cycle_l += 1
			visited[p[x]] = 1
			x = p[x]
		cycles.append(cycle_l)
	return cycles

def read_data(f):
    s = file(f).read().splitlines()[1:]
    s = [map(int,x.split(" ")) for x in s[1::2]]
    return s

def solve(l):
    return sum(filter(lambda x:x!=1,get_cycles(l)))

def solve_all(inp,out):
    data = read_data(inp)
    res = map(solve, data)
    f = file(out,"w")
    for i,r in enumerate(res):
        f.write("Case #%d: %6f\n"%(i+1,r))

