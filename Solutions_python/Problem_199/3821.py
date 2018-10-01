import sys

def read():
    return sys.stdin.readline().strip().split()

def doit():
    nr_cases = int(read()[0])

    for q in range(nr_cases):
        flips = 0
        state, w = read()
        state = map(lambda c: c=="+", state)
        w=int(w)
        for i in range(len(state) - w + 1):
            if not state[i]:
                for x in range(w):
                    state[i+x] = not state[i+x]
                flips+=1
        print "Case #%s:" % (q+1),
        if all(state):
            print flips
        else:
            print "IMPOSSIBLE"

if __name__ == '__main__':
    doit()
