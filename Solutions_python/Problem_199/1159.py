def flip(s):
    if s == "-":
        s = "+"
    else:
        s = "-"
    return s

def flipper(s, k):
    length = len(s)
    s = list(s)
    ans = 0

    for i in range(length+1-k):
        if s[i] == "-":
            ans += 1
            for j in range(k):
                s[i+j] = flip(s[i+j])
    st = "".join(s)
    if "-" in s:
        ans = "IMPOSSIBLE"
    return ans

in_f = open("i.txt", 'r')
ou_f = open("o.txt", 'w')

T = int(in_f.readline())
for i in range(T):
    s , k = in_f.readline().split(" ")
    k = int(k)
    out = flipper(s, k)

    j = "Case #" + str(i+1) +": " + str(out) + "\n"
    ou_f.write(j)
in_f.close()
ou_f.close()