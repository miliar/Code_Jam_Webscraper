import sys

#WORD = "So you've registered. We sent you a welcoming email, to welcome you to code jam. But it's possible that you still don't feel welcomed to code jam. That's why we decided to name a problem \"welcome to code jam.\" After solving this problem, we hope that you'll feel very welcome. Very welcome, that is, to code jam."
#WORD = "elcomew elcome to code jam"
#WORD = "wweellccoommee to code qps jam"
#WORD = "welcome to codejam"
STR = "welcome to code jam"

def init_partial():
    partial = []
    for i in range(0, len(STR)):
        partial.append(-1)
    return partial

def test_cases(FILENAME):
    f = open(FILENAME)
    total = f.readline()
    for line in f:
        yield line
    f.close()

def solve(word):
    partial = init_partial()
    solutions = 0
    low = word.find(STR[0])
    high = word.rfind(STR[-1])
    word = word[low:high+1]
    last = word.rfind(STR[0])
    end = len(STR) - 1
    
    partial[0] = 0
    i = 1
    
    while i >= 0:
        previous = partial[i-1] if i > 0 else partial[0]
        from_index = max(previous,partial[i])
        index = word.find(STR[i],from_index+1)
        if index >= 0: #exito, sigo
            partial[i] = index
            if i == end: #llegue al final, contar la solucion, ir para atras 
                solutions += 1
            else:
                i += 1
        else: #backtrack!
            partial[i] = -1
            i -= 1
            
    return solutions

def do_C(FILENAME):
    cases = test_cases(FILENAME)
    for case in cases:
        solution = solve(case)
        yield solution
 
def output(solutions):
    f = open('C:\\output_C.txt', 'w')
    i = 1
    for solution in solutions:
        solution = str(solution)
        solution = solution[-4:]
        left = 4-len(solution)
        solution = (left * '0') + solution
        f.write("Case #%s: %s\r\n" % (i,solution))
        i += 1
    f.close()
    
if __name__ == '__main__':
    solutions = do_C(sys.argv[1])
    output(solutions)