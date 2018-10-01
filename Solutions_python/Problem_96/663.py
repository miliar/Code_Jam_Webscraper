import sys

num_cases = int(sys.stdin.readline())

for case_num in range(num_cases):
    case = sys.stdin.readline().split()
    case = [int(i) for i in case]
    num_googlers = case[0]
    num_surprising = case[1]
    p = case[2]
    scores = case[3:]

    min_score = 3*p - 2
    surprising_min_score = min_score-2

    output = 0
    for score in scores:
        if score < p:
            continue
        if score >= min_score:
            output += 1
        elif num_surprising > 0 and score >= surprising_min_score:
            output += 1
            num_surprising -= 1

    print "Case #"+str(case_num+1)+":", output
