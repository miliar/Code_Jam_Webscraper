import itertools

def all_scores():
    score = set()

    for x in itertools.product(list(range(11)), repeat=3):
        ss = tuple(sorted(list(x)))
        if max(ss) - min(ss) <= 2:
            score.add(ss)
    return score

surprise = {}
normal = {}

for s in all_scores():
    if max(s) - min(s) == 2:
        surprise[sum(s)] = max(s)
    else:
        normal[sum(s)] = max(s)

def solve_line(scores, surprises, limit):
    above, maybe, below = [], [], []

    for s in scores:
        if s in normal and normal[s] >= limit:
            above.append(s)
        elif s in surprise and surprise[s] >= limit:
            maybe.append(s)
        else:
            below.append(s)

    return len(above) + min(surprises, len(maybe))

def solve(path):
    outpath = path.replace("in", "out")

    with open(path) as fin:
        with open(outpath, "w") as fout:
            num_cases = int(fin.readline())

            for n in range(num_cases):
                data = [int(s) for s in fin.readline().strip().split()]
                goog = data.pop(0)
                surp = data.pop(0)
                limi = data.pop(0)
                sol = solve_line(data, surp, limi)
                fout.write("Case #%i: %i\n" % (n+1, sol))
                print "Case #%i: %i" % (n+1, sol)
