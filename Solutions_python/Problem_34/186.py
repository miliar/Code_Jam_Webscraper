file = open("A-large.in")
limits = [int(s) for s in file.next().split(" ")]
words = []
tests = []
for i in range(limits[1]):
    words.append(file.next().strip())
for i in range(limits[2]):
    tests.append(file.next().strip())
file.close()
for i in range(len(tests)):
    chars = [[] for j in range(limits[0])]
    index = 0
    inpar = False
    for c in tests[i]:
        if c == '(':
            inpar = True
        elif c == ')':
            inpar = False
            index += 1
        else:
            chars[index].append(c)
            if not inpar:
                index += 1
    count = 0
    for word in words:
        match = True
        for c in range(limits[0]):
            if chars[c].count(word[c]) == 0:
                match = False
                break
        if match:
            count += 1
    print "Case #%i: %i" % (i + 1, count)
