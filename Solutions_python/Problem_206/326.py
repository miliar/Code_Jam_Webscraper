import string

def solve(D, N, horses):
    return min(D/((D-K_i)/S_i) for (K_i, S_i) in horses)

def test(inputs, ans):
    b = solve(*inputs)
    if (b != ans):
        print "Failed test! Inputs {} should give answer of {} not {}".format(' '.join(inputs), ans, b)

def main():

    outfile = open('a.out','w')
    T = int(string.strip(raw_input()))

    for k in xrange(1,T+1):
        print k
        D, N = map(int,string.strip(raw_input()).split())
        # parse the line here
        horses = []
        for i in range(N):
            K_i, S_i = map(float, string.strip(raw_input()).split())
            horses.append((K_i, S_i))

        answer = solve(D, N, horses) # add appropriate arguments
        outfile.write('Case #%d: %s\n' % (k,answer))

if __name__ == '__main__':
    main()
