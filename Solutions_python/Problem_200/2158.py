def number(x):
    while True:
        n = list(str(x))
        if all(n[i] <= n[i+1] for i in range(len(n)-1)):
            return x
        else:
            for y in range(len(n)-2):
                if n[y] > n[y+1]:
                    for z in range(y+1, len(n)-1):
                        n[z] = "0"
                    break
            return number(int("".join(n))-1)


for x in range(1, int(input())+1):
    n = int(input())
    print("Case #{}: {}".format(x, number(n)))
