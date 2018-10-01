from math import ceil
from math import floor

def check(N, train, user_pos):
    counter = [0 for i in range(N)]
    promote = 0
    for u in user_pos:
        for p in user_pos[u]:
            if counter[p] < train:
                counter[p] += 1
            else:
                t = p - 1
                while t >= 0 and counter[t]>= train:
                    t -= 1
                if t >= 0 and counter[t] < train:
                    counter[t] += 1
                    promote += 1
                else:
                    return False, 0
    return True, promote
f = open('B-small-attempt1.in', 'r')
fo = open('output.txt', 'w')
T = int(f.readline())
for caseID in range(T):
    line = f.readline().strip().split()
    N = int(line[0])
    C = int(line[1])
    M = int(line[2])
    P = []
    B = []
    user_pos = {}
    for i in range(M):
        eles = f.readline().strip().split()
        p = int(eles[0])
        u = int(eles[1])
        P.append(p-1)
        B.append(u)
        if u not in user_pos:
            user_pos[u] = []
        user_pos[u].append(p-1)
    min_train = 0
    for u in user_pos:
        if len(user_pos[u]) > min_train:
            min_train = len(user_pos[u])
    max_train = M
    y=0
    z=0
    while min_train + 2 < max_train:
        train = (min_train+max_train) // 2
        flag, promo = check(N, train, user_pos)
        if not flag:
            min_train = train + 1
        if flag:
            max_train = train - 1
    found = False
    train = max_train
    while train >= min_train:
        flag, promo = check(N, train, user_pos)
        if flag:
            train -= 1
        else:
            train += 1
            y, z = check(N, train, user_pos)
            found = True
            break;
    if not found:
        y, z = check(N, min_train, user_pos)
        train = min_train
    fo.write("Case #{}: {} {}\n".format(caseID+1, train, z))
f.close()
fo.close()