import sys

tc = int(raw_input())
idx = 0
for data in sys.stdin:
    idx += 1
    data = data.strip()
    val = int(data)
    num = None
    for id in range(val + 1):
        s = str(id)
        prev = s[0]
        found = True
        for i in range(1, len(s)):
            if s[i] < prev:
                found = False
                break
            else:
                prev = s[i]
        if found:
            num = id
    print "Case #" + str(idx) + ": " + str(num)



