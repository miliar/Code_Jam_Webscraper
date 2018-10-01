def main():
    f = open('A-large-out.txt', 'w')
    input = open('A-large.in', 'r')
    n = int(input.readline().strip('\n'))
    for i in xrange(0, n):
        case = input.readline().strip('\n')
        maxS = int(case.split()[0])
        array = []
        for j in case.split()[1]:
            array.append(int(j))

        neededFriends = findMinFriends(maxS, array)
        f.write('Case #' + str(i + 1) + ": " + str(neededFriends) + '\n')

def findMinFriends(maxS, array):
    currentCount = 0
    neededFriends = 0
    for index in xrange(0, len(array)):
        if index > currentCount:
            neededFriends += index - currentCount
            currentCount += index - currentCount
        currentCount += array[index]
        #print currentCount

    return neededFriends

if __name__ == "__main__":
    main()
