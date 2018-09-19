import sys
sys.stdout = open("out.txt","w")
sys.stdin = open("in.txt", "r")
T = int(input())
for q in range(T):
    C, F, X = map(float, input().split())
    time = 0.0
    prod = 2.0
    done = 0.0
    ans = 123253643646444565656
    ansopt = 0
    while ansopt < 5:
        if ans >= time + X / prod:
            ans = time + X / prod
        else:
            ansopt += 1
        time += C / prod
        prod += F
    print("Case #%s: %s"%(q+1, ans))

