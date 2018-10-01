#!/usr/bin/env python

import shlex
import string

class GetOutOfLoop1(Exception):
    pass
class GetOutOfLoop2(Exception):
    pass

with open('A-small-1.in', 'r') as inf:
    with open('A-small-1.out', 'w') as outf:
        T = int(inf.readline())
        for i in range (1, (T + 1)):
            try:
                ans = []
                cards1 = []
                cards2 = []
                ans.append(int(inf.readline()))
                for j in range(0, 4):
                    line = shlex.split(inf.readline())
                    temp = []
                    for k in line:
                        temp.append(int(k))
                    cards1.append(temp)
                ans.append(int(inf.readline()))
                for j in range(0, 4):
                    line = shlex.split(inf.readline())
                    temp = []
                    for k in line:
                        temp.append(int(k))
                    cards2.append(temp)
                found = []
                for j in cards1[ans[0] - 1]:
                    try:
                        for k in range(0, 4):
                            l = cards2[k]
                            try:
                                l.index(j)
                                found.append(k + 1)
                                raise GetOutOfLoop1
                            except ValueError:
                                pass
                    except GetOutOfLoop1:
                        pass
                n = 0
                for j in range(0, 4):
                    if found.count(found[j]) == 1:
                        n += 1
                m = 0
                if n == 0:
                    for j in cards1[ans[0] - 1]:
                        try:
                            cards2[ans[1] - 1].index(j)
                        except ValueError:
                            m += 1
                    if m == 4:
                        result = ("Case #", str(i), ": Volunteer cheated!\n")
                        raise GetOutOfLoop2
                    result = ("Case #", str(i), ": Bad magician!\n")
                    raise GetOutOfLoop2
                else:
                    a = elem = 0
                    for j in cards1[ans[0] - 1]:
                        try:
                            elem = cards2[ans[1] - 1][cards2[ans[1] - 1].index(j)]
                            a += 1
                            if a > 1:
                                result = ("Case #", str(i), ": Bad magician!\n")
                                raise GetOutOfLoop2
                        except ValueError:
                            pass
                    if a == 1:
                        result = ("Case #", str(i), ": ", str(elem), "\n")
                        raise GetOutOfLoop2
                    result = ("Case #", str(i), ": Volunteer cheated!\n")
                    raise GetOutOfLoop2
            except GetOutOfLoop2:
                pass
            outf.write(string.join(result, ""))
