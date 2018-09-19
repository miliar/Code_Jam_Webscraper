import re
def matchString (pattern, string):
    pattern = pattern.replace('(', '[').replace(')', ']')
    r = re.compile (pattern)
    return bool(r.match(string))
def inputParser (string):
    lines = re.compile('\n').split (string)
    l, d, n = [int(i) for i in re.compile(' ').split(lines.pop(0))]
    words = []
    for i in range(d):
        words.append(lines.pop(0))
    outString = ""
    for i in range(n):
        pattern = lines.pop(0)
        testCount = 0
        for word in words:
            if matchString (pattern, word):
                testCount+=1
        outString += 'Case #%d: %d\n' % (i+1, testCount)
    return outString
ouf = open ('output.out', 'w')
inf = open (input('Enter input file:'), 'r')
ouf.write(inputParser(inf.read()))
ouf.close()
inf.close()
