import sys
with open(sys.argv[1]) as f:
    T = int(f.readline().strip())
    for i in range(T):
        line = f.readline().strip().split()
        C = int(line.pop(0))
        combines_list = line[:C]
        line = line[C:]
        D = int(line.pop(0))
        opposers = line[:D]
        invoked = line[-1]
        result = ""
        combines = {}
        for c in combines_list:
            combines[c[0:2]] = c[2]
            combines[c[1] + c[0]] = c[2]
        for c in invoked:
            result += c
            if result[-2:] in combines:
                result = result[:-2] + combines[result[-2:]]
            for a, b in opposers:
                if a in result and b in result:
                    result = ''
        print "Case #%d:"%(i+1), str(list(result)).replace("'", "")
