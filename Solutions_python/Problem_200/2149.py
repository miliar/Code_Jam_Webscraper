#import random


f = open("B-large.in.txt", "r")

t = -1
nums = []

for line in f:
    if t == -1:
        t = int(line)
    else:
        nums.append(int(line))

f.close()

def getTidy(n):

    # Convert to list
    nStr = str(n)

    if len(nStr) == 1:
        return n

    nList = [int(i) for i in nStr]

    violate = -2

    for i in range(0, len(nList)-1):

        if nList[i] > nList[i+1]:
            #print(nList[i], nList[i+1])
            #return (nList[(i+1):], i)
            violate = i+1
            #if i >= 1 and nList[i-1] == nList[i]:
                #violate = i
                
            # Rollback look for duplicates
            for j in range(i, 0, -1):
                if nList[j-1] == nList[j]:
                    violate = j
                else:
                    break
            
            break

    if violate == -2:
        #return -1
        return n

    #return (nStr[violate:])
    return n - (int(nStr[violate:]) + 1)


def bruteTidy(n):

    for i in range(n, 0, -1):
        tidy = True

        string = str(i)
        for j in range(0, len(string)-1):
            if string[j] > string[j+1]:
                tidy = False
                break

        if tidy:
            return i

out = open("tidyOut.txt", "w")
for i,num in enumerate(nums):
    out.write("Case #" + str(i+1) + ": " + str(getTidy(num)) + "\n")

out.close()

'''
for i in range(100, 231):
    print(i, getTidy(i))
    print(i, bruteTidy(i))

print(3320, getTidy(3320))
print(3320, bruteTidy(3320))
print(3330, getTidy(3330))
print(3330, bruteTidy(3330))
'''
'''
random.seed()
testNums = [random.randint(00000, 99999) for i in range(1000)]
testNums = [i for i in range(1, 1001)]

for num in (testNums):
    if (bruteTidy(num) == getTidy(num)):
        print("Good", num)
    else:
        print("WHY", num)
        break

'''
'''
testT = open("testTidy.txt", "w")
#for i in range(10000000, 10000000+1000):
for i in testNums:
    testT.write(str(i) + " " + str(getTidy(i)) + "\n")

testT.close()


testBrute = open("testBrute.txt", "w")
for i in testNums:
    testBrute.write(str(i) + " " + str(bruteTidy(i)) + "\n")
    print(i, bruteTidy(i))
    
testBrute.close()
'''



