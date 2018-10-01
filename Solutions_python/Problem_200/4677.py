import time

def isTidy(x):
    if ''.join(sorted(str(x))) == str(x):
        return True
    return False

t = int(input())
for i in range(1, t + 1):
    n = [int(s) for s in input().split(" ")][0]
    found = False
    while True:
        #print(n)
        if isTidy(n):
            answer = n
            break
        n -= 1
        #time.sleep(1)
    print("Case #{}: {}".format(i, answer))
