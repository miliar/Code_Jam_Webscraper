
def SnapperChain():
    N, K = map(int, raw_input().split())
    if (K+1) & ((1<<N)-1):
        print "OFF"
    else:
        print "ON"

#---------------------------------------------------------------

T = int(raw_input())
for testcase in range(T):
    print "Case #%d:" % (testcase+1),
    SnapperChain()
