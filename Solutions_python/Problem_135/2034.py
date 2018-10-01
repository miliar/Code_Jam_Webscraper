def main():

    pos_sol = []
    for i in xrange(4):
        if first_arr[ans1][i] in sec_arr[ans2]:
            pos_sol.append(first_arr[ans1][i])
    if len(pos_sol) == 1:
        return pos_sol[0]
    elif len(pos_sol) > 1:
        return 'Bad magician!'
    return 'Volunteer cheated!'

if __name__ == '__main__':

    import sys

    T = int(sys.stdin.readline())
    for t_case in xrange(1,T+1):

        ans1 = int(sys.stdin.readline()) - 1
        first_arr = [sys.stdin.readline().strip().split() for _ in xrange(4)]

        ans2 = int(sys.stdin.readline()) - 1
        sec_arr = [sys.stdin.readline().strip().split() for _ in xrange(4)]

        sys.stdout.write('Case #%d: %s\n' % (t_case, main()))
