'''
Created on Apr 14, 2012

@author: dhutchis
'''
import pickle
global numToRecycleList
numToRecycleList = []

# rotate right
def rotate(s):
    return s[-1]+s[:-1]

# generate list of numbers m such that n < m and m is recycled from n
def getSortedBiggerRecycleList(num):
    result_set = set()
    num_s = str(num)
    num_s_rot = num_s
    for i in range(len(num_s)):
        num_s_rot = rotate(num_s_rot)
        num_s_rot_int = int(num_s_rot)
        if num_s_rot_int > num:
            result_set.add(num_s_rot_int)
    result_list = list(result_set)
    result_list.sort()
    return result_list
    
def formRecycleList():
    global numToRecycleList
    numToRecycleList = [ [] for n in range(2000001)]
    for n in range(2000001):
        numToRecycleList[n] = getSortedBiggerRecycleList(n)

if __name__ == '__main__':
    '''
    fi = open("biglist", 'wb')
    formRecycleList()
    pickle.dump(numToRecycleList, fi)
    fi.close()
    '''
    
    fi = open("biglist", 'rb')
    numToRecycleList = pickle.load(fi)
    fi.close()
    input("Ready? ")
    
    w = open("out.out", "w")
    f = open("test.in")
    T = int(f.readline())
    for tnum in range(1, T+1):
        line = f.readline().split()
        w.write("Case #"+str(tnum)+': ')
        A = int(line[0])
        B = int(line[1])
        resultPairs = 0
        for n in range(A,B):
            for m in reversed(range(len(numToRecycleList[n]))):
                if numToRecycleList[n][m] <= B:
                    resultPairs += m + 1
                    break
        w.write(str(resultPairs)+'\n')
    f.close()
    w.close()
    


