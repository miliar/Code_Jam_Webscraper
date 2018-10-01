"""
Chuletas

P = map(int,P.split(" "))
P = [int (s) for s in raw_input().split(" ")] # lista de precios
import pdb; pdb.set_trace()

"""
import sys


def log(s):
    print >> sys.stderr, s


def leelinea():
    global filein
    return filein.readline().rstrip('\n')

if __name__ == "__main__":

    if len(sys.argv) == 1:
        filein = sys.stdin
        fileout = sys.stdout
        log("File in standard")
    else:
        filein = open(sys.argv[1] + '.in', 'r')
        fileout = open(sys.argv[1] + '.out', 'w')
        log("File in " + sys.argv[1])

    casos = int(leelinea())

    for caso in range(1, casos+1):
        log("---------- Caso %d de %d" % (caso, casos))

        # Lee caso
        (kilometros, num_horses) = map(int, leelinea().split(" "))
        log ("%d kilometros. %d horses" % (kilometros, num_horses))

        horses = [];
        t = 0
        for i in range(num_horses):
            horses.append(map(int, leelinea().split(" ")))
            log("Caballo %d : km %d velmax = %d" % (i, horses[i][0], horses[i][1]))

            # Este caballo tarda...
            este = (kilometros*1.0 - horses[i][0]) / horses[i][1]
            log("Este caballo tarda %d" % (este))
            if este > t:
                t = este
                log("El mas lejano, por ahora")

        v = kilometros * 1.0 / t




        res = "%f" % (v)
        print >> fileout, "Case #%d: %s" % (caso, res)
