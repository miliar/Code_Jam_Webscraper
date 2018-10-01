DEBUG=0
import math

def printd(*arg):
    if DEBUG == 1:
        print("---",arg)
    
t = int(input())  # read a line with a single integer
printd("t:",t)
for case_num in range(1, t + 1):
    n,r,o,y,g,b,v =  [int(s) for s in input().split(" ")]
    #    N, R, O, Y, G, B, and V
    # ogv
    impossible = False
    if o > b:
        impossible = True
    if g > r:
        impossible = True
    if v > y:
        impossible = True
    if v > 0 and v == y :
        if (r > 0 or o > 0 or g > 0 or b > 0):
            impossible = True
        else:
            result = "VY"*v
            print("Case #{}: {}".format(case_num,result))
            continue
    if o > 0 and o  == b :
        if (r > 0 or v > 0 or g > 0 or y > 0):
            impossible = True
        else:
            result = "OB"*o
            print("Case #{}: {}".format(case_num,result))
            continue
    if g > 0 and g == r  :
        if (v > 0 or o > 0 or y > 0 or b > 0):
            impossible = True
        else:
            result = "RG"*r
            print("Case #{}: {}".format(case_num,result))
            continue
    if impossible:
        print("Case #{}: IMPOSSIBLE".format(case_num))
    else:
        b = b - o
        r = r - g
        y = y - v
        numbers = [r,y,b]
        printd("numbers: ", numbers)
        m = max(numbers)
        index = numbers.index(m)
        if index == 0:
            result = 'R'
        elif index == 1:
            result = 'Y'
        elif index == 2:
            result = 'B'
        last = result
        numbers[index] = numbers[index] - 1
        printd("numbers: ", numbers)
        m = max(numbers)
        while m > 0:
            index = numbers.index(m)
            if last == 'R':
                m = max(numbers[1],numbers[2])
                if m > 0:
                    if numbers[1] > numbers[2]:
                        index = 1
                    else:
                        index = 2
                else:
                    index = 0    
            if last == 'Y':
                m = max(numbers[0],numbers[2])
                if m > 0:
                    if numbers[0] > numbers[2]:
                        index = 0
                    else:
                        index = 2
                else:
                    index = 1
            if last == 'B':
                m = max(numbers[0],numbers[1])
                if m > 0:
                    if numbers[0] > numbers[1]:
                        index = 0
                    else:
                        index = 1
                else:
                    index = 2
            if index == 0:
                result = result + 'R'
                last = "R"
            elif index == 1:
                result = result + 'Y'
                last = "Y"
            elif index == 2:
                result = result + 'B'
                last = "B"
            numbers[index] = numbers[index] - 1
            printd("numbers: ", numbers)
            m = max(numbers)
        printd("result before loop: ", result)
        if result[0] == result[-1]:
            first = result[0]
            for i in range(len(result) - 1):
                if result[i] != first and result[i+1] != first:
                    result = result.replace(result[i]+result[i+1],result[i]+first+result[i+1],1)
                    result = result[0:len(result)-1]
                    break
        printd("result after loop: ", result)
        for i in range(len(result)-1):
            if result[i] == result[i+1]:
                impossible = True
                break
        if result[0] == result[-1]:
            impossible = True
        if impossible:
            print("Case #{}: IMPOSSIBLE".format(case_num))
        else:
            printd("result before replace:", result)
            for i in range(o):
                result = result.replace("B","BOB",1)
            for i in range(v):
                result = result.replace("Y","YVY",1)
            for i in range(g):
                result = result.replace("R","RGR",1)
            print("Case #{}: {}".format(case_num, result))
    
    
