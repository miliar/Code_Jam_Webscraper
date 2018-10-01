def isTidy(n):
    if n < 10:
        return True
    ones = n % 10
    newN = n // 10
    tens = newN % 10
    if ones < tens:
        return False
    else:
        return isTidy(newN)

input()

counter = 0

while True:
    counter += 1
    try:
        line = input()
    except EOFError:
        break
    if not line:
        break
    i = int(line)
    for curr in range(i, 0, -1):
        if(isTidy(curr)):
            print("Case #{}: {}".format(counter, curr))
            break

