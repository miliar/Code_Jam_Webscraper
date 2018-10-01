t = int(input())
s = []
for i in range(1, t + 1):
    s.append(str(input()))
for i in range(0, len(s)):
    if (int(s[i]) < 10):
        print('Case #'+ str(i+1) + ': ' + s[i])
    else:
        strList = list(s[i])
        digInd = 0
        while (digInd < len(strList)-1):
            if(int(strList[digInd]) < int(strList[digInd + 1])):
                digInd = digInd + 1
            elif(int(strList[digInd]) == int(strList[digInd + 1]) and digInd < len(strList) - 2):
                if (int(strList[digInd]) > int(strList[digInd + 2])):
                    break
                else:
                    digInd = digInd + 1
            elif(int(strList[digInd]) == int(strList[digInd + 1])):
                digInd = digInd + 1
            else:
                break
        if (digInd == len(strList) - 1):
            print('Case #'+ str(i+1) + ': ' + s[i])
        else:
            strList[digInd] = str(int(strList[digInd]) - 1)
            for j in range(digInd + 1, len(strList)):
                strList[j] = str(9)
            string = ''.join(strList)
            string = string.lstrip('0')
            print('Case #'+ str(i+1) + ': ' + string)
