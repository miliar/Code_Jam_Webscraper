f= open("B-large.in", 'r')
t = f.readlines()
f.close()

cases = int(t[0])
o = open("3.out", 'w')
for c in range(1, cases+1):
    inp = map(int, t[c].strip().split())
    googlers = inp[0]
    surprise = inp[1]
    p = inp[2]
    score = inp[3:]
    scores = []
    for s in score:
        if s % 3 == 0:
            scores.append((s/3, s/3, s/3, 0))
        elif s % 3== 1:
            scores.append((s/3, s/3, s/3 + 1, 1))
        elif s % 3 == 2:
            scores.append((s/3, s/3 + 1, s/3 + 1, 2))
    count = 0
    remain = 0
    for s in scores:
        if s[2] >= p:
            count += 1
        elif s[2] + 1 >= p:
            if s[3] == 2:
                # 2 is minimum so always work
                remain += 1
            elif s[3] == 1:
				pass
            else:
                # 001
                if s[0] != 0:                
                    remain += 1
    if remain < surprise:
        count += remain
    else:
        count += surprise
    print count
    o.write("Case #" + str(c) + ": " + str(count) + '\n')
            
o.close()
