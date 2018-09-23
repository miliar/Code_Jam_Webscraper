#Python 3.6
#Jeremiah Gastilo
#Google Code Jam 2017 - Qualifier A Small Source

#functions
def flip(str):
    if str == "+":
        return "-"
    if str == "-":
        return "+"
    return "!"      

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, k = [q for q in input().split(" ")]  # read a list of integers, 2 in this case
    k = int(k)
    step = 0
    for x in range(0,len(n)-(k-1)):
        if n[x] == "-":
            rep = n[:x]
            rep2 = ""
            rep3 = n[x+k:]
            for y in range(k):
                rep2 += flip(n[x+y])
            n = rep+rep2+rep3
            step = step + 1
    m = 0
    for z in range (len(n)-(k-1), len(n)):
        if n[z] == "-":
            m = m + 1
    if m > 0:
        result = "IMPOSSIBLE"
    if m == 0:
        result = str(step)
    print("Case #{}: {}".format(i, result))