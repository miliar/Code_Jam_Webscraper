import glob, os, math
def wtf():

    # output file
    h= open('output.txt','w+')

    caseNumber= 1
    coco= 0
    with open('input.txt','r') as f:
        for line in f.readlines():
            if (coco == 0):
                print("HI")
                numberOfCases= line
            else:
                spliter= line.split(" ")
                counterNum= 0
                counter= int(spliter[0]);
                endBound= int(spliter[1]) + 1;
                while (counter < endBound):
                    squareroot= str(math.sqrt(counter)).split(".")
                    if isPalin(str(counter)) and (squareroot[1] == "0") and isPalin(str(squareroot[0])):
                        counterNum += 1
                    counter += 1
                h.write("Case #" + str(caseNumber) + ": " + str(counterNum) + "\n")
                caseNumber += 1
            coco=1
    f.close()
            


def isPalin(stringer):
    return stringer == stringer[::-1]

            

    
    
