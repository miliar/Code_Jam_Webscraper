def solve(C,F,X):
    S = 2
    cost = 0
    least = X/S
    while((C/S + cost + X/(S+F)) < least):
        cost = cost + C/S
        S = S + F
        least = cost + X/S
    return least

    
f = open('B-large.in', 'r')
line1 = f.readline()
cases = int(line1)
for case in range(1,cases+1):
    line = f.readline()
    prob = line.split()
    C = float(prob[0])
    F = float(prob[1])
    X = float(prob[2])
    print "Case #"+str(case)+ ": " + str(solve(C,F,X))
