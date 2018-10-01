import fileinput

def read_problem(stdin):
    row = int(stdin.next()) - 1
    for i in range(4):
        if i == row:
            ret = [int(n) for n in stdin.next().split()]
        else:
            stdin.next()
    return ret

def solve(stdin):
    r1 = read_problem(stdin)
    r2 = read_problem(stdin)
    d = set(r1) & set(r2)
    if len(d) == 1:
        return d.pop()
    if len(d) == 0:
        return "Volunteer cheated!"
    return "Bad magician!"

if __name__ == '__main__':
    stdin = fileinput.input()
    nprobs = int(stdin.next())
    for n in range(1, nprobs + 1):
        print "Case #%d:" % n, solve(stdin)
