'''
@author: Shawn McClelland
'''
from itertools import combinations
###  Enter filename for input and output
filename = 'C-test'
filename = 'C-small-attempt0'
#filename = 'C-large'

file_in = open('%s.in' % filename)

####  Get first line of file as number of cases
number_cases = int(file_in.readline())

####  Get lists of data for each Case - 3 places to remove '#'
dataline_single_integer1 = []
#dataline_single_integer2 = []
#dataline_single_string1 = []
dataline_multiple_integers1 = []
#dataline_multiple_integers2 = []
#dataline_multiple_strings1 = []


for i in xrange(number_cases):
###  Get lists of data for each Case - 3 places to remove '#'
    dataline_single_integer1.append(int(file_in.readline()))
#    dataline_single_integer2.append(int(file_in.readline()))
#    dataline_single_string1.append(file_in.readline())
    dataline_multiple_integers1.append(map(int, file_in.readline().split()))
#    dataline_multiple_integers2.append(map(int, file_in.readline().split()))
#    dataline_multiple_strings1.append(file_in.readline().split())
    

file_in.close()
file_out = open('%s.out' % filename, 'w')


###  Iterate for each case
for i in xrange(number_cases):
###  Get lists of data for each Case - 3 places to remove '#'
    tmp_datas1 = dataline_single_integer1[i]
#    tmp_datas2 = dataline_single_integer2[i]

#    tmp_datass1 = dataline_single_string1[i]   ------------>>??need to get rid of '\n'?? 
#    if tmp_datass1 == '\n': tmp_datass1 = tmp_datass1[:-1]

    tmp_datam1 = dataline_multiple_integers1[i]
#    tmp_datam2 = dataline_multiple_integers2[i]
#    tmp_datams1 = dataline_multiple_strings1[i]



###  Algorithm Start
    print tmp_datas1, tmp_datam1
    values1, values2, values3 = [], [], []
    for j in xrange(tmp_datas1-1):
        for k in combinations(tmp_datam1, j+1):
            values1.append(list(k))
            values2.append(sum(k))
            tmpvalue3 = 0
            for l in k:
                tmpvalue3 = tmpvalue3^l
            values3.append(tmpvalue3)
                
    print values1
    print values2
    print values3
    
    result = 'NO'
    while len(values1)>0:
        tmpindex = values2.index(max(values2))
        tmp1, tmp2, tmp3 = values1.pop(tmpindex), values2.pop(tmpindex), values3.pop(tmpindex)
        tmpsub = list(tmp_datam1)
        for x in tmp1:
            tmpsub.pop(tmpsub.index(x))
        tmpindex2 = values1.index(tmpsub)
        tmp4, tmp5, tmp6 = values1.pop(tmpindex2), values2.pop(tmpindex2), values3.pop(tmpindex2)
        if tmp3 == tmp6:
            result = tmp2
            break
    
    print 'Result', result

    output1 = result
    
    
        
    linein = str("Case #%d:" % (i + 1)) + str(' ') + str(output1) + str('\n')
    file_out.write(linein)

###  Algorithm End



file_out.close()