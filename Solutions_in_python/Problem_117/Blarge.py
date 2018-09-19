def matrix(height, width, value=None):
    """Return a list of lists representing a matrix."""
    function = value
    if not callable(value):
        function = lambda x, y: value
    return [[function(x, y) for x in range(height)] for y in range(width)]

def transpose(m):
    new_matrix = matrix(len(m), len(m[0]))
    for y in range(len(m)):
        for x in range(len(m[0])):
            new_matrix[x][y] = m[y][x]
    return new_matrix

target = open('B-large.in')
answer = open('B-large.txt', 'w')
target_string = target.read()
line = target_string.splitlines()
number_test_cases = int(line[0])
next_case = 1
for case in range(number_test_cases):
    answer.write('Case #' + str(case+1) + ': ')
    N = int(line[next_case].split()[0])
    M = int(line[next_case].split()[1])
    m = matrix(N, M)
    for x in range(M):
        for y in range(N):
            m[x][y] = int(line[next_case+y+1].split()[x])
    ok = True
    m_transpose = transpose(m)
    min_height = matrix(N,M)
    for x in range(M):
        for y in range(N):
            min_height[x][y] = min(max(m[x]), max(m_transpose[y]))
            if min_height[x][y] > m[x][y]:
                ok = False
    if ok:
        answer.write('YES\n')
    else:
        answer.write('NO\n')
    next_case += N + 1
target.close()
answer.close()
