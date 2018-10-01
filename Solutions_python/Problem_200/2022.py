def check_nonDec(number):
    strn = str(number)

    digits = [int(dig) for dig in strn]
    if digits == sorted(digits):
        return True

    return False

T = int(raw_input())

f = open('output.txt', 'w')


for _ in range(1,T+1):
    n = int(raw_input())
    # print n
    while not check_nonDec(n):
        n -= 1

    print n


    f.write("Case #" + str(_) + ": " + str(n) + "\n")






f.close()