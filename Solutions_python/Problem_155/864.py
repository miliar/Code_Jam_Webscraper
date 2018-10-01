def f(s):
    c = 0
    for i, x in enumerate(int(c) for c in s):
        if x and c < i:
            yield i - c
            c = i
        c += x

def solve(s):
    return sum(f(s))

def parse(fname):
    with open(fname) as f:
        next(f)
        for line in f:
            yield line.split()[1]
            
def display(i, r):
    print "Case #{}: {}".format(i, r)


def solve_file(fname):
    for i, s in enumerate(parse(fname), 1):
        display(i, solve(s))

    
if __name__ == "__main__":
    import sys
    solve_file(sys.argv[1])
