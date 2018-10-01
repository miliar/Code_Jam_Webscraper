from math import ceil

testcases = int(input())

def best_result(t, s, p):
    counter = 0
    for g in t:
        # special cases
        if p > 10:
            continue
        # any googler passes
        if p <= 0:
            counter += 1
            continue
        # no googler passes with so few points
        if g == 0:
            continue
        # if googler has in total 1 point, he took exactly 1 point
        if g == 1:
            if p <= 1:
                counter += 1
                continue
            
        # general case
        g /= 3
        if ceil(g) >= p:
            counter += 1
        elif round(g + 1) >= p and s > 0:
            s -= 1
            counter += 1
            
    return counter
            

for i in range(1, testcases + 1):
    in1 = [int(i) for i in input().split()]
    (N, S, p, t) = (in1[0], in1[1], in1[2], in1[3:])
    
    print('Case #' + str(i) + ': ' + str(best_result(t, S, p)))
