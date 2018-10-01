import sys

def main():
    if len(sys.argv) >= 2:
        file = sys.argv[1]
        f = open(file)
        numOfTest = f.readline().split()[0]
        for i in range(int(numOfTest)):
            rowOne = int(f.readline())
            for j in range(4):
                if j != rowOne - 1:
                    f.readline()
                    continue
                rowOneContent = f.readline().split()
            rowTwo = int(f.readline())
            for j in range(4):
                if j != rowTwo - 1:
                    f.readline()
                    continue
                rowTwoContent = f.readline().split()
            judge(i + 1, rowOneContent, rowTwoContent)
            
def judge(caseNum, listOne, listTwo):
    if len(set(listOne).intersection(set(listTwo))) > 1:
        print "Case #" + str(caseNum) + ": " + "Bad magician!"
    elif len(set(listOne).intersection(set(listTwo))) == 1:
        print "Case #" + str(caseNum) + ": "+ list(set(listOne).intersection(set(listTwo)))[0]
    else:
        print "Case #" + str(caseNum) + ": " + "Volunteer cheated!"
        
    
if __name__ == '__main__':
    main()