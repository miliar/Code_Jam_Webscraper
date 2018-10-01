from pprint import pprint
from difflib import Differ
from itertools import tee
import logging
import multiprocessing

__author__ = 'Robert'

class brain():
    def __init__(self, data):
        self.data = data
        self.cases = int(next(self.data))
        #self.N,self.M = map(int, data.next().split())
        #self.cache = {}
        self.results = list(self.solve_cases())

    def solve_cases(self):
        for case in range(1, self.cases + 1):
            result = self.solve_case(case)
            print result
            yield result

    def solve_case(self,case):
        A,B = map(int, next(self.data).split())
        count = 0
        for a in range(A,B+1):
            for b in range(a+1,B+1):
                a = str(a)
                b = str(b)
                for i in range(len(a)):
                    if a[i:] + a[:i] == b:
                        count += 1
                        break

        result = count
        return "Case #%s: %s" % (case, result)

def get_data(filename):
    try:
        with open(filename) as input_file:
            for line in input_file:
                line = line.strip()
                if line == "":
                    raise RuntimeError("blank line")
                yield line
    except IOError,e:
        print e
        for line in input_:
            yield line

def main():
    my_brain = brain(get_data("C-small-attempt0.in"))

    print ""
    print "checking results.. "
    pprint(list(Differ().compare(my_brain.results, solution)))

    #write results
    with open("out.txt",'w') as file_:
        file_.write("\n".join(my_brain.results))


table = """4
1 9
10 40
100 500
1111 2222

Case #1: 0
Case #2: 3
Case #3: 156
Case #4: 287
"""
table = table.splitlines()
i = table.index("")
input_ = table[:i]
solution = table[i+1:]

if __name__ == '__main__':
    print ""
    print "running.."
    main()