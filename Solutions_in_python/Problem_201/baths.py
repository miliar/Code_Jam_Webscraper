import numpy as np

def read_file():
    '''
    Reads the input file
    '''
    n_data = int(raw_input())  # read a line with a single integer
    N = np.zeros(n_data, dtype=int)
    K = np.zeros(n_data, dtype=int)
    for i in range(n_data):
        line = raw_input()
        line = line.split(" ")
        N[i] = int(line[0])
        K[i] = int(line[1])
        #print "{} {}".format(N[i], K[i])

    return N, K

def getAandB(i):
    return i/2, i/2+i%2


def solve_problem(N, K):
    for i, n, k in zip(range(len(N)), N, K):
        sizes = np.array([n])
        for j in range(k):
            # number of places
            slot = np.max(sizes)
            pos_slot = np.where(sizes==slot)[0][0]
            # max space
            a, b = getAandB(slot)
            b -= 1
            sizes[pos_slot] = b
            sizes = np.insert(sizes, pos_slot+1, a)

        line = "Case #{}: {} {}".format(i+1, max(a,b), min(a,b))
        print(line)

if __name__ == '__main__':
    #filename = sys.argv[1]
    #print filename
    # read
    N, K = read_file()
    #print len(data.keys())
    #print len(flip_sizes)

    # solve
    #print "Solving"
    solve_problem(N, K)

    # write
    #outfile = filename.split('.')[0]
    #outfile += ".out"
    #print outfile
    #write_file(result)
