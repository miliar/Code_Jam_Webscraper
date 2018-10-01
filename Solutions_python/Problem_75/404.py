import sys

def main():
    lines = sys.stdin.readlines()
    cases = int(lines[0])
    for case in xrange(1,cases+1) :
        occurrence = {'Q' : 0, 'W' : 0, 'E' : 0, 'R' : 0, 'A' : 0, 'S' : 0, 'D' : 0, 'F' : 0}
        combine = {}; opposed = {}
        line = lines[case].split()
        count = 1; combineRules = int(line[0])
        for i in xrange(combineRules) :
            combine[line[count][0:2]] = line[count][2]
            count = count + 1
        opposedRules = int(line[count])
        count = count + 1
        for i in xrange(opposedRules) :
            opposed[line[count]] = 1
            count = count + 1
        invokeCount = int(line[count])
        invoke = line[count+1]
        elementList = []
        for i in xrange(invokeCount) :
            current = invoke[i]
            elementList.append(invoke[i])
            occurrence[invoke[i]] = occurrence[invoke[i]] + 1
            if len(elementList) >= 2 :
                lastTwo = elementList[-2] + elementList[-1]
                if lastTwo in combine or lastTwo[::-1] in combine :
                    if lastTwo[::-1] in combine :
                        lastTwo = lastTwo[::-1]
                    elementList.pop()
                    elementList.pop()
                    elementList.append(combine[lastTwo])
                    occurrence[lastTwo[0]] = occurrence[lastTwo[0]] - 1
                    occurrence[lastTwo[1]] = occurrence[lastTwo[1]] - 1
                else :
                    if (('Q'+current in opposed or current+'Q' in opposed) and occurrence['Q'] > 0) or \
                       (('W'+current in opposed or current+'W' in opposed) and occurrence['W'] > 0) or \
                       (('E'+current in opposed or current+'E' in opposed) and occurrence['E'] > 0) or \
                       (('R'+current in opposed or current+'R' in opposed) and occurrence['R'] > 0) or \
                       (('A'+current in opposed or current+'A' in opposed) and occurrence['A'] > 0) or \
                       (('S'+current in opposed or current+'S' in opposed) and occurrence['S'] > 0) or \
                       (('D'+current in opposed or current+'D' in opposed) and occurrence['D'] > 0) or \
                       (('F'+current in opposed or current+'F' in opposed) and occurrence['F'] > 0) :
                        elementList = []
                        occurrence = {'Q' : 0, 'W' : 0, 'E' : 0, 'R' : 0, 'A' : 0, 'S' : 0, 'D' : 0, 'F' : 0}
        
        print "Case #" + str(case) + ": [" + ", ".join(elementList) + "]"
    
main()
