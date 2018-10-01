def output(f, solution_iter):
    s = list()
    for solution in solution_iter:
        s.append('Case #')
        s.append(str(solution['number']))
        s.append(': [')
        s.append(', '.join(solution['stack']))
        s.append(']\n')
        pass
    f.write(''.join(s))
    pass

def read(f):
    fiter = iter(f)
    cases = int(next(fiter))
    raw_problem_iter = list()
    for x in range(cases):
        raw_problem_iter.append({
            'number': x + 1,
            'data': next(fiter).rstrip('\n').split(' '),
        })
        pass
    return iter(raw_problem_iter)

def convert(raw_problem):
    combine = list()
    oppose = list()
    #
    i = iter(raw_problem['data'])
    cs = int(next(i))
    for x in range(cs):
        combine.append(next(i))
        pass
    os = int(next(i))
    for x in range(os):
        oppose.append(next(i))
        pass
    es = int(next(i))
    element = next(i)
    return {
        'number': raw_problem['number'],
        'combine': combine,
        'oppose': oppose,
        'element': element,
    }

def solution(problem):
    solu = dict()
    solu['number'] = problem['number']
    if 0 == len(problem['element']):
        solu['stack'] = list()
        pass
    elif 1 == len(problem['element']):
        solu['stack'] = [problem['element']]
        pass
    else:
        solu = hard_solution(problem)
        pass
    return solu

def hard_solution(problem):
    solu = dict()
    solu['number'] = problem['number']
    combine = dict()
    for trip in problem['combine']:
        combine[(trip[0], trip[1])] = trip[2]
        combine[(trip[1], trip[0])] = trip[2]
        pass
    oppose = dict()
    for dup in problem['oppose']:
        oppose[dup[0]] = dup[1]
        oppose[dup[1]] = dup[0]
        pass
    #
    #print 'start'
    eliter = iter(problem['element'])
    stack = list()
    stack.append(next(eliter))
    #print stack[0], stack
    for current in eliter:
        what(combine, oppose, stack, current)
        pass
    solu['stack'] = stack
    return solu

def what(combine, oppose, stack, letter):
    if stack:
        last = stack.pop()
        if (last, letter) in combine:
            #print last + ' ' + letter + ' ' + combine[(last, letter)], stack
            new = combine[(last, letter)]
            what(combine, oppose, stack, new)
            pass
        elif letter in oppose:
            if (oppose[letter] in stack) or (oppose[letter] == last):
                for x in range(len(stack)):
                    stack.pop()
                    pass
                #print last + ' ' + letter + ' ' + 'clear', stack
                pass
            else:
                stack.append(last)
                stack.append(letter)
                #print letter, stack
                pass
            pass
        else:
            stack.append(last)
            stack.append(letter)
            #print letter, stack
            pass
        pass
    else:
        stack.append(letter)
        #print letter, stack
        pass
    pass

def frame(in_file_path, out_file_path):
    solist = list()
    for raw_problem in read(open(in_file_path)):
        p = convert(raw_problem)
        s = solution(p)
        solist.append(s)
        pass
    output(open(out_file_path, 'w'), iter(solist))
    pass
