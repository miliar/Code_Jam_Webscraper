from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())
    for pb_i in xrange(n):
        # Solve problem i
        row_1 = int(raw_input())
        tab_1 = [[int(_) for _ in raw_input().split()] for _ in xrange(4)]
        d1 = tab_1[row_1-1]
        row_2 = int(raw_input())
        tab_2 = [[int(_) for _ in raw_input().split()] for _ in xrange(4)]
        d2 = tab_2[row_2-1]
        d3 = []
        for i in d1:
            if i in d2:
                d3.append(i)
        if len(d3) == 1:
            print("Case #{}: {}".format(pb_i+1, d3[0]))
        elif len(d3) == 0:
            print("Case #{}: {}".format(pb_i+1, "Volunteer cheated!"))
        else:
            print("Case #{}: {}".format(pb_i+1, "Bad magician!"))
