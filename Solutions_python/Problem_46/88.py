import doctest

def swap(l, i, j):
    if j <= i:
        raise "Index Error %d %d" % (i, j)
    t = l.pop(j)
    l.insert(i, t)
    return j - i

def count1(s):
    l = range(len(s))
    l.reverse()
    for i in l:
        if s[i] == '1':
            return i
    return 0

def check(l_x):
    for i, x in enumerate(l_x):
        if x > i:
            return i
    return - 1

def solve(question):
    if question == ['1']:
        return repr(0)

    print question
    ans = 0
    l_x = [count1(_) for _ in question]
    ind = check(l_x)
    while ind >= 0:
        i_targ = l_x.index([ _ for _ in l_x[ind:] if _ <= ind][0], ind)
        #print ind, i_targ, l_x
        ans += swap(l_x, ind, i_targ)
        ind = check(l_x)

    return repr(ans)



if __name__ == '__main__':
    doctest.testmod()
    #str_in = 'A-sample.in'
    str_in = 'A-large.in'
    #str_in = 'A-small-attempt1.in'
    f_in = open(str_in)
    f_out = open(str_in.rstrip('.in') + '.out', 'w')

    N = int(f_in.next())
    for num_q in range(N):
        n = int(f_in.next().strip())
        question = [f_in.next().strip() for _ in range(n)]
        output = 'Case #' + str(num_q + 1) + ': ' + solve(question) + '\n'
        f_out.write(output); print output,

    f_in.close(); f_out.close()
