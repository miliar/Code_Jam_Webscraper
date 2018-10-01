import sys
import numpy as np

def last_tidy(n):
    n = np.array(list(n), np.int32)

    max_d = 0
    last_i = 0
    decr = False

    for i in range(len(n)):
        if n[i]>max_d:
            last_i = i
            max_d = n[i]
        elif n[i]<max_d:
            decr = True
            break

    if decr:
        n[last_i] -= 1
        n[last_i+1:] = 9
    if n[0] == 0:
        n = n[1:]

    return "".join(map(str,n))



if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    t = int(f.readline())
    for i in xrange(t):
    	n = f.readline().strip()
        
    	last = last_tidy(n)

    	print("CASE #{0}: {1}".format(i+1, last))
