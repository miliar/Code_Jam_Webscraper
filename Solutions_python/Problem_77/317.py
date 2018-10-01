from random import shuffle
import copy
import sys
# from http://networkx.lanl.gov/ 
import networkx as nx

sys.setrecursionlimit(10000)

def sim(n):
    l = range(n)
    shuffle(l)
    shuffles = 0
    while len(l) > 0:
        shuffles += 1
        for i in l:
            if l.index(i) == i:
                n -= 1
        l = range(n)
        shuffle(l)
    return shuffles


def solver(numbers):
    # return answer
    sorted_numbers = copy.copy(numbers)
    sorted_numbers.sort()
    edges = zip(numbers, sorted_numbers)
    edges = [edge for edge in edges if edge[0] != edge[1]]
    g = nx.DiGraph(edges)
    cycles = nx.simple_cycles(g)
    answer = 0
    for c in cycles:
        answer += len(c) - 1
    return answer


def ssi(s):
    """
    space separated integers
    """
    return map(int, s.strip('\n').split())

def main():
    # open input file
    input_file = open('infile.txt')
    cases = int(input_file.readline())
    output = []
    # loop through cases passing input to solver
    for c in range(cases):
        print c
        num = int(input_file.readline())
        numbers = ssi(input_file.readline())
        answer = solver(numbers)
        output.append('Case #%d: %d\n' % (c+1, answer))
    input_file.close()
    # open output file
    output_file = open('outfile.txt', 'w')
    # write ouput to file
    output_file.writelines(output)
    # close out file
    output_file.close()
    print 'Done!'



if __name__=='__main__':
    main()
