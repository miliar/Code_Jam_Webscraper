import string


def is_blank(x):
    if isinstance(x, list):
        return all(v == "?" for v in x)
    if isinstance(x, str):
        return x == "?"
    print "bad x!", x

def extend_list(lst):
    ret = lst[:]
    if is_blank(lst):
        return lst
    val = [v for v in lst if not is_blank(v)][0]
    for i in range(len(lst)):
        if is_blank(ret[i]):
            ret[i] = val
        else:
            val = ret[i]
    return ret


def solve(cake):
    print cake
    step_one = [extend_list(row) for row in cake]
    print step_one
    done = extend_list(step_one)
    print done
    return "\n".join(["".join(row) for row in done])

def test(inputs, ans):
    b = solve(*inputs)
    if (b != ans):
        print "Failed test! Inputs {} should give answer of {} not {}".format(' '.join(inputs), ans, b)

def main():

    outfile = open('a.out','w')
    T = int(string.strip(raw_input()))

    for k in xrange(1,T+1):
        print k
        R, C = map(int,string.strip(raw_input()).split())
        # parse the line here
        cake = []
        for i in range(R):
            row = list(string.strip(raw_input()))
            cake.append(row)

        answer = solve(cake) # add appropriate arguments
        outfile.write('Case #%d:\n%s\n' % (k,answer))

if __name__ == '__main__':
    main()
