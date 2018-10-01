T = int(raw_input())
for t in range(1, T+1):
    N, K = map(int, raw_input().split())
    if (K+1)%(2**N)==0:
	print "Case #%d: ON" % t
    else:
	print "Case #%d: OFF" % t    
