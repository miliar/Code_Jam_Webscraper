def isTidy(number):
    num = list(str(number))
    for n in range(len(num)):
        num[n] = int(num[n])
    original = num.copy()
    num.sort()
    if original == num:
        return True
    else:
        return False

cases = int(input())
for case in range(0,cases):
    number = int(input())
    lowest = number
    if (isTidy(lowest)):
        print("Case #{}: ".format(str(case + 1)) + str(lowest))
    else:
        while (lowest >= 1):
            if (isTidy(lowest)):
                print("Case #{}: ".format(str(case + 1)) + str(lowest))
                break
            else:
                lowest = lowest - 1