from math import *

def explode(s, c):
    t = []
    s += c;
    p = 0;
    for i in range(len(s)):
        if (s[i] == c or s[i] == "\n") and s[p:i] != "" and s[p:i] != "\n":
            t.append(s[p:i])
            p = i + 1
    return t

def palindrome(n):
    return str(n) == str(n)[::-1]

def check(n):
    r = int(sqrt(n))
    return palindrome(r) and palindrome(n) and r**2 == n

def solveCase(line):
    x = explode(line, ' ')
    ans = 0
    for i in range(int(x[0]), int(x[1]) + 1):
        if check(i): ans += 1
    return ans

def process(data):
    out = ""
    for i in range(1, len(data)):
        if i > 1: out += '\n'
        out += "Case #" + str(i) + ": "
        out += str(solveCase(data[i]))
    return out

def main(fn):
    iFile = open(fn + ".in", "r")
    oFile = open(fn + ".out", "w")
    print("Files opened.")

    data = []
    while True:
        line = iFile.readline()
        if not line: break
        data.append(line)

    out = process(data)
    print("Calculations complete. Outputting to file.")
    oFile.writelines(out)
    print("Output complete.")
    iFile.close()
    oFile.close()
    print("Files closed.")

main("small")
