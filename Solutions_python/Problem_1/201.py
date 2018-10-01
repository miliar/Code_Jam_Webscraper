import sys

def find_longest_prefix(q_list, engine_list):
    engine_set = set(engine_list)
    for x in range(len(q_list)):
        pre = q_list[:x+1]
        pre_set = set(pre)
        if len(engine_set - pre_set) > 0:
            continue
        else:
            return x
    return len(q_list)

def find_min(query, engine):
    if len(query) == 0:
        return 0

    count = -1
    while query:
        x = find_longest_prefix(query, engine)
        count += 1
        query = query[x:]
    return count

def main(path):
    f = open(path)
    n_case = int(f.readline())

    for i in range(n_case):
        n_engine = int(f.readline())
        engines = []
        for j in range(n_engine):
            e = f.readline()
            engines.append(e)

        n_query = int(f.readline())
        queries = []
        for j in range(n_query):
            q = f.readline()
            queries.append(q)

        print "Case #%d: %d" % (i + 1, find_min(queries, engines))
    f.close()


if __name__ == "__main__":
    import sys
    main(sys.argv[1])
