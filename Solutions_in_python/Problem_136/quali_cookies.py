with open('B-small-attempt0.in') as in_put:
    content = in_put.readlines()

content = [line.strip('\n') for line in content]

N = int(content[0])

def time_elapsed(strategy,C,F,X):
    time = 0
    for farm in xrange(strategy):
        time = time + C/(2.+farm*F)
    return time + X/(2.+strategy*F)
    

with open('B-small-attempt0.out', 'w') as out_put:
    for case in xrange(N):
        [C,F,X] = content[case+1].split()
        C = float(C)
        F = float(F)
        X = float(X)
        strategy = 0 #buy strategy farms before finishing up
        time = time_elapsed(strategy,C,F,X)
        while time_elapsed(strategy+1,C,F,X) < time:
            time = time_elapsed(strategy+1,C,F,X)
            strategy = strategy+1
        print("Case #%d: %.7f" % (case+1,time))
        out_put.write("Case #%d: %.7f\n" % (case+1,time))

