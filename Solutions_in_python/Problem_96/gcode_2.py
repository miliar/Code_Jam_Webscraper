import math

def can_acheive(score, target, has_sup_flag=False):
    if score < target:
        return False

    left = score - target
    lower = int(math.floor(left / 2))
    higher = score - target - lower
    #print "({}, {}, {})\n".format(target, lower, higher)

    diff = max(target, higher, lower) - min(target, higher, lower)
    allowance = 2 if not has_sup_flag else 3
    if diff >= allowance:
        if target < 10:
            return can_acheive(score, target+1, has_sup_flag)

        return False

    return True

def solve(no_sup, target, googs_score):
    solved = []
    for goo in sorted(googs_score):
        if can_acheive(goo, target):
            solved.append(goo)
            googs_score.remove(goo)

    for goo in googs_score:
        if not no_sup:
            break

        if can_acheive(goo, target, True):
            solved.append(goo)
            no_sup = no_sup - 1

    return solved

def read_file(path):
    with open(path, 'r') as f:
        num_cases = int(f.readline()[:-1])
        lines = []
        for index in xrange(num_cases):
            parts = [int(x) for x in f.readline()[:-1].split(' ') if x ]
            no_googs = int(parts[0])
            no_sup = int(parts[1])
            target = int(parts[2])
            googs_score = [int(p) for p in parts[3:3+no_googs]]
            max_googs = solve(no_sup, target, googs_score)
            #print "COUNT: {}\n{}".format(len(recycled), recycled)
            #print "\n"
            print "Case #{}: {}".format(index+1, len(max_googs))


if __name__ == '__main__':
    import sys
    read_file(sys.argv[1])
