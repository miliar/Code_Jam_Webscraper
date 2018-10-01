#! /usr/bin/python
import sets

def readInt():
    return int(raw_input())

def readInts():
    return map(int, raw_input().split())


def main():
    t = readInt()
    for i in range(t):
        op = 'Case #' + str(i+1) + ': '
        r1 = readInt()
        for i1 in range(4):
            if i1 == r1-1:
                g1 = set(readInts())
            else:
                raw_input()
        r2 = readInt()
        for i1 in range(4):
            if i1 == r2-1:
                g2 = set(readInts())
            else:
                raw_input()
        c = g1.intersection(g2)
        if len(c) == 1:
            op = op + str(c.pop())
        elif len(c) == 0:
            op = op + 'Volunteer cheated!'
        else:
            op = op + 'Bad magician!'
        print op

if __name__ == '__main__':
    main()
