def solve(num):   
    while True:
        checkTiny = True
        textTiny = str(num)
        if len(textTiny) == 1:
            break
        index = len(textTiny) - 1
        for i in reversed(range(1, len(textTiny))):
            if int(textTiny[i]) < int(textTiny[i-1]):
                checkTiny = False
                break
        if checkTiny == True:
            break
        else:
            textTiny = list(textTiny)
            for i in reversed(range(1, len(textTiny))):
                if int(textTiny[i]) < int(textTiny[i-1]):
                    for j in range(i, len(textTiny)):
                        textTiny[j] = '9'
                    textTiny[i] = '9'
                    textTiny[i-1] = str(int(textTiny[i-1]) - 1)
            num = int("".join(textTiny))
    return num

if __name__ == "__main__":
    import fileinput
    f = fileinput.input()
    T = int(f.readline())
    for case in range(1,T+1):
        NUMBER = int(f.readline())
        answer = solve(NUMBER)
        print("Case #{0}: {1}".format(case, answer))