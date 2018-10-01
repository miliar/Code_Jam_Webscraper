"""

"""

#import psyco; psyco.full()
#import pyximport; pyximport.install()

dynamic = True
def solve(case, case_nb=None):
    X, S, R, TR, N = case[0]
    Ws = case[1:]
    
    # I must add non moving walkways
    Ws.sort()
    stop = False
    while not stop:
        stop = True
        p = 0
        for i, (a, b, w) in enumerate(Ws):
            if p < a:
                Ws.insert(i, [p, a, 0])
                stop = False
                break
            else:
                p = b
            if i == len(Ws) - 1 and b < X:
                Ws.append([b, X, 0])
    
    Ws.sort(cmp=lambda x, y: cmp(x[2], y[2]))
    
    T = 0.0
    for a, b, w in Ws:
        dr = TR * (R+w)
        if dr > b - a:
            t = 1.0 * (b-a) / (R+w)
            T += t
            TR -= t
        else:
            T += TR + 1.0 * (b-a-dr) / (S+w)
            TR = 0    
    return T
    
    
def parse_input(dynamic=False):
    from sys import argv, stdin
    def try_int(s):
        try:
            return int(s)
        except:
            return s
    if len(argv) > 1:
        f = open(argv[1])
    else:
        f = stdin
    lines = f.read().split('\n')[0:-1]
    nb_inputs = int(lines[0])
    lines = lines[1:]
    # Number of lines per case
    if not dynamic:
        p = len(lines) / nb_inputs
    line_nb = 0
    for i in range(nb_inputs):
        if dynamic:
            line = map(try_int, lines[line_nb].split(' '))
            p = line[-1]
            if len(line) > 1:
                p += 1
            else:
                # I do not take a line that contain only the number of lines
                line_nb += 1
        case_lines = lines[line_nb:line_nb+p]
        case = [map(try_int, line.split(' ')) for line in case_lines]
        if not dynamic and p == 1:
            case = case[0]
        line_nb += p
        yield case

if __name__ == '__main__':
    for i, case in enumerate(parse_input(dynamic=dynamic)):
        case_nb = 'Case #%i: ' % (i+1)
        result = solve(case, i+1)
        if type(result) is list:
            result = ' '.join(map(str, result))
        elif type(result) is float:
            result = '%.06f' % result
        else:
            result = str(result)
        print case_nb + result
