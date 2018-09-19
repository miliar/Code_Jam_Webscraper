i = 0
N = [] #Total Dancers
S = [] #Surpising Scores (max difference = 2)
P = [] #Score were looking for
scoresum = []
IN = open('ScoresLargeIn.txt','r')
OUT = open('ScoresLargeOut.txt','w')
for line in IN:
    i = i + 1
    if (i == 1):
        total_cases = int(line)
    else:
        data = line.split(' ')
        N.append(int(data[0]))
        S.append(int(data[1]))
        P.append(int(data[2]))
        tempsum = []
        for j in range(3,len(data)):
            tempsum.append(int(data[j]))
        scoresum.append(tempsum)
"""
print total_cases
print N
print S
print P
print scoresum
"""
for i in range(0,total_cases):
    used = 0 #Total Surpising scores used
    answer = 0
    if(P[i] == 0):
        answer = N[i]
    elif(P[i] == 1):
        for j in range(0,len(scoresum[i])):
            if scoresum[i][j] > 0:
                answer = answer + 1
    elif(P[i] == 2):
        for j in range(0,len(scoresum[i])):
            if (scoresum[i][j] == 2 and used < S[i]):
                used = used + 1
                answer = answer + 1
            elif (scoresum[i][j] == 3 and used < S[i]):
                used = used + 1
                answer = answer + 1
            elif (scoresum[i][j] > 3):
                answer = answer + 1
    else:
        for j in range(0,len(scoresum[i])):
            #print "Dancer = {0}".format(scoresum[i][j])
            step1 = max(scoresum[i][j] - P[i],0)
            #print step1
            step2 = step1/2.0
            #print step2
            if (step2 >= P[i] - 1):
                #print "WERE FINE HERE\n"
                answer = answer + 1
            elif(step2 >= P[i] - 2):
                if (used < S[i]):
                    #print "HEY IT WAS SURPRISING\n"
                    used = used + 1
                    answer = answer + 1
                #else:
                    #print "NO MORE SURPRISES ALLOWED"
    print "Case #{0}: {1}\n".format(i+1,answer)
    OUT.write("Case #{0}: {1}\n".format(i+1,answer))
OUT.close()
