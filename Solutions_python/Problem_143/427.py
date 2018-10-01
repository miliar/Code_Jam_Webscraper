f_in = open("B-small-attempt0.in.", 'r')
f_out = open("B-small.out", 'w')


def get_int():
    return int(f_in.readline().rstrip())

def get_triple():
    temp = f_in.readline().rstrip().split()
    return [int(x) for x in temp]

T = get_int()

for i in range(1, T + 1):

    # First number less than A, second less than B
    # She buys all less than K
    # Want number of ways A, B makes her win
    # Ie number of combinations of A, B where A & B < K
    A, B, K = get_triple()

    combs = 0

    for a in range(0, A):
        for b in range (0, B):
            if a & b < K:
                combs += 1
    
    print "Case #{1}: {0}".format(combs, i)
    f_out.write("Case #{1}: {0}\n".format(combs, i))


f_in.close()
f_out.close()
