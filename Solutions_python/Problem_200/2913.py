import sys
import re


inf = sys.stdin
outf = sys.stdout


def do_step(arr):
    # for i in range(len(arr)):
    #     arr[i] = 1
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            arr[i] -= 1
            for j in range(i + 1, len(arr)):
                arr[j] = 9
            break

def is_correct(arr):
    if not arr:
        return True
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def to_str(arr):
    first = True
    res = ''
    for i in arr:
        if i == 0 and first:
            continue
        res += str(i)
        first = False
    return res

def handle_case(case_num):
    arr = map(int, inf.readline().strip())
    while not is_correct(arr):
        do_step(arr)
    case_str = 'Case #{0}: {1}'.format(case_num, to_str(arr))
    print >>outf, case_str


def main():
    if len(sys.argv) > 1:
        global inf
        inf = open(sys.argv[1])
    if len(sys.argv) > 2:
        global outf
        outf = open(sys.argv[2], 'w')

    T = int(inf.readline().strip())
    for case_num in xrange(1, T+1):
        handle_case(case_num)

    if inf != sys.stdin:
        inf.close()
    if outf != sys.stdout:
        outf.close()


if __name__ == '__main__':
    main()
