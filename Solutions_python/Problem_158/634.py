table = {"11":"GRRR", "12":"GGRR", "13":"GRRR", "14":"GGRR", "22":"GGRR", "23":"GGGR", "24":"GGRR", "33":"GRGR", "34":"GGGG", "44":"GGRG"}

T = int(input())
for I in range(1, T+1):
    s = raw_input().split()
    X, R, C = int(s[0]), int(s[1]), int(s[2])
    if (R > C):
        R, C = C, R
    if table["" + str(R) + str(C)][X-1] == 'G':
        print("Case #%d: GABRIEL" % I)
    else:
        print("Case #%d: RICHARD" % I)
