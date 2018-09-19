from itertools import product, permutations, compress
from root.codejam.Tools import Problem
import operator
#copy sample input and output here
sampleIn = """3
2 5
0.6 0.6
1 20
1
3 4
1 0.9 0.1
"""
sampleOut = """Case #1: 7.000000
Case #2: 20.000000
Case #3: 4.500000
"""

def expect(probs, strokes):
    return sum([1.0 * probs[i] * strokes[i] for i in range(len(probs))])

def getprob(p_list, binary):
    rv = []
    for i in range(len(p_list)):
        rv.append(p_list[i]  if binary[i] == 1 else (1 - p_list[i]))
    return reduce(operator.mul, rv)

def getStrokeKeepTyping(A, B, binary):  
    if binary != (1,) * A:
        return 2 * B - A + 2
    else:
        return B - A + 1
    
def getStrokeBackspace(A, B, binary, nBack):
    deleted = binary[:-1 * nBack] == (1,) * (A - nBack)  
    if deleted:
        return 2 * nBack + B - A + 1
    else:
        #backspace, finish typing, found wrong, type again
        return nBack + nBack + B - A + 1 + B + 1  
        
    
    
def cal2(A, B, p_list):
    strings = product((1, 0), repeat=A)
    prob = []
    keeptyping = []
    enternow = []
    backspace = [[] for i in range(A)]
    for binary in strings:
        prob.append(getprob(p_list, binary))
        keeptyping.append(getStrokeKeepTyping(A, B, binary))
        enternow.append(2 + B)
        for i in range(A):    
            backspace[i].append(getStrokeBackspace(A, B, binary, i + 1))
    
#    print 'prob', prob
#    print keeptyping, expect(prob, keeptyping)
    rv = expect(prob, keeptyping)
    for i in range(A):    
#        print 'backpace%s' % (i + 1)
#        print backspace[i], expect(prob, backspace[i])
        rv = min(rv, expect(prob, backspace[i]))
#    print 'enternow', enternow, expect(prob, enternow)
    rv = min(rv, expect(prob, enternow))
    return rv





class ProblemA(Problem):
    def solve(self, inputObj):
        line = inputObj.nextLine(sep=' ', toInt=True)
        #unpack the parameters
        #e.g: N, S, p = line[:3]; t_list = line[3:];
        A, B = line
        #percentages
        p_list = inputObj.nextLine(sep=' ', toFloat=True)     
        
        return cal2(A, B, p_list)




if __name__ == '__main__':
    p = ProblemA('A', sampleIn)
    p.interact()
        
