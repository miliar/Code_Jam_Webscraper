from sortedcontainers import SortedDict
from math import floor,ceil
FILENAME = "C-small-2-attempt1.in"
OUTPUT = "stalls_output.txt"

def main():
    f = open(FILENAME, "r")
    o = open(OUTPUT, "w")
    testcases = int(f.readline())
    n = 1
    for i in f:
        l = i.split()
        res1, res2 = compute(int(l[0]), int(l[1]))
        o.write("Case #" + str(n) + ": " + str(res1) + " " + str(res2) + "\n")
        print(res1, res2)
        n = n+1
    o.close()
    f.close()
    return

def compute(N, K):

    lst = SortedDict()

    def lst_add(length, mult):
        if length in lst:
            oldval = lst[length]
            lst[length] = oldval + mult
        else:
            lst[length] = mult
    def lst_rem(length, mult=-1):
        if mult == -1:
            mult = lst[length]

        if length in lst:
            if lst[length] == mult:
                del lst[length]
            else:
                oldval = lst[length]
                lst[length] = oldval - mult
        else:
            raise ValueError

    lst[N] = 1

    i = 1
    while i < K:
        left = K-i

        t = lst.popitem()
        lent = t[0] # length
        mult = t[1]
        use = min(left, mult)

        new_length1 = int(floor((lent-1) / 2))
        new_length2 = int(ceil((lent-1) / 2))
        if new_length1 > 0:
            lst_add(new_length1, use)
        if new_length2 > 0:
            lst_add(new_length2, use)
        if use < mult:
            lst_add(lent, mult-use)

        i+=use

    t = lst.popitem()
    tl = t[0]
    new_length1 = int(floor((tl - 1) / 2))
    new_length2 = int(ceil((tl - 1) / 2))

    return (max(new_length1,new_length2), min(new_length1,new_length2))

main()