import math

with open('input.in', 'r') as fin:
    with open('output.txt', 'w') as fout:

        '''
        pascal = [[1], [1,1]]
        for i in range(1,1001):
            middle = [pascal[i][j] + pascal[i][j+1] for j in range(i)]
            pascal.append([1]+middle+[1])


        permsnumwrong = [[1], [1,0]]
        probnumhits = [0, 0]
        fact = 1
        for i in range(2,1001):
            middle = [pascal[i][j] * permsnumwrong[j][-1] for j in range(i)]
            total = sum(middle)
            fact *= i
            permsnumwrong.append(middle+[fact-total])
            probnumhits.append((sum([(probnumhits[i]+1)*middle[i] for i in range(len(middle))])+fact-total)/total)
        '''
        numcases = int(fin.readline())
        for i in range(1, numcases+1):
            casesize = int(fin.readline())
            numwrong = 0
            line = [int(k) for k in fin.readline().split()]
            for j in range(casesize):
                if (j+1 != line[j]):
                    numwrong += 1

            fout.write("Case #"+str(i)+": ")
            fout.write(str(numwrong))
            fout.write('\n')
        
        


