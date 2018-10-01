
def calc(n,k):
    rems = []
    rems.append(n)
    num = rems[0]
    for i in range(k):
        num = rems.pop(0)
        if num % 2 == 0:
            rems.append(num/2)
            rems.append((num/2)-1)
        else:
            rems.append(num/2)
            rems.append(num/2)
        if i != (k-1):
            rems = sorted(rems, reverse=True)
    rems = rems[::-1]
    if rems[0] == -1:
        rems[0] = 0
    if rems[1] == -1:
        rems[1] = 0
    return rems[1], rems[0]

for i in range(input()):
    n, k = map(int,raw_input().strip().split())
    maxi, mini = calc(n, k)
    print "Case #{}: {} {}".format(i + 1, maxi, mini)
