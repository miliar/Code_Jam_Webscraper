import sys


def main(in_stream, out_stream):
    t = int(in_stream.readline())
    for tc in range(t):
        fraction = in_stream.readline()
        p, _, q = fraction.partition('/')
        p = int(p)
        q = int(q)
        b = 1
        mn = "impossible"
        out_stream.write("Case #%d: " % (tc + 1))
        for i in range(40):
            if q % 2 != 0:
                p *= 2
                q *= 2
            if p >= q / 2:
                p -= q / 2
                if mn == "impossible":
                    mn = i + 1
            q /= 2
        if not p:
            out_stream.write("{}\n".format(mn))
        else:
            out_stream.write("impossible\n")


if __name__ == '__main__':
    # main(sys.stdin, sys.stdout)
    main(open("A-large.in", "r"), open("A-large-output.txt", "w"))