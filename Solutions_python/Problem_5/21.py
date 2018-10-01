
# another stupid solution for small input

def Milkshakes():
    N = int(raw_input())
    M = int(raw_input())
    F = []
    for i in range(M):
        s = map(int, raw_input().split())
        T = s[0]
        F.append([])
        for j in range(T):
            F[i].append((s[2 * j + 1] - 1, s[2 * j + 2]))
    best = N + 1
    result = "IMPOSSIBLE"
    for b in range(2**N):
        ok = 0
        for Fi in F:
            for f in Fi:
                bit = 1 << f[0]
                test = bit *  f[1]
                if (b & bit) == test:
                    ok += 1
                    break
        if ok == M:
            count = 0
            r = ""
            for i in range(N):
                malted = b & 1
                r += str(malted) + " "
                count += malted
                b >>= 1
            if count < best:
                best = count
                result = r
    print result

C = int(raw_input())
for testcase in range(C):
    print "Case #%d:" % (testcase + 1),
    Milkshakes()
