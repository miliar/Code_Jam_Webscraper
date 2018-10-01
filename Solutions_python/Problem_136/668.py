import utils

if __name__ == "__main__":
    inputFile = "B-large.in"
    outputFile = "outputQ2Large"
    inputData = utils.createReadFile(inputFile)
    outputData = utils.createWriteFile(outputFile)
    cases = inputData.next()
    cases = cases.replace("\n","")
    print cases
    for index in range(1, int(cases) + 1):
        count = 1
        for row in inputData:
            rowData = row.replace("\n","")
            rowData = rowData.split(" ")
            print rowData 
            C = float(rowData[0])
            F = float(rowData[1])
            X = float(rowData[2])
            P = 2.0
            flag = 1
            totalTime = 0.0
            if X <= C:
                flag = 0
                totalTime = X / P
            else:
                totalTime += C / P
            while flag == 1:
                lower = C / F
                upper = (X - C) / P
#                time1 = C / productRate + 
                if lower >= upper:
                    totalTime += upper
                    flag = 0
                else:
                    P += F
                    totalTime += C / P
                

            outputString = "Case #" + str(count)+ ": " + str(totalTime) + "\n"
            print outputString
            outputData.write(outputString)
                
            count += 1
            

