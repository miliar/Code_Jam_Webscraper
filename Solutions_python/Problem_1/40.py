import sys
def readline():
    return sys.stdin.readline()

def main():
    ncase = int(readline())
    for case in range(ncase):
        neng = int(readline())
        eng = []
        engmap = {}

        for i in range(neng):
            name = readline().strip()
            engmap[name] = len(eng)
            eng.append(name)

        nquery = int(readline())

        sofar = [0] * neng
        for i in xrange(nquery):
            query = readline().strip()
            if query in engmap:
                no = engmap[query]
                
                sofar[no] = min(sofar[:no] + sofar[no+1:]) + 1
            else:
                # ok
                pass
        #print sofar
        print 'Case #%d: %d' % (case+1, min(sofar))
            




    pass

main()
