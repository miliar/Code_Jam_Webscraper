def readInput(path):
    cases = []
    with open(path, mode='r') as f:
        numCases = f.readline().strip()
        cases = []

        while True:
            line = f.readline().strip().split(' ')
            if len(line)<5:
                break
            N, R, O, Y, G, B, V = line



            cases.append((R, O, Y, G, B, V))


    return numCases, cases


def printSolutions(solutions, name):
    with open(name, mode='w') as f:
        case = 0
        for solution in solutions:
            case+=1
            f.writelines("Case #"+str(case)+": "+solution+"\n")


def verify(string):
    if string[0] == string[-1]:
        return 'IMPOSSIBLE'

    prev = ''
    for i in string:
        if prev == i:
            return 'IMPOSSIBLE'
        else:
            prev = i

    return string


def arrivalTime(destination, position, speed):
    distance = destination - position
    time = distance / speed
    return time

numCases, cases = readInput("Input")
solution = []

for R, O, Y, G, B, V in cases:
    horses = {'R':int(R), 'Y':int(Y), 'B':int(B)}
    sort = sorted(horses.items(), key=lambda x: x[1])
    maximum = sort[2][0]
    amount = sort[2][0]

    N = int(R) + int(Y) + int(B)
    string = ''
    previous = ''

    for i in range(N):

        if horses[maximum]>0 and previous != maximum:
            place = maximum
        else:
            sort = sorted(horses.items(), key=lambda x: x[1])
            place = sort[2][0]
            if place == previous:
                place = sort[1][0]

        previous=place
        string += place
        horses[place] -= 1

    print (string + "-" +verify(string))
    solution.append(verify(string))


printSolutions(solution, "Output")
