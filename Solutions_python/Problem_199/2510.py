

def processMany():
    with open("/Users/ChesterAiGo/Desktop/ASmall.txt") as Doc:
        lines = [x.strip() for x in Doc.readlines()]

    for i in range(len(lines)):
        print("Case #{0}: {1}".format(i + 1, processOne(lines[i])))


def processOne(tc):
        input = tc.split(" ")

        if("-" not in input[0]):
            return 0

        K = int(input[1])

        intArr = []
        for i in input[0]:
            if(i == '-'):
                intArr.append(-1)
            else:
                intArr.append(1)


        counter = 0

        while(-1 in intArr):

            firstMinus = intArr.index(-1)
            if(firstMinus + K > len(intArr)):
                return "IMPOSSIBLE"

            for i in range(firstMinus, firstMinus + K):
                intArr[i] *= -1

            counter += 1
            # print(intArr)

        return str(counter)



processMany()









