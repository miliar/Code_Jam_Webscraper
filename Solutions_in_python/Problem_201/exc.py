def main(n, k):
    steps = 0
    seg = [[1, n]]
    while True:
        new_seg = dict()
        s = seg.pop(0)
        #print(s, steps, 1)

        steps += s[0]
        if s[1] == 1:
            pass
        elif s[1] == 2:
            new_seg[1] = s[0]
        else:
            if s[1] % 2 == 1:
                new_seg[s[1] // 2] = s[0] * 2
            else:
                new_seg[s[1] // 2 - 1] = s[0]
                new_seg[s[1] // 2] = s[0]

        #print(steps, 3, steps, k, steps >= k)
        if steps >= k:
            if s[1] % 2 == 1:
                return str(s[1] // 2) + " " + str(s[1] // 2)
            else:
                return str(s[1] // 2) + " " + str(s[1] // 2 - 1)
        else:
            if len(seg) > 0:
                s = seg.pop(0)
                #print(s, steps, 2)

                steps += s[0]
                if s[1] == 1:
                    pass
                elif s[1] == 2:
                    if 1 in new_seg:
                        new_seg[1] += s[0]
                    else:
                        new_seg[1] = s[0]
                else:
                    if s[1] % 2 == 1:
                        if s[1] // 2 in new_seg:
                            new_seg[s[1] // 2] += s[0] * 2
                        else:
                            new_seg[s[1] // 2] = s[0] * 2
                    else:
                        if s[1] // 2 - 1 in new_seg:
                            new_seg[s[1] // 2 - 1] += s[0]
                        else:
                            new_seg[s[1] // 2 - 1] = s[0]
                        if s[1] // 2 in new_seg:
                            new_seg[s[1] // 2] += s[0]
                        else:
                            new_seg[s[1] // 2] = s[0]
                if steps >= k:
                    if s[1] % 2 == 1:
                        return str(s[1] // 2) + " " + str(s[1] // 2)
                    else:
                        return str(s[1] // 2) + " " + str(s[1] // 2 - 1)

        for t in new_seg:
            seg.append([new_seg[t], t])
        if len(seg) > 1 and seg[0][1] < seg[1][1]:
            seg[0], seg[1] = seg[1], seg[0]

inf = open("in.txt", "r")
ouf = open("out.txt", "w")
            
t = int(inf.readline())
for cs in range(1, t + 1):
    n, k = map(int, inf.readline().split())
    ouf.write("Case #" + str(cs) + ": " + main(n, k) + "\n")

inf.close()
ouf.close()
