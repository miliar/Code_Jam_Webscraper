def split_cases(text):
    res = []
    text = text.split('\n')
    while text:
        lines = int(text.pop(0).split()[0])
        res.append([[int(y) for y in x.split(' ')] for x in text[:lines]])
        text = text[lines:]
    return res


def horizontal_largest(i, j, case):
    line = case[i]
    if case[i][j] == max(line):
        return True
    return False


def vertical_largest(i, j, case):
    point = case[i][j]
    for line in case:
        if point < line[j]:
            return False
    return True

input_file = "/Users/gerrrr/Downloads/B-large.in"
text = ''
with open(input_file) as f:
    f.readline()
    text = f.read().strip()

cases = split_cases(text)


def solve_case(case):
    for i in xrange(len(case)):
        for j in xrange(len(case[i])):
            if not (horizontal_largest(i, j, case) or
               vertical_largest(i, j, case)):
                return "NO"
    return "YES"

for i, r in enumerate(map(solve_case, cases)):
    print 'Case #%s: %s' % (i + 1, r)
