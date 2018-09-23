def test(n):
    lista = range(n + 1)[::-1]
    for num in lista:
        if check(num):
            return num


def check(num):
    listn = [int(i) for i in str(num)]
    previous = listn[0]
    for n in listn[1:]:
        if n >= previous:
            previous = n
        else:
            return False
    return True



t = int(input())
for i in range(1, t + 1):
    n = int(input())
    print("Case #{}: {}".format(i, test(n)))
