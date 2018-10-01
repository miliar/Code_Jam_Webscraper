def get_line(f):
    answer = int(f.readline().strip()) - 1
    lines = [f.readline().strip().split(' ') for x in xrange(4)]
    return set(lines[answer])

def solve(f):
    solution = get_line(f) & get_line(f)
    if len(solution) == 1:
        return solution.pop()
    elif len(solution) == 0:
        return 'Volunteer cheated!'
    elif len(solution) > 1:
        return 'Bad magician!'
    

data = []    
with open(raw_input('filename > '), 'r') as f:
    cases = int(f.readline().strip())
    for x in xrange(1, cases + 1):
        data.append('Case #%d: %s' % (x, solve(f)))
data = '\n'.join(data)
with open('output.txt', 'w') as f:
    f.write(data)
print data
        
