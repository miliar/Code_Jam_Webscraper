def isTidy(l):
    return l == sorted(l)

def joined(lst):
    return "".join(str(item) for item in lst)

for t in range(int(input())):
    n = int(input())
    print("Case #{}: ".format(t + 1), end = "")
    n = [int(item) for item in list(str(n))]
    u = len(n)
    if isTidy(n):
        print(joined(n))
    else:
        i = 1
        while isTidy(n[:i - 1] + [n[:i][-1] - 1]):
            l = n[:i - 1] + [n[:i][-1] - 1] + [9] * (u - i)
            i += 1
            #print(l)
        print(int(joined(l)))