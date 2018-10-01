from __future__ import print_function


def input_grid(n):
    acc = None
    for i in xrange(4):
        line = raw_input()
        if i + 1 == n:
            acc = set(int(v) for v in line.split())

    return acc


if __name__ == "__main__":
    t = int(raw_input())
    for i in xrange(1, t + 1):
        n1 = int(raw_input())
        line1 = input_grid(n1)
        n2 = int(raw_input())
        line2 = input_grid(n2)
        common = line1 & line2
        print("Case #{0}:".format(i), end=" ")
        if len(common) == 1:
            print(list(common)[0])
        elif not common:
            print("Volunteer cheated!")
        else:
            print("Bad magician!")
