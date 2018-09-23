def dosomething():
    print("myname")



def number(z):
    while True:
        x = str(z)
        if all(x[i] <= x[i+1] for i in range(len(x)-1)):
            return z
        else:
            z = z-1


for i in range(1, int(input())+1):
    n = int(input())
    print("Case #{}: {}".format(i, number(n)))


