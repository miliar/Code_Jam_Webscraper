class BadLogic():
    pass

def calc_largest_tidy(n):
    l = len(str(n))
    if int('1' * l) <= n:
        cur, ret = 1, ''
        for i in range(l):
            for d in range(9, cur - 1, -1):
                rem = l - i
                tmp = int(ret + (str(d) * rem))
                if tmp <= n:
                    cur = d;
                    ret += str(d)
                    break
            else:
                raise BadLogic()
        return ret
    else:
        return '9' * (l - 1)

def main():
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        print("Case #{t}: {ans}".format(t=t, ans=calc_largest_tidy(N)))

if __name__ == '__main__':
    main()
