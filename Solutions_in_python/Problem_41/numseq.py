
def embiggen(s):
    i = len(s)-1
    prev = "0"
    while i>=0:
        nextdigit = s[i]
        #print "{0}<{1}? {2}".format(nextdigit, prev, nextdigit<prev)
        if nextdigit<prev:
            left = s[:i]
            middle = s[i]
            right = s[i+1:]
            nextmiddle = sorted(r for r in right if r>middle)[0]
            rightchars = sorted(right+middle)
            rightchars.remove(nextmiddle)
            nextright = "".join(rightchars)
            return left+nextmiddle+nextright
        prev = nextdigit
        i-=1
    zeros = "".join(ch for ch in s if ch == "0")
    sortedchars = sorted(ch for ch in s if ch != "0")
    sortedchars.insert(1,"0"+zeros)
    return "".join(sortedchars)

cases = int(raw_input().strip())
for i in xrange(cases):
    print "Case #{0}: {1}".format(
        i+1, embiggen(raw_input().strip()))
