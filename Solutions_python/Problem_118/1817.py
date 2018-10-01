import math

def FairSquareList():
    A = 1
    B = 100000000000000
    FairSquareNumbers = list()
    start = int(math.ceil(math.sqrt(A)))
    end = int(math.sqrt(B))
    for i in range(start, end+1):
        #print 'DEBUG', i, math.pow(i,2)
        if (str(i) == str(i)[::-1]):
            curr_num = int(math.pow(i,2))
            if (str(curr_num) == str(curr_num)[::-1]):
                FairSquareNumbers.append(curr_num)

    return FairSquareNumbers

def FairSquare(AllNumsList):
    inp = raw_input()
    nums = inp.split(' ')
    A = int(nums[0])
    B = int(nums[1])
    #get start point
    start = -1
    for i in range(AllNumsList.__len__()):
        if (AllNumsList[i] >= A):
            start = i
            break
    if (start == -1):
        return 0
    else:
        end = AllNumsList.__len__()-1
        for i in range(start, AllNumsList.__len__()):
            if AllNumsList[i] > B:
                end = i-1
                break
        return end-start+1
    

if __name__ == "__main__":
    testcases = int(raw_input())
    AllNums = FairSquareList()
    for i in range(0, testcases):
        print "Case #"+str(i+1)+': '+str(FairSquare(AllNums));
        
