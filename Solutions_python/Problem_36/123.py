word  = "welcome to code jam"
N = int(raw_input())
for C in xrange(N):
    phrase  = raw_input()
    lookup = [0] * len(word)
    for i in phrase:
        for  j in xrange(len(word)):
            if i == word[j]:
                if j == 0:
		     lookup[j] += 1
                     lookup[j] %= 10000
		else:
 		     lookup[j] += lookup[j-1]
                     lookup[j] %= 10000
    print "Case #%d: %04d" % (C+1,lookup[-1])
