# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    dataInput = input().split()
    dataList = list(dataInput[0])
    dataInt = int(dataInput[1])
    count = 0 # Count of ations
    for j in range(0, (len(dataList) - dataInt + 1)):
        if (dataList[j] == "-"):
            count = count + 1
            for k in range(j, j + dataInt):
                if dataList[k] == "-": 
                    dataList[k] = "+"
                elif dataList[k] == "+":
                    dataList[k] = "-"
    for j2 in range(len(dataList) - dataInt + 1, len(dataList)):
        if (dataList[j2] == "-"): 
            count = "IMPOSSIBLE"
    print("Case #{}: {}".format(i, count))
