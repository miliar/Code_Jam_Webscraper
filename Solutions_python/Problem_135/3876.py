import sys


def __process(str1, str2):
    c = 0
    r = ''
    arr1 = str1.split(' ')
    arr2 = str2.split(' ')

    for e1 in arr1:
        for e2 in arr2:
            if e2 == e1:
                c += 1
                r = e1
                if c > 1:
                    return 'Bad magician!'
                continue
    if c == 1:
        return r
    return 'Volunteer cheated!'


def main(in_path, out_path):
    print 'codejam %d >>> round %s' % (2014, 'a')

    in_file = open(in_path, 'r')
    out_file = open(out_path, 'w')

    # total
    t = int(in_file.readline())

    for i in range(t):
        c1 = int(in_file.readline())
        l1 = [in_file.readline(), in_file.readline(), in_file.readline(), in_file.readline()]

        c2 = int(in_file.readline())
        l2 = [in_file.readline(), in_file.readline(), in_file.readline(), in_file.readline()]

        out_file.write('Case #%d: %s\n' % (i + 1, __process(l1[c1 - 1].strip('\r\n'), l2[c2 - 1].strip('\r\n'))))

    in_file.close()
    out_file.close()


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])