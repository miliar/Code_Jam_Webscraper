filename = "C-small-attempt1.in"
f = open(filename)
T = int(f.readline())
fair_and_square = [1,4,9,121,484]
for case in range(1,T+1):
    s = f.readline()
    A, B = map(int,s.split())
    answer = 0
    for koho in fair_and_square:
        if koho in range(A,B+1):
            answer += 1
    print "Case #" + str(case) + ": " + str(answer)
