outputPath = "/Users/oallbless.ctr/Documents/Google Code Jam 2017/output.out"

with open(outputPath, "w"):
    pass

def output(s):
    #print(s)
    with open(outputPath, "a") as myfile:
        myfile.write(s + "\n")

def getUntidyIndex(s):
    for i in range(len(s) - 1):
        if (s[i] > s[i+1]):
            return i
    return -1

def getTidy(s):
    while True:
        i = getUntidyIndex(s)
        if (i == -1):
            return s
        s[i] = str(int(s[i]) - 1)
        for j in range(i + 1, len(s)):
            s[j] = '9'

t = int(input())
for i in range(1, t+1):
    tidy = getTidy(list(input()))
    output("Case #" + str(i) + ": " + ''.join(tidy if tidy[0] != '0' else tidy[1:]))
