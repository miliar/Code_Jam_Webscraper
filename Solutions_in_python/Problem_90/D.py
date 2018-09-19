# -*- coding: utf-8 -*-
# Usage:
# python script.py input_file output_file
# If output_file is not specified, it simply
# writes the result to console
# Lines between #---v and #---^ are part of
# the template and should not be edited.

#----------v
import sys
import multiprocessing
#----------^

#----------v
def main(d):
#----------^

    graph = [[False for _ in range(d['n_planets'])] for __ in range(d['n_planets'])]
    for w in d['worms']:
        graph[w[0]][w[1]] = True
        graph[w[1]][w[0]] = True
    th = set()
    for x, w in enumerate(graph[0]):
        if w:
            th.add(x)
    paths = [[[0], th]]
    done = graph[0][1]
    while not done:
        old_paths = paths
        paths = []
        for p in old_paths:
            for d, w in enumerate(graph[p[0][-1]]):
                if w and d not in p[0]:
                    conq = p[0] + [d]
                    th = set(p[1])
                    th.discard(d)
                    for d2, w2 in enumerate(graph[d]):
                        if w2 and d2 not in conq:
                            th.add(d2)
                            if d2 == 1:
                                done = True
                    paths.append([conq, th])
    conquer = len(paths[0][0]) - 1
    threaten = 0
    for p in paths:
        if 1 in p[1] and len(p[1]) > threaten:
            threaten = len(p[1])
    result = str(conquer) + " " + str(threaten)

#----------v
    return result

def parse_input():
    input = open(sys.argv[1])
    n = int(input.readline())
    data = []
    for i in range(n):
        d = dict()
#----------^

        d['n_planets'], n_worms = map(int, input.readline().split())
        d['worms'] = map(lambda x: map(int, x.split(',')), input.readline().split())

#----------v
        data.append(d)
    input.close()
    return data

if __name__ == '__main__':
    data = parse_input()
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    output = None
    if len(sys.argv) == 3:
        output = open(sys.argv[2], 'w')
    for n, result in enumerate(pool.map(main, data)):
    #for n, d in enumerate(data):
    #    result = main(d)
        print("Case #"+str(n+1)+": "+str(result))
        if len(sys.argv) == 3:
            output.write("Case #"+str(n+1)+": "+str(result)+"\n")
    if len(sys.argv) == 3:
        output.close()
#----------^




