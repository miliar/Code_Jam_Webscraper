def check(n):
    l = list(n[::-1])
    for i in range(0, len(l) - 1):
        if l[i] >= l[i + 1]:
            continue
        else:
            return False
    return True


for i in range(int(input())):
    n = int(input())
    while 1:
        if check(str(n)):
            print('Case #' + str(i + 1) + ': ' + str(n))
            break
        else:
            n -= 1
