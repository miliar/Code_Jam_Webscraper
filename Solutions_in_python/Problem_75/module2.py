#!/usr/bin/env python

def parseCombineList(list, num):
    d = dict()
    for i in range(0, num):
#        print list[i]
        d[list[i][0:2]] = list[i][2]
        d[list[i][0:2][::-1]] = list[i][2]
    return d

def parseOpposedList(list, num):
    d = dict()
    for i in range(0, num):
#        print list[i]
        d[list[i][0]] = list[i][1]
        d[list[i][1]] = list[i][0]
    return d

combined = False

def combine(elems, newElem, dic):
    elems = elems + newElem
    if (dic.has_key(elems[-2:])):
        elems = elems.replace(elems[-2:], dic[elems[-2:]])
        combined = True
    else:
        combined = False
    return elems

def oppose(elems, dic):
    if combined == True:
        return elems

    if (dic.has_key(elems[-1])):
        pairNum = elems.find(dic[elems[-1]], 0, len(elems) - 1)
        if pairNum >= 0:
#            elems = elems[0:pairNum]
            elems = ""
    return elems

f = open("B-small-attempt4.in")
f.readline()

case = 1
for line in f.readlines():
    lineList = line.split(" ")
    combineDic = dict()
    opposedDic = dict()

    combineListNum = int(lineList[0])
#    print "Combine num : " + str(combineListNum)
    if combineListNum > 0:
        combineDic = parseCombineList(lineList[1:], combineListNum)

    opposedListNum = int(lineList[combineListNum+1])
#    print "Opposed num : " + str(opposedListNum)
    if opposedListNum > 0:
        opposedDic = parseOpposedList(lineList[combineListNum+2:], opposedListNum)

    invokeElem = lineList[combineListNum + opposedListNum + 3].strip()
#    print "Invoked Elem : " + invokeElem
    answer = invokeElem[0]

    for i in range(1, len(invokeElem)):
        answer = combine(answer, invokeElem[i], combineDic)
        answer = oppose(answer, opposedDic)

    answerStr = "["
    for c in answer:
        answerStr = answerStr + c + ", "
    if len(answer) != 0:
        answerStr = answerStr[0:-2]
    answerStr += "]"

    print "Case #" + str(case) + ": " + answerStr
    case += 1

f.close()