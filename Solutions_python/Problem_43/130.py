fn = "A-large"
input = open(fn+".in")
output = open(fn + ".out", "w")

for case in range (1, int(input.readline()) +1):
    v = []
    max = 2
    i = 1;
    map = []
    for y in range(26 +10):
        map.append(None)
    ic = 0
    next = 1
    for ch in input.readline():
        if ch == '\n': break
        if ch >='0' and ch <= '9':
            k = ord(ch)-ord('0')
        else:
            k = ord(ch) - ord('a') + 10
        if map[k] is None:
            en = next
            if next==1:
                next = 0
            elif next==0:
                next = 2
            else:
                next += 1
            map[k] = en
        else:
            en = map[k]
        v.append(en)
    v.reverse()
    num = 0
    p = 1
    if next < 2: next = 2
    for t in v:
        num += t * p
        p *= next
    output.write("Case #" + str(case) + ": " + str(num) + "\n")
    
    