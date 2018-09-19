def output(f, solution_iter):
    s = list()
    for solution in solution_iter:
        s.append('Case #')
        s.append(str(solution['number']))
        s.append(': ')
        s.append('%.6f' % solution['avg'])
        s.append('\n')
        pass
    f.write(''.join(s))
    pass

def read(f):
    fiter = iter(f)
    cases = int(next(fiter))
    raw_problem_iter = list()
    for x in range(cases):
        numbers = int(next(fiter))
        raw_problem_iter.append({
            'number': x + 1,
            'data': next(fiter).rstrip('\n').split(' '),
        })
        pass
    return iter(raw_problem_iter)

def convert(raw_problem):
    return {
        'number': raw_problem['number'],
        'data': [int(x) for x in raw_problem['data']],
    }

def solution(problem):
    solu = dict()
    solu['number'] = problem['number']
    num = 1
    error = 0
    for ele in problem['data']:
        if num != ele:
            error += 1
            pass
        num += 1
        pass
    solu['avg'] = error
    return solu

def frame(in_file_path, out_file_path):
    solist = list()
    for raw_problem in read(open(in_file_path)):
        p = convert(raw_problem)
        s = solution(p)
        solist.append(s)
        pass
    output(open(out_file_path, 'w'), iter(solist))
    pass
