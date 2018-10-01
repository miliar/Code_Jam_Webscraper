
def check(n):
    i = numero_digitos(n)
    flag = 1
    while (i > 1):
        z = n % 10
        n = n // 10
        y = n % 10
        if (z < y):
            flag = 0
            break
        i -= 1
    if (flag == 1):
        return True
    else:
        return False

def bigger(x):
    if check(x):
        return x
    else:
        return bigger(x-1)

        
def numero_digitos (x):
    if x < 10:
        return 1
    else:
        return 1 + numero_digitos (x // 10)

def execute(nome):
    file = open(nome, 'r')
    n = eval(file.readline())
    i = 1
    out = open('out.txt', 'w')
    while (i <= n):
        z = eval(file.readline())
        if ((z // 10) == 0):
            out.write ("Case #" + str(i) + ": " + str(z) + "\n")
        else:
            if (check(z)):
                out.write ("Case #" + str(i) + ": " + str(z) + "\n")
            else:
                out.write ("Case #" + str(i) + ": " + str(bigger(z-1)) + "\n")
        i += 1
    out.close
