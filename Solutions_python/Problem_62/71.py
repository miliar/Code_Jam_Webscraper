#!/usr/bin/env python

import sys

def cross_wire(A, B):
    if A[0] < B[0] and A[1] > B[1]:
        return True
    if A[0] > B[0] and A[1] < B[1]:
        return True
    return False

def main():
    num = int(sys.stdin.readline().strip())
    for i in range(num):
        wire_num = int(sys.stdin.readline().strip())
        wires = []
        for j in range(wire_num):
            (l, r) = sys.stdin.readline().strip().split()
            wires.append((int(l), int(r)))

        count = 0
        for j in range(wire_num):
            for k in range(wire_num):
                if j == k:
                    continue
                if cross_wire(wires[j], wires[k]):
                    count += 1

        print "Case #%d: %d" % (i+1, count / 2)
if __name__ == '__main__':
    main()
