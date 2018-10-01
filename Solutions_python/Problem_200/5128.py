def foo(x):
    k = 1
    x = int(x)
    last = k
    while k <= x:
        string = str(k)
        if string == merge(sorted(string)):
            last = k
        k += 1

    return last


def merge(l):
    string = ''
    for s in l:
        string += s
    return string


length = int(input())
for i in range(1, length + 1):
    last = foo(int(input()))
    print("Case #{}: {}".format(i, last))
