def gira(s):
    result = []
    for c in s:
        if c == '+':
            result.append('-')
        else:  # c == '-'
            result.append('+')
    return ''.join(result)

def ngira(s, n):
    """ gira gli n pancakes a dx e sx della stringa s 
    return s, n_mosse
    """
    if n >= len(s):
        # assert n == len(s)
        return gira(s), 1
        # se n > len(s): impossible se len != 0, risolto se len==0 return mosse 0
    n = min(n, len(s) - n)
    return gira(s[:n]) + s[n : len(s)-n] + gira(s[len(s)-n : ]), 2
# print(ngira('----+',3)); input()


with open('A-large.in', 'r') as f_in, open('out.txt', 'w') as f_out:
    t = int(f_in.readline())
    for i, line in enumerate(f_in):
        s, k = line.split(" ")
        k = int(k)
        print("Case #{}: {} {}".format(i + 1, s, k))

        n_mosse = 0
        s = s.strip('+')
        while len(s) >= k:
            s, m = ngira(s, k)
            n_mosse += m
            s = s.strip('+')
            print("         {} {}".format(s, k))

        f_out.write("Case #{}: ".format(i + 1))
        if len(s) == 0:
            f_out.write("{}\n".format(n_mosse))
        else:
            f_out.write("IMPOSSIBLE\n")
