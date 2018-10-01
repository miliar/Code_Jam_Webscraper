from math import sqrt

def main(filein):
    f = open(filein, "r")
    outname = filein.split(".")[0] + "OUT.txt"
    g = open(outname, "w")

    count = -1
    for line in f:
        count += 1
        if count == 0:
            continue
        newline = "Case #" + str(count) + ": " + code(line) + "\n"
        g.write(newline)
    
    f.close()
    g.close()
    
def code(line):
    if line[-1] == "\n":
        line = line[:-1]
    a,b = line.split(" ")
    a = int(a)
    b = int(b)
    total = 0
    start = int(sqrt(a))
    if start ** 2 < a:
        start += 1
    end = int(sqrt(b))
    if (end + 1) ** 2 <= b:
        end += 1
    while start <= end:
        if palindrome(start):
            if palindrome(start ** 2):
                total += 1
        start += 1
    return str(total)
    
def palindrome(n):
    st = str(n)
    rev = st[::-1]
    return st == rev