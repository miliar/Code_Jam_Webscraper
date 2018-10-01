def run():
    caseCount = int(input())
    
    for i in range(caseCount):
        case = input().split(' ')
        maxVal = (int(case[0]))
        shyArr = [0]*(maxVal+1)

        shyStr = case[1]
        for j in range(maxVal+1):
            shyArr[j] = int(shyStr[j])

        currentStanders = 0
        standersRequired = 0
        for j in range(maxVal+1):
            if shyArr[j] == 0:
                continue

            if currentStanders < j:
                standersRequired += (j-currentStanders)
                currentStanders = j

            currentStanders += shyArr[j]


        print("Case #%i: %i" % (i+1, standersRequired))


if __name__ == "__main__":
    run()
