def main():
    fi = open('in.txt', 'r')
    fo = open('out.txt', 'w')
    T = int(fi.readline())

    for cas in range(1, T + 1):
        fo.write('Case #%d: ' % cas)
        parts = fi.readline().split()
        A = int(parts[0])
        B = int(parts[1])

        ans = 0
        for i in range(A, B + 1):
            si = str(i)
            l = len(si)
            d = {}
            sk = si
            for j in range(0, l - 1):
                sk = si[j + 1 : ] + si[ : j + 1]
                k = int(sk)
                if k != i and k >= A and k <= B:
                    d[k] = 0
            ans += len(d)

        ans /= 2
        fo.write('%d\n' % ans)

if __name__ == '__main__':
    main()
