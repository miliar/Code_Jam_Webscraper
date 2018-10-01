#!/usr/bin/env python
input_file = "input.txt"
output_file = "output.txt"


def read():
    a = f.read(1)
    while ((a == " ") or (a == "\n")):
        a = f.read(1)
        if not a:
            print "End of file"
            break

    return int(a)


def read2():
    a = f.read(3)
    while ((a == " ") or (a == "\n")):
        a = f.read(1)
        if not a:
            print "End of file"
            break

    return int(a)

if __name__ == '__main__':
    with open(input_file) as f:
        fo = open(output_file, 'w')
        T = read2()
        for i in xrange(1, T + 1):
            fo.write("Case #%d: " % i)
            N = read()
            fans = 0
            temp = read()
            total = temp
            for j in xrange(1, N + 1):
                temp = read()
                if (j > total and temp != 0):
                    fans += (j - total)
                    total += (j - total)
                total += temp
            fo.write("%d\n" % fans)
