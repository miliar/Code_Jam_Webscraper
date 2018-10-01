T = int(raw_input())

for t in range(T):
    N, s = raw_input().split()
    N = int(N)
    s_ = map(int, s)
    standing = 0
    friends = 0
    for n in range(N+1):
        if standing + friends >= N:
            break
        if s_[n] != 0:
            if standing + friends >= n:
                standing += s_[n]
            else:
                friends += n - (standing + friends)
                standing += s_[n]

    print "Case #" + str(t+1) + ": " + str(friends)

