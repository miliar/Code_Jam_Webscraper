import sys
fp = open('input_large')
case_num = int(fp.readline())
for i in range(case_num):
    n, k = [int(x) for x in fp.readline().split()]
    result = ( (k / 2 ** (n - 1)) % 2 == 1) and ((k + 1) % (2 ** (n - 1)) == 0)
    s = ''
    if result:
        s = 'ON'
    else:
        s = 'OFF'
    print "Case #%d: %s" % (i + 1, s)
