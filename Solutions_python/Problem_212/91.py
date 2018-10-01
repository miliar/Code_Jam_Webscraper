from collections import Counter

t = int(raw_input())
for c in xrange(1, t+1):
    n, s = map(int, raw_input().split())
    groups = map(int, raw_input().split())
    divisible = [i for i in groups if i % s == 0]
    nonmod = [i % s for i in groups if i % s != 0]
    counter = Counter(nonmod)
    extra = False
    if s == 2:
        result = len(divisible) + counter[1] // 2
        extra = counter[1] % 2 != 0
    if s == 3:
        stuff = min(counter[1], counter[2])
        counter[1] -= stuff
        counter[2] -= stuff
        stuff1 = counter[1] // 3
        counter[1] -= stuff1*3
        stuff2 = counter[2] // 3
        counter[2] -= stuff2*3
        result = len(divisible) + stuff + stuff1 + stuff2
        extra = counter[1] or counter[2]
        # print stuff, stuff1, stuff2, result, extra
    if s == 4:
        result = len(divisible) + min(counter[1], counter[3]) + counter[2] // 2
        extra = counter[3] != counter[1] or counter[2] % 2 != 0
    if extra:
        result += 1
    print("Case #{}: {}".format(c, result))