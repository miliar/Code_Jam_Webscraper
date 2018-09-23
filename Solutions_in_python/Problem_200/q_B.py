
# -*- coding: UTF-8 -*-

import sys


def debug(msg):
    sys.stderr.write(msg)
    sys.stderr.flush()
    

def solve(s):
    #debug(str(ps))
    #debug(str(k))

    pos = -1
    for ind in range(1, len(s)):
        cur = int(s[ind])
        prev = int(s[ind-1])

        if cur < prev:
            pos = 0
            for r_ind in range(ind - 1, 0, -1):
                cur = prev - 1
                prev = int(s[r_ind-1])

                if cur >= prev:
                    pos = r_ind
                    break
            break

    if pos < 0:
        return s

    ans = list(s)
    for ind in range(len(ans)):
        if ind == pos:
            ans[ind] = str(int(ans[ind])-1)
        elif ind > pos:
            ans[ind] = '9'

    debug("ans:")
    debug(str(ans))
    debug("\n")

    if ans[0] == '0':
        return "".join(ans[1:])

    return "".join(ans)


#input_file = "sample.in"
#input_file = "B-small-attempt0.in"
input_file = "B-large.in"
f = open(input_file)
sys.stdout = open(input_file.replace(".in", ".txt"), 'w')
tc_num = int(f.readline().rstrip())

for tc in range(tc_num):
    l = f.readline().rstrip()
    ans = solve(l)
    print("Case #" + str(tc+1) + ": " + ans)

