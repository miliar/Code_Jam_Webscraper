'''
Google Code Jam 2009
Qualification Round
C. Welcome to Code Jam 

@author: Samuel Spiza
'''

def count(string):
    gcj = "welcome to code jam"
    cnt = [[0 for x in range(len(string))] for y in range(len(gcj))]
    for i in range(len(gcj) - 1, -1, -1):
        for j in range(len(string)):
            cnt[i][j] = 0
            if string[j] == gcj[i]:
                if i + 1 == len(gcj):
                    cnt[i][j] = 1
                else:
                    for k in range(1, len(string) - j):
                        cnt[i][j] = (cnt[i][j] + cnt[i + 1][j + k])%10000
    return str(sum(cnt[0])%10000).rjust(4, "0")

#fileName = "C-small-practice.in"
#fileName = "C-small-attempt0.in"
fileName = "C-large.in"
file = open(fileName, "r")

i = 0
lines = []

for line in file:
    if i == 0:
        N = int(line.strip())
    else:
        lines.append(line.strip())
    i = i + 1
file.close()

string = ""
for i in range(len(lines)):
    string = string + "Case #" + str(i + 1) + ": " + str(count(lines[i])) + "\n"
    
file = open(fileName.rsplit(".", 1)[0] + ".out", "w")
file.write(string.strip())
file.close()
