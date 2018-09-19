input_file = "large_input.in"

f = open(input_file)

num_cases = int(f.readline())
##print num_cases

num_search_engines = [0] * num_cases
num_queries = [0] * num_cases
search_engines = [0] * num_cases
queries = [0] * num_cases

for case in range(num_cases):
    num_search_engines[case] = int(f.readline())
    ##print num_search_engines
    search_engines[case] = [0] * num_search_engines[case]
    for i in range(num_search_engines[case]):
        search_engines[case][i] = str(f.readline())
##        print search_engines[case][i]

    num_queries[case] = int(f.readline())
    ##print num_queries
    queries[case] = [""] * num_queries[case]
    for i in range(num_queries[case]):
        queries[case][i] = str(f.readline())
##        print queries[case][i]


def allseen(arr, next):
    index = search_engines[case].index(q)
    for i in range(len(arr)):
        if (i != index and arr[i] == 0):
            return False
    return True

    
for case in range(num_cases):
    if (num_queries[case] < num_search_engines[case]):
        print "Case #" + str(case + 1) + ": 0";
    else:
        arr = [0] * num_search_engines[case]
        for engine in queries[case]:
##            print engine
            if (engine in search_engines[case]):
                index = search_engines[case].index(engine)
                arr[index] = arr[index] + 1

        arr.sort()

        if (arr[0] < 2):
            print "Case #" + str(case + 1) + ": " + str(arr.pop(0));
        else:
            seen = [0] * num_search_engines[case]
            switches = 0
            for q in queries[case]:
                if (allseen(seen, q)):
                    switches = switches + 1
                    seen = [0] * num_search_engines[case]
                    index = search_engines[case].index(q)
                    seen[index] = 1
                else:
                    if (q in search_engines[case]):
                        index = search_engines[case].index(q)
                        seen[index] = 1
            print "Case #" + str(case + 1) + ": " + str(switches);
