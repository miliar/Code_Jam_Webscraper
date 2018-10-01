import sys

INPUT_FILE = 'C:\Users\Marius\Downloads\A-small-attempt0.in'

global graph, visited, reached

def search(D, vines, state):
    global graph, visited, reached
    visited.add(state)

    pos, num = state
    d, l = vines[num]

    if pos + d >= D:
        reached = 'YES'

    for i in xrange(num + 1, len(vines)):
        if pos + d < vines[i][0]:
            break
        if abs(vines[i][0] - d) <= vines[i][1]:
            np = abs(vines[i][0] - d)
        else:
            np = vines[i][1]
        ns = (np, i)
        if ns not in visited:
            search(D, vines, (np, i))

def solve(D, vines):
    global graph, visited, reached
    graph = {}
    visited = set()
    initial = (vines[0][0], 0)

    reached = 'NO'
    search(D, vines, initial)
    return reached

def main():
    try:
        file = INPUT_FILE
    except NameError:
        file = 'SampleTests.txt'
    fh = open(file)
    number_of_cases = int(fh.readline())
    for case in range(number_of_cases):
        N = int(fh.readline())
        vines = [[int(x) for x in fh.readline().split()] for y in xrange(N)]
        D = int(fh.readline())
        result = solve(D, vines)
        print 'Case #%s: %s' % (case + 1, result)

if __name__ == '__main__':
    try:
        sys.stdout = open('Result.txt', 'w')
        main()
    finally:
        sys.stdout = sys.__stdout__
