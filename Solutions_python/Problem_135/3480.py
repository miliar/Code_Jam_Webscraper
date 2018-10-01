import sys

T = int(sys.stdin.readline())

class Case(object):
    def __init__(self, ans_one, ans_two, grid_one, grid_two):
        self.ans_one = ans_one
        self.ans_two = ans_two
        self.grid_one = grid_one
        self.grid_two = grid_two

    def solve(self):
        res = self.grid_one[self.ans_one - 1] & self.grid_two[self.ans_two - 1]
        if len(res) == 1:
            answer = list(res)[0]
        elif len(res) > 1:
            answer = 'Bad magician!'
        else:
            answer = 'Volunteer cheated!'
        return answer


for i in xrange(1, T+1):
    ans_one = int(sys.stdin.readline())
    grid_one = []
    for _ in range(4):
        grid_one.append(set(sys.stdin.readline().split()))
    ans_two = int(sys.stdin.readline())
    grid_two = []
    for _ in range(4):
        grid_two.append(set(sys.stdin.readline().split()))

    case = Case(ans_one, ans_two, grid_one, grid_two)
    print 'Case #%s: %s' % (i, case.solve())