
opened_file = open('A-large.in','r')
strnop = ''

testcases = int(opened_file.readline())

for casenum in range(1,testcases+1):
    temp_list = opened_file.readline().split(' ')
    smax = int(temp_list[0]) + 1
    inpstrn = temp_list[1].strip('\n')
    
    standing = 0
    newp = 0
    for i in range(smax):
        if i > standing + newp:
            newp += i - (standing + newp)
        
        standing += int(inpstrn[i])
    
    strnop += 'Case #' + str(casenum) + ': ' + str(newp) + '\n'

open('output_file','w').write(strnop)
opened_file.close()

