cases = int(input())
for t in range(1,cases+1):
    line = input().split(' ')[1]
    p = [int(c) for c in line]
    needed = 0
    have = p[0]
    for i in range(1, len(p)):
        if have < i:
            needed += i - have
            have = i
        have += p[i]
    print ('Case #%d: %d' % (t, needed))
