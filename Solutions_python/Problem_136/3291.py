import sys
sys.stdin = open("input.txt")
sys.stdout = open("output.txt", "w+")

for case in range(1, input()+1):
    output = "Case #%s: " % case

    P = 2.0 # per second producing cookies
    Y = 0.0 # current cookies
    Z = 0.0 # current time
    C, F, X = map(float, raw_input().split())

    R = 0.0
    while True:
        A = Z + (X-Y)/P
        B = Z + (C-Y)/P + X/(P+F)

        if A < B:
            R = A
            break

        Z += (C-Y) / P
        P += F
        Y = 0.0

    output += "%.7f" % R
    print output
