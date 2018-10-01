def check(n):
    l = list(n)
    i = 0
    while i < len(l) - 1:
        if int(l[i]) > int(l[i+1]):
            return False
        i += 1
    return True

def tidy(n):
    if check(n):
        return n
    else:
        return tidy(str(int(n)-1))

t = int(input())
n = 1
while n <= t:
    num = input()
    ti = tidy(num)
    print('Case #' + str(n) + ': ' + ti)
    n += 1
