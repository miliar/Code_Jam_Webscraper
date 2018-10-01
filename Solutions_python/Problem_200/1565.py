f = open("B-large.in","r")
number = int(f.readline())

def tidy(s):
    if len(s) == 1:
        return s
    s = list(s.strip())
    i = 0
    while(i<len(s) and i+1<len(s) and s[i]<=s[i+1]):
        i += 1
    if i == len(s) -1:
        return "".join(s)
    if s[i] != "0":
        s[i] = str(int(s[i])-1)
        for j in range(i+1,len(s)):
            s[j] = "9"
    else:
        s[i-1] = str(int(s[i-1]-1))
        for j in range(i,len(s)):
            s[j] = "9"
    return "".join(s).strip("0")

count = 0
for i in range(number):
    s= str(f.readline())
    temp = tidy(s)
    while "".join(sorted(temp)) != temp:
        temp = tidy(temp)
    print("Case #"+str(i+1)+": "+temp)
    if "".join(sorted(temp))!=temp:
       count += 1
print(count)

