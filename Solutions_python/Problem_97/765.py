f = open("data.txt", 'r')
g = open("data1.txt", 'w')

def cycles(x):
    s = str(x)
    cyclelist = []
    for i in range(1, len(s)):
        cyclelist.append(int(s[i:] + s[:i]))
    return set(cyclelist)

line = f.readline()
n = int(line)
for i in range(1, n+1):
    line = f.readline()
    (a, b) = (int(x) for x in line.split())
    result = 0
    for x in range(a, b):
        for y in cycles(x):
            if x < y <= b:
                result += 1
    string = "Case #" + str(i) + ": " + str(result) + '\n'
    g.write(string)

f.close()
g.close()
    
