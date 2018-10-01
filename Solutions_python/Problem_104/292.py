import sys


def parse(filename):
    f = open(filename)
    T = int(f.readline())
    for i in range(T):
        line = f.readline().strip()
        terms = line.split()
        N = int(terms[0])
        S = [int(a) for a in terms[1:]]
        yield N, S
    f.close()

def solve(N, S):
    S = sorted(S)
    n = 1
    diff = {}
    diff[S[0]] = 2
    solved = False
    while not solved:
        for i in range(n, N):
            s = S[i]
            if s in diff:
                diff[s] += 1*(10**i)  # add left 
                res = diff[s]
                solved = True
                break
            if -s in diff:
                #print diff[-s]
                diff[-s] += 2*(10**i)  # add right
                res = diff[-s]
                solved = True
                break
            toadd = [] 
            for key in diff:
                toadd.append((key + s,  diff[key] + 2*(10**i)))  # add right
                toadd.append((key - s,  diff[key] + 1*(10**i)))  # add left
            for k, v in toadd:
                diff[k] =  v
            
    res = str(res)
    set_left = []
    set_right = []
    order = []
    for i in range(len(res)-1, -1, -1):
        order.append(res[i])
    for i in range(len(order)):
        if order[i] == '1':
            set_left.append(S[i])
        elif order[i] == '2':
            set_right.append(S[i])
    assert sum(set_left) == sum(set_right)
    #print sum(set_left) == sum(set_right), sum(set_left), sum(set_right)
    assert not set(set_left).intersection(set_right)
    return '\n' + ' '.join([str(a) for a in set_left]) + '\n' + ' '.join([str(b) for b in set_right])
            
            

def main(filename):
    case = 1
    for data in parse(filename):
        res = solve(*data)
        print "Case #%d:" % case, res
        case += 1
    

if __name__ == '__main__':
    #main('a.in')
    main(sys.argv[1])
