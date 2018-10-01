t = input()
t = int(t)
for i in range(0, t):
    entry = input()
    n = list(entry)
    x = 0
    f = 0
    while x < len(n):
        if int(n[x]) != int(n[x - 1]):
            f = x
        if x + 1 >= len(n):
            break
        if int(n[x]) > int(n[x + 1]):
            break
        x = x + 1
    #print(str(x))
    if x == (len(n) - 1):
        n = int("".join(n))
        print("Case #" + str(i + 1) + ": " + str(n))
    else:
        n[f] = str(int(n[f]) - 1)
        for j in range(f + 1, len(n)):
            n[j] = '9'
        n = int("".join(n))
        print("Case #" + str(i + 1) + ": " + str(n))
