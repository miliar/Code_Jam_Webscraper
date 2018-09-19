fp = open('third.in', 'r')
cases = int(fp.readline().strip())

def indexes(string, l):
    result = []
    for i in range(len(string)):
        if string[i] == l:
            result.append(i)
    return result

string = "welcome to code jam"

for x in range(cases):
    result = [0] * len(string)
    text = fp.readline().strip()
    for l in text:
        for i in indexes(string, l):
            if i == 0:
                result[0] += 1
            else:
                result[i] += result[i - 1]
    #print result[-1]
    print 'Case #%d: %04d' % (x+1, result[-1] % 10000)
