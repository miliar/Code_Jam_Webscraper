def output(f, solution_iter):
    s = list()
    for solution in solution_iter:
        s.append('Case #')
        s.append(str(solution['number']))
        s.append(': ')
        s.append(str(solution['time']))
        s.append('\n')
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
    blist = list()
    olist = list()
    bo = list()
    i = iter(raw_problem['data'])
    presses = int(next(i))
    for press in range(presses):
        robot = next(i)
        button = int(next(i))
        bo.append((robot, button,))
        pass
    print bo
    return {
        'number': raw_problem['number'],
        'data': bo,
    }

def solution(problem):
    borange = (1,1)
    solu = dict()
    solu['number'] = problem['number']
    if 0 < len(problem['data']):
        current = problem['data'][0][0]
        exetime = 0
        time = 0
        for ele in problem['data']:
            if ele[0] == current:
                exetime += 1 + abs(borange[0] - ele[1])
                time += 1 + abs(borange[0] - ele[1])
                borange = (ele[1], borange[1],)
                pass
            else:
                current = ele[0]
                borange = (borange[1], borange[0])
                #
                exetime = 1 + max(0, abs(borange[0] - ele[1]) - exetime)
                time += exetime
                borange = (ele[1], borange[1],)
                pass
            pass
        solu['time'] = time
        pass
    else:
        solu['time'] = 0
        pass
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
