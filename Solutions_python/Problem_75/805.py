f = open('B-large.in', 'r')
outfile = open('output.txt', 'w')

numcases = f.readline()
numcases = int(numcases)

def checkCombos(ans, combos):
    if(len(ans)<=1):
        return ans
    E1 = ans[-1]
    E2 = ans[-2]
    for combo in combos:
        if(combo[0]==E1):
            if combo[1]==E2:
                ans = ans[0:-2]
                ans += combo[2]
                return ans
        elif(combo[0]==E2):
            if combo[1]==E1:
                ans = ans[0:-2]
                ans += combo[2]
                return ans
    return ans

def checkOpposed(ans, opposed):
    if(len(ans)<=1):
        return ans
    E1 = ans[-1]
    for opposer in opposed:
        if(opposer[0]==E1):
            if opposer[1] in ans[0:-1]:
                ans = ""
                return ans
        elif opposer[1]==E1:
            if opposer[0] in ans[0:-1]:
                ans = ""
                return ans
    return ans

for case in range(numcases):
    index = 0
    line = f.readline().split()
    numcombos=int(line[index])
    index += 1
    combos = []
    for combo in range(numcombos):
        combos.append(line[index])
        index += 1
    
    numopposed = int(line[index])
    index+=1
    opposed = []
    for opposer in range(numopposed):
        opposed.append(line[index])
        index+=1
        
    arglen = line[index]
    index += 1
    arg = line[index]
    ans = ""
    
    for element in arg:
        ans += element
        ans = checkCombos(ans, combos)
        ans = checkOpposed(ans, opposed)
    
    outfile.write('Case #' + str(case+1) +': [')
    i=1
    for letter in ans:
        if i<len(ans):
            outfile.write(letter + ', ')
        if i==len(ans):
            outfile.write(letter)
        i+=1
    outfile.write(']\n')
        

                