def read_data(f):
	s = file(f).read().splitlines()[1:]
	s = [map(int,x.split(" ")) for x in s[1::2]]
	return s

def solve(l):
    if reduce(lambda x,y: x^y,l) != 0:
        return "NO"
    else:
        return sum(l) - min(l)

    
def solve_all(inp,out):
    data = read_data(inp)
    res = map(solve,data)
    f = file(out,"w")
    for i,r in enumerate(res):
        f.write("Case #%d: "%(i+1,) + str(r) + "\n")
