import sys

def main(file):
    sys.setrecursionlimit(10000)
    n_cases = int(file.readline().strip())
    for i in range(n_cases):
        n_engines = int(file.readline().strip())
        engines = []
        for j in range(n_engines):
            engines.append(file.readline().strip())
        n_searches = int(file.readline().strip())
        searches = []
        for k in range(n_searches):
            searches.append(file.readline().strip())
        print "Case #%d: %d" % (i+1, num_switches(engines, searches))

def num_switches(engines, searches):
    high_index = -1
    for engine in engines:
        try:
            index = searches.index(engine)
        except ValueError:
            return 0
        if index > high_index:
            high_index = index
    return 1 + num_switches(engines, searches[high_index:])

if __name__ == "__main__":
    main(open(sys.argv[1]))
