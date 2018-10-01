def is_tidy(n):
    tidy = True
    if (int(n)) < 10:
        return True
    n.split()
    for i in range(len(n) - 1):
        if int(n[i]) > int(n[i+1]):
            tidy = False
            break
    return tidy


with open('B-small-attempt1.in', 'r') as f:
    cases = int(f.readline())
    for n in range(cases):
        number = f.readline()
        number = str(int(number))
        while not is_tidy(number):
            numberaux = int(number)
            numberaux -= 1
            number = str(numberaux)
        g = open('B-small-attempt1.out', 'a')
        g.write("Case #%s: %s\n" % (n+1, number))
        g.close()




f.close()