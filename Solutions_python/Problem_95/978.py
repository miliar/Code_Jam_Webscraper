fin = "small.in"
fout = "small.out"


if __name__ == "__main__":
    f_in = open(fin)
    f_out = open(fout,'w')
    d = {}
    d['\n'] = ''
    d[' '] = ' '
    d['y'] = 'a'
    d['n'] = 'b'
    d['f'] = 'c'
    d['i'] = 'd'
    d['c'] = 'e'
    d['w'] = 'f'
    d['l'] = 'g'
    d['b'] = 'h'
    d['k'] = 'i'
    d['u'] = 'j'
    d['o'] = 'k'
    d['m'] = 'l'
    d['x'] = 'm'
    d['s'] = 'n'
    d['e'] = 'o'
    d['v'] = 'p'
    d['p'] = 'r'
    d['d'] = 's'
    d['r'] = 't'
    d['j'] = 'u'
    d['g'] = 'v'
    d['t'] = 'w'
    d['h'] = 'x'
    d['a'] = 'y'
    d['z'] = 'q'
    d['q'] = 'z'
    test_cases = int(f_in.readline())
    for t in range(0,test_cases):
        s = f_in.readline()
        s2 = ''
        if t >0:
            f_out.write('\n')
        for c in s:
            s2 += d[c]
        s2 = "Case #" + str(t + 1) + ": " + s2
        f_out.write(s2)
    f_in.close()
    f_out.close()
