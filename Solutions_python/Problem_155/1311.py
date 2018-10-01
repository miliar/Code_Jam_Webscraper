def to_num(l):
    return list(map(int, l))
    
def readline():
    return input().split(' ')

def main():
    T = to_num(readline())[0]
    for t in range(T):
        n, s = readline()
        n = int(n)
        s = to_num(list(s))
        num = 0
        add = 0
        for i, v in enumerate(s):
            if v > 0 and i > num:
               add += (i - num)
               num = i
            num += v
        print("Case #{}: {}".format(t + 1, add))

main()