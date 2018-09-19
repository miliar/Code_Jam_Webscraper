from __future__ import print_function, division

import sys

infile = open(sys.argv[1])
outfiles = (sys.stdout, open(sys.argv[2], 'w'))

def read_in(infile):
    content = []
    data = infile.readlines()
    amount = int(data[0])
    print('amount:', amount)
    for idx in xrange(1, amount*10+1, 10):
        n1 = data[idx]
        n2 = data[idx + 5]
        array1 = data[idx + 1: idx + 5]
        array2 = data[idx + 6: idx + 10]
        s1 = set([int(s) for s in array1[int(n1)-1].split()])
        s2 = set([int(s) for s in array2[int(n2)-1].split()])

        intersect = s1.intersection(s2)
        l = len(intersect)

        if l == 0:
            content.append("Volunteer cheated!")
        elif l == 1:
            content.append('{0}'.format(intersect.pop()))
        else:
            content.append("Bad magician!")

    assert amount == len(content)
    return content


def do_output(number, output, outfiles):
    for f in outfiles:
        print('Case #%d:' % number, output, file=f)


def main():
    for i, content in enumerate(read_in(infile)):
        do_output(i+1, do_task(content), outfiles)


def do_task(content):
    return content

if __name__ == '__main__':
    main()
