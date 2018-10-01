import sys


def flip(p, k, index):
    p[index:index+k] = [not i for i in p[index:index+k]]


def flipall(p, k):
    count = 0
    for i in range(len(p) - k + 1):
        if not p[i]:
            flip(p, k, i)
            count += 1
    if not all(p[i:i + k]):
        return "Impossible"
    return count


if __name__ == '__main__':

    for arg in sys.argv:
        inputfilename = arg;

    #check if input string is null???

    inputfile = open(inputfilename, 'r')

    outputfile = open(inputfilename + ".out", 'w')
    numberofsets = int(inputfile.readline())

    for m in range(numberofsets):
        p, k = inputfile.readline().rstrip('\r\n').split(' ')
        p = [True if i == '+' else False for i in p]
        print(p)
        k = int(k)
        count = flipall(p, k)

        outputline = "Case #{}: {}\n".format(m+1, count)
        print(outputline)
        outputfile.write(outputline)

