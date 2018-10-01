from bitarray import bitarray

def greedy(case):
    flips_needed = 0
    line = input().split()
    k = int(line[1])
    s = list(line[0])
    for i in range(len(s) - k + 1):
        if s[i] == "-":
            flips_needed += 1
            for j in range(k):
                if s[i+j] == "+":
                    s[i + j] = "-"
                else:
                    s[i + j] = "+"

    for i in range(k):
        if s[-i] == "-":
            print("Case #" + str(case) + ": IMPOSSIBLE")
            return
    print("Case #" + str(case) + ": " + str(flips_needed))

n = int(input())
for i in range(n):
    greedy(i+1)