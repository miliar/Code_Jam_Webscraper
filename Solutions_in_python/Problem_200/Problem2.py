def first_index(s):
    for i in range(1,len(s)):
        if int(s[i]) < int(s[i-1]):
            return i
    return -1
def get_tidy(s):
    x = first_index(s)
    n = 0
    if x >= 0:
        while x >=0:
            tidy = s[:x-1] + str(int(s[x-1])-1) + '9'*(len(s)-x)
            x = first_index(tidy)
            n = n + 1
        return str(int(tidy))
    else:
        return s    


f = open('input.txt')
o = open('output.txt','w')
T = int(f.readline().strip())
for i in range(T):
    s = str(f.readline().strip())
    print("Case #" + str(i+1) + ": " + get_tidy(s),file = o)
o.close()
f.close()


