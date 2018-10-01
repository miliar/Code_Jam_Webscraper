import functools

__author__ = 'ben'

lines = [line.rstrip('\n') for line in open('input')][1:]

outFile = open("output", "w")

def merge(a, b):
    c = b.copy()
    for k, v in a.items():
        if k in c:
            c[k] += a[k]
        else:
            c[k] = a[k]
    return c


@functools.lru_cache(maxsize=None)
def f(gap):
    if gap == 1:
        return {(0, 0): 1}
    if gap == 2:
        return {(1, 0): 1, (0, 0): 1}
    if gap % 2 == 1:
        a = gap//2
        b = a
        return merge(merge(f(a), f(b)), {(a, a): 1})
    else:
        a = gap//2
        b = a - 1
        return merge(merge(f(a), f(b)), {(a, b): 1})

c = 1
for line in lines:
    result = list(reversed(sorted(f(int(line.split(" ")[0])).items())))
    total = 0
    target = int(line.split(" ")[1])
    for i in result:
        total += i[1]
        if total >= target:
            outFile.write("Case #{}: {} {}\n".format(c, i[0][0], i[0][1]))
            break
    c += 1

outFile.close()
