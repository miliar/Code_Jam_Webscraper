f = open("input.txt", "r")
ans = open("ans.txt", "w")

def is_tidy(num):
    num = str(num)
    for i in range(len(num)-1):
        if num[i] > num[i+1]:
            return False
    return True

data = f.readlines()
t = int(data[0])
for x in range(t):
    n = int(data[x+1])
    if is_tidy(n):
        print n
        ans.write("Case #{}: {}" .format(x+1,str(n) + "\n"))
    else:
        while not is_tidy(n):
            if is_tidy(n):
                break
            else:
                l = []
                n = str(n)
                for i in range(len(n)-1):
                    if n[i] <= n[i+1]:
                        l.append(n[i])
                    else:
                        if n[i] == 0:
                            l.append(str(9))
                        else:
                            l.append(str(int(n[i])-1))
                        break
                n = int("".join(l + ["9"] * (len(n)-len(l))))
        print n
        ans.write("Case #{}: {}" .format(x+1,str(n) + "\n"))