import sys


def main(in_stream, out_stream):
    t = int(in_stream.readline())
    for tc in range(t):
        n = int(in_stream.readline())
        a = map(lambda x: float(x), in_stream.readline().split())
        b = map(lambda x: float(x), in_stream.readline().split())
        a = sorted(a)
        b = sorted(b)
        dw = 0
        w = 0
        for i in range(n):
            if a[i] > b[dw]:
                dw += 1
            if b[i] > a[w]:
                w += 1
        out_stream.write("Case #%d: %d %d\n" % (tc + 1, dw, n - w))

if __name__ == '__main__':
    # main(sys.stdin, sys.stdout)
    main(open('D-large.in', 'r'), open('D-large-out.txt', 'w'))