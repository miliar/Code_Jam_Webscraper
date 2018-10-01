from math import log, pow
import copy

def patrick_add(x, y):
    return (x|y)-(x&y)

def patrick_sum(list):
    if( len(list) == 1 ): return list[0]
    val = 0
    for i in list:
        val = patrick_add(val, i)
    return val

def comb(list): 
    return list and map(lambda x,list=list: [list[0]]+x , comb(list[1:])) + comb(list[1:]) or [[]]
        
def diff(list, origin):
    for i in list:
        origin.remove(i)
        
    return origin

def solve(candybag):
    numbers = []
    solution = []
    feasible = 0
    
    for t in candybag.split(' '):
        numbers.append(int(t))

    subset = comb(numbers)
    difset = copy.copy(subset)
    difset.reverse()
    
    for i in range(0, len(subset)):
        sum_a = patrick_sum(subset[i])
        sum_b = patrick_sum(difset[i])
        
        if( sum_a == sum_b and sum_a != 0):
            solution.append([subset[i], difset[i]])
                    
    for candidate in solution:
        sum_a = sum(candidate[0])
        sum_b = sum(candidate[1])
        greater = sum_a if sum_a > sum_b else sum_b
        feasible = greater if greater > feasible else feasible
    
    return feasible if solution else 'NO'


def mainRoutine():
    infile = open("C.in", 'r')
    outfile = open("C.out", 'w')
    
    C = int(infile.readline())
    
    for case in range(1, C+1):
        T = int(infile.readline())
        line = infile.readline()
        
        outfile.write("Case #%d: %s\n" % (case, solve(line)))
    
    infile.close()
    outfile.close()


if __name__ == "__main__":
    mainRoutine()
