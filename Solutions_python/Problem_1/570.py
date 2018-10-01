def maisLonge(engines, queries):

    distancia = 0;
    try:
        for engine in engines:
            a = queries.index(engine)

            if (distancia < a):
                distancia = a
    except:
        return len(queries)

    return distancia

def caminho(engines, queries):

    f = 0
    changes = 0
    size = len(queries)

    while True:
        f += maisLonge(engines, queries[f:])

        if (f < size):
            changes += 1

        else:
            break

    return changes

f = open("c:\input.txt", "r")
o = open("c:\output.txt", "w")

n = int(f.readline())

for x in range(1, n + 1):

    engines = list()
    queries = list()

    l = int(f.readline())
    for a in range(l):
        engines.append(f.readline())
            
    l = int(f.readline())
    for a in range(l):
        queries.append(f.readline())

    o.write("Case #%d: %d\r" % (x, caminho(engines, queries)))
    del engines, queries

f.close()
o.close()
