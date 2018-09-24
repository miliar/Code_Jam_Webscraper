def main():
    fi = open("data.in")
    cases = int(fi.readline())
    output = []
    i=1
    while i <= cases:
        ##Read data
        switches = 0
        engines, queries = list(),list()
        nrOfEngines = int(fi.readline())
        while nrOfEngines >0:
            line = fi.readline()
            engines.append(line[:-1])
            nrOfEngines-=1
        nrOfQueries = int(fi.readline())
        while nrOfQueries >0:
            line = fi.readline()
            queries.append(line.strip())
            nrOfQueries-=1
        ##Main logic
        qc,finish = 0,0
        seen = list()
        while qc < len(queries):
            while len(seen) != len(engines):
                if qc == len(queries):
                    break
                if not queries[qc] in seen:
                    if queries[qc] in engines:
                        seen.append(queries[qc])
                qc+=1
            if len(seen) == len(engines):
                switches+=1
            seen = [seen.pop()]
        if i < cases:
            output.append('Case #%s: %s\n' % (i, switches))
        else:
            output.append('Case #%s: %s' % (i, switches))
        i+=1
    fi.close()
    fo = open("data.out","w+")
    fo.writelines(output)
    fo.close()
main()