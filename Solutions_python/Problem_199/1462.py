f = open("A-large.in","r")
number = int(f.readline())

def countnumber(s, k):
    count = 0
    s = list(s)
    for i in range(len(s) - k + 1):
        if s[i] == "-":
            for j in range(i, i + k):
                if s[j] == "+":
                    s[j] = "-"
                else:
                    s[j] = "+"
            count += 1

    for i in range(len(s) - k+1, len(s)):
        if s[i] == "-":
            return "IMPOSSIBLE"
    return count

for i in range(number):
    s= f.readline()
    s = s.split()
    temp = s[0]
    k = int(s[1])
    print("Case #"+str(i+1)+": "+str(countnumber(temp, k)))

