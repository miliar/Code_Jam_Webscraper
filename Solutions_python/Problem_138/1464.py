import sys

sys.stdin = open("input.in")
sys.stdout = open("output.txt", "w")
tn = int(sys.stdin.readline());

for ti in range(tn):
    n = int(sys.stdin.readline());
    wa = [float(x) for x in sys.stdin.readline().split()];
    wb = [float(x) for x in sys.stdin.readline().split()];
    wa.sort();
    wb.sort();
    a = wa[:]
    b = wb[:]
    score = 0

    for i in range(n):
        win = 0
        for j in range(len(a)):
            if b[i] < a[j]:
                score += 1
                del a[j]
                win = 1
                break
        if win != 1:
            break

    print "Case #%s:" % (ti + 1), score,

    a = wb[:]
    b = wa[:]
    score = 0

    for i in range(n):
        win = 0
        for j in range(len(a)):
            if b[i] < a[j]:
                score += 1
                del a[j]
                win = 1
                break
        if win != 1:
            break

    print n-score


sys.stdout.close()
