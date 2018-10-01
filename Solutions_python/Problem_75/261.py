from codejam import *

@main
def Magicka():
    T = read_int()
    for case in xrange(T):
        tmp = read_strs()
        C = int(tmp[0])
        combining = {}
        for cc in tmp[1:C+1]:
            combining[cc[:2]] = cc[2]
            combining[cc[1]+cc[0]] = cc[2]
        D = int(tmp[C+1])
        opposing = {}
        for dd in tmp[C+2:C+2+D]:
            opposing[dd[0]] = dd[1]
            opposing[dd[1]] = dd[0]
        elements = tmp[-1]
        result = ''
        debug(combining)
        debug(opposing)
        for e in elements:
            if len(result) == 0:
                result = e
            elif result[-1]+e in combining:
                result = result[:-1] + combining[result[-1]+e]
            elif e in opposing and opposing[e] in result:
                result = ''
            else:
                result += e
            debug((e, result))
        printcase(case, '[' + ', '.join(result) + ']')
