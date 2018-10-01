import sys, itertools

lines_per_case = 1

def solve_case(case):
    case = case[0].split()
    
    end = int(case[0])
    start = 0
    combinations = {}
    for rule in case[start + 1:end + 1]:
        combinations[rule[:2]] =  rule[2];
        combinations[rule[1::-1]] =  rule[2];
    
    eliminations = {}
    current_eliminations = {}
    start = end + 1
    end = int(case[start]) + start
    for elim in case[start + 1:end + 1]:
        (x,y) = elim
        eliminations[x] = y
        eliminations[y] = x
        current_eliminations[x] = 0
        current_eliminations[y] = 0
        
    result = []
    prev = ''
    
    for e in case[-1]:
        c = prev + e
        if  c in combinations:
            if prev in eliminations and current_eliminations[prev] > 0:
                current_eliminations[prev] -= 1
            prev = combinations[c]
            result[-1] = prev
        else:
            result.append(e)
            prev = e
            
            if e in eliminations:
                o = eliminations[e]
                if current_eliminations[o]:
                    for k in eliminations:
                        current_eliminations[k] = 0
                    result = []
                    prev = ''
                else:
                    current_eliminations[e] += 1
            
    return str(result).replace("'", "")


def get_time(bot, button, state):
    return abs(int(button) - int(state[bot]['b'])) + 1


def produce_output(index, solution):
    print 'Case #%s: %s' % (index, solution)


def get_test_cases(lines, n_of_lines_per_case=1):
    return itertools.izip(*(iter(lines[i::n_of_lines_per_case] for i in range(n_of_lines_per_case))));

if __name__ == "__main__":
    if(len(sys.argv) > 1):
        fn = sys.argv[1]
        with open(fn) as f:
            lines = f.readlines()
            nt = int(lines[0])
            for index, case in enumerate(get_test_cases(lines[1:], lines_per_case), 1):
                solution = solve_case(case)
                produce_output(index, solution)