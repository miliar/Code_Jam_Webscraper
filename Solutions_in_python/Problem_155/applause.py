

def readFile(filename):
    with open(filename, 'r') as myfile:
        # First line is the smax
        text = myfile.readline()[:-1]#
        i=1
        for line in myfile:
            # Read the line in a list
            line = line[:-1]
            # Give the line without \n
            L = lineToList(line)
            # solve the problem
            nb = solveApplause(L)
            print("Case #{}: {}".format(i, nb))
            i += 1


def lineToList(line):
    for i in range(len(line)):
        if line[i] == ' ':
            n = i+1
    numbers = line[n:]
    l = []
    for e in numbers:
        l.append(int(e))
    return l


def solveApplause(people):
    res = 0
    applausers = 0
    for (i, shy_i) in enumerate(people):
        if i <= applausers:
            applausers += shy_i
        else:
            res += i - applausers
            applausers = i + shy_i
    return res


if __name__ == "__main__":
    filename = "A-small-attempt2.in"
    filename = "A-large.in"
    readFile(filename)
    #l = [0, 6, 4, 3, 5, 1]
    #n =solveApplause(l)
    #print(l,n)
