import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
t = int(raw_input())
for i in range(t):
    n,p = raw_input().strip().split()
    s = [int(c) for c in p]
    standing_so_far = 0
    extra_audience = 0
    for j in range(int(n)+1):
        if j>standing_so_far:
            extra_audience += (j-standing_so_far)
            standing_so_far = j
        standing_so_far += s[j]
    print "Case #%d: %d" % (i+1, extra_audience)
