from numpy import *

def create_bit_vector(B, T, X, V):
    return ((float(B) - array(X)) / array(V)) <= T
##    return [float(B - i) / V <= T for i in X]

def do_q(K, B, T, X, V):
    bits = create_bit_vector(B, T, X, V)
    if K == 0:
        return 0
    elif sum(bits) < K:
        return "IMPOSSIBLE"
    else:
        rev = bits[::-1]
##        return sum([sum(~rev[:i]) for i in nonzero(rev)[0][:K]])
        cs = cumsum(~rev)
        return sum(take(cs, nonzero(rev)[0][:K]))


def parse_input_and_output(infile, outfile):
    lines = open(infile).readlines()
    C = int(lines[0])
    cnt = 1
    R = []
    for i in range(C):
        try:
            t = lines[cnt].split()
            N = int(t[0])
            
            K = int(t[1])
            B = int(t[2])
            T = int(t[3])

            X = map(int, lines[cnt + 1].split())
            V = map(int, lines[cnt + 2].split())

            res = do_q(K, B, T, X, V)
            
            R.append("Case #%d: %s" % (i + 1, res))
            
            cnt += 3
        except (IndexError, ValueError):
            pass
    open(outfile, "w").write("\n".join(R))
