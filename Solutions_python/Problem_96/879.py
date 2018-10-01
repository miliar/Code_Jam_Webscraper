import sys

def best_normal_result(total_score):
    base, n = total_score / 3, total_score % 3
    return base + 1 if n else base

def best_suprising_result(total_score):
    base, n = total_score / 3, total_score % 3
    if total_score < 2 or total_score > 28:
        return None
    elif n == 0 or n == 1:
        # n=0: 3 = (1,1,1) = (2,1,0)
        # n=1: 4 = (2,1,1) = (2,2,0)
        return base + 1
    else:
        # n=2: 5 = (2,2,1) = (3,2,1)
        return base + 2

best_normal_results = [best_normal_result(ts) for ts in range(31)]
best_suprising_results = [best_suprising_result(ts) for ts in range(31)]

def maximium_googlers(total_scores, suprising_results, p):
    googlers = 0
    close_but_below_p = []

    for total_score in total_scores:
        if best_normal_results[total_score] >= p:
            googlers += 1
        elif total_score >= p - 2 and suprising_results > 0:
            if best_suprising_results[total_score] >= p:
                suprising_results -= 1
                googlers += 1

    return googlers

num_cases = int(sys.stdin.readline())
for i, line in zip(range(1, num_cases + 1), sys.stdin):
    sys.stderr.write('Case #%d out of %d\n' % (i, num_cases))
    splitted = line.split(' ')

    googlers = int(splitted[0])
    suprising_results = int(splitted[1])
    p = int(splitted[2])
    total_scores = [int(s) for s in splitted[3:]]

    print "Case #%d: %d" % (i, maximium_googlers(total_scores,
                                                 suprising_results,
                                                 p))
