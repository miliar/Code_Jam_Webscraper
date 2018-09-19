import math

if __name__ == '__main__':
    inputFile = open('G:\\codejam\\B-small-attempt0.in', 'r+')
    outputFile = open('G:\\codejam\\output.txt', 'r+')
    inputString = inputFile.read()
    splitString = inputString.split('\n')
    
    for j in xrange(1,len(splitString)):
        if len(splitString[j]) > 0:
            string = splitString[j].split(' ')
            
            num = 0
            surprising = int(float(string[1]))
            
            p = int(float(string[2]))
            scores = []
            for i in xrange(3,len(string)):
                scores.append(int(float(string[i])))
            for score in scores:

                average = score /3.0
                print average
                ceil = math.ceil(average)
                if ceil >= p:
                    num = num +1
                else:
                    Round = round(average)
                    if p >0: 
                        if Round + 1 >= p and surprising > 0 and Round - 1 > 0:
                            surprising = surprising -1
                            num = num +1
                    else:
                        num = num + 1

            if not( j == len(splitString)-1):
                    outputFile.write('Case #'+str(j)+': ' +str(num) + '\n')
            else:
                    outputFile.write('Case #'+str(j)+': ' +str(num))

    inputFile.close()
    outputFile.close()

