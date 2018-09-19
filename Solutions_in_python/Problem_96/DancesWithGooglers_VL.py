#Google Code Jam 2012 - Qualification B
#Victor Legros
with open('B-large.in') as f:
    with open ('B-large.out', 'w') as out:
        T = int(f.readline().strip()) #size
        for i in range(T):
            params = f.readline().strip().split()
            N = int(params[0]) #number
            S = int(params[1]) #surprising
            p = int(params[2]) 
            #print('\nCase #' + str(i+1) + ': N:' + str(N) +
            #      ', S:' + str(S) + ' p:' + str(p))
            #out.write('Case #' + str(i+1) + ': ')

            #Build Scores information
            scoresList = []
            for j in range(N):
                totalPoints = int(params[3+j])
                floorAverage = totalPoints // 3
                remainder = totalPoints % 3
                scoresList.append([totalPoints,floorAverage, remainder]) #nest list
            #print('Inputs: ' + str(scoresList))

            #Check for numbers: each surprising can +2
            candidateSurprise = 0
            result = 0
            for j in range(N):
                #print('Score: ' + str(scoresList[j][1]))
                if scoresList[j][1] >= p :
                    result += 1
                elif scoresList[j][1] >= (p-1) : #p is 1 greater than average
                    if scoresList[j][2] >= 1: #when 3A + 1 = p or 3A + 2
                        result += 1
                    elif (scoresList[j][2] == 0 and scoresList[j][0] > 0 ) : #Non-zeros are fine
                        candidateSurprise += 1
                        #print(str((p)))
                        #print('why: ' + str(scoresList[j]))
                elif scoresList[j][1] >= (p-2) : #p is 2 greater than average
                    if scoresList[j][2] == 2 : #when 3A + 2 = p
                        candidateSurprise += 1

                #print('Result: ' + str(result) + ', ob2: ' + str(countOffByTwo) )

            #Adjust for 'surprising' cases
            #print('S: ' + str(S) + ', ob2: ' + str(candidateSurprise) + ', minOB2; ' + str(min([S, candidateSurprise])) )
            result += min([S, candidateSurprise])

            #print('Case #' + str(i+1) + ': ' + str(result))
            out.write('Case #' + str(i+1) + ': ' + str(result) + '\n')
    out.close()
f.close()
