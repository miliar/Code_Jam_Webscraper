

def flip(pancakes, i, y):
    for j in range(i, y+1):
        if pancakes[j] == '+':
            pancakes[j] = '-'
        elif pancakes[j] == '-':
            pancakes[j] = '+'

def solve(pancakes, flipper):
    result = 0
    i = 0;
    size = len(pancakes)
    for i in range(0, size-flipper+1):
        if pancakes[i] == '-':
            result = result + 1
            flip(pancakes, i, i + flipper-1)
    return result

def check(pancakes, flipper):
    size = len(pancakes)
    for i in range(size-1, size-1-flipper,-1):
        if (pancakes[i] == '-'):
            return False
    return True

if __name__ == "__main__":

    open('output.txt', 'w').close()

    import fileinput
    f = fileinput.input('A-large.in')

    T = int(f.readline())
    for case in range(1,T+1):
        parse = list()
        parse = f.readline().split()
        pancakes = list(parse[0])
        flipper = int(parse[1])

        result = solve(pancakes, flipper)
        valid = check(pancakes, flipper)

        answer = ''
        if valid == True:
            answer = str(result)
        else:
            answer = 'IMPOSSIBLE'

        fileoutput = open('A-large.out', 'a+')
        print("Case #{0}: {1}".format(case, answer))
        print >> fileoutput, "Case #{0}: {1}".format(case, answer)
