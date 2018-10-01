"""
Google Code Jam 2015 - QR - Question - 01 - Standing Ovation
__author__     = "Aby Paul"
"""

def findMinFriendsNeeded(inDataRecord):    
    minFriendsNeeded = 0
    audienceStoodSoFar = 0
    
    inDataList = inDataRecord.split()
    sMax = int (inDataList[0])    
    sCurrentData = inDataList[1]
    for idx in range(sMax+1):
        fNeededForLevel = 0
        audienceNeeded = idx
        if audienceNeeded > audienceStoodSoFar:
            fNeededForLevel = audienceNeeded - audienceStoodSoFar
        minFriendsNeeded += fNeededForLevel
        audienceStoodSoFar += (fNeededForLevel + int(sCurrentData[idx]))
    
    # print(inDataRecord, str(minFriendsNeeded))
    return minFriendsNeeded

def main():
    inFileName = 'indata.txt'
    outFileName = 'outdata.txt'
    with open(outFileName, 'w') as fw:
        with open(inFileName, 'r') as fr:
            testCaseCount = int (fr.readline().strip())
            for testCase in range(testCaseCount):
                line = fr.readline().strip()
                minFriendsNeeded = findMinFriendsNeeded(line)
                print('Case #{}: {}'.format(testCase+1, minFriendsNeeded), file=fw)
         
    pass

if __name__ == '__main__':
    main()