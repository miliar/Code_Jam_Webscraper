'''
@author: Shawn McClelland
'''

###  Enter filename for input and output
filename = 'B-test'
filename = 'B-small-attempt0'
filename = 'B-large'

file_in = open('%s.in' % filename)

####  Get first line of file as number of cases
number_cases = int(file_in.readline())

####  Get lists of data for each Case - 3 places to remove '#'
#dataline_single_integer1 = []
#dataline_single_integer2 = []
dataline_single_string1 = []
#dataline_multiple_integers1 = []
#dataline_multiple_integers2 = []
#dataline_multiple_strings1 = []


for i in xrange(number_cases):
###  Get lists of data for each Case - 3 places to remove '#'
#    dataline_single_integer1.append(int(file_in.readline()))
#    dataline_single_integer2.append(int(file_in.readline()))
    dataline_single_string1.append(file_in.readline())
#    dataline_multiple_integers1.append(map(int, file_in.readline().split()))
#    dataline_multiple_integers2.append(map(int, file_in.readline().split()))
#    dataline_multiple_strings1.append(file_in.readline().split())
    

file_in.close()
file_out = open('%s.out' % filename, 'w')


###  Iterate for each case
for i in xrange(number_cases):
###  Get lists of data for each Case - 3 places to remove '#'
#    tmp_datas1 = dataline_single_integer1[i]
#    tmp_datas2 = dataline_single_integer2[i]

    tmp_datass1 = dataline_single_string1[i]    
    if tmp_datass1 == '\n': tmp_datass1 = tmp_datass1[:-1]

#    tmp_datam1 = dataline_multiple_integers1[i]
#    tmp_datam2 = dataline_multiple_integers2[i]
#    tmp_datams1 = dataline_multiple_strings1[i]



###  Algorithm Start
    tmp_datass1 = tmp_datass1.split()
    print tmp_datass1
    C = int(tmp_datass1.pop(0))
    Cs = []
    if C>0:
           for k in xrange(C):
               Cs.append(tmp_datass1.pop(0))
    D = int(tmp_datass1.pop(0))
    Ds = []
    if D>0:
           for k in xrange(D):
               Ds.append(tmp_datass1.pop(0))
    N = int(tmp_datass1.pop(0))
    Ns = ''
    if N>0:
           Ns = tmp_datass1.pop(0)
    
    Cs1 = []       
    for j in Cs:
        tmp = [j[0:2], j[2]]
        Cs1.append(tmp)
    Ds1 = []
    for j in Ds:
        tmp = [j[0], j[1]]
        Ds1.append(tmp)
    
    print C, Cs1, D, Ds1, N, Ns
    
    
    result=''
    for j in xrange(len(Ns)):
        #print Ns[j]
        result += Ns[j]
        for k in Cs1:
            #print 'k', k
            if k[0] in result:
                result = result.replace(k[0], k[1])
            tmp = k[0]
            tmp = tmp[::-1]
            #print 'tmp', tmp
            if tmp in result:
                result = result.replace(tmp, k[1])
        for k in Ds1:
            if k[0] in result and k[1] in result:
                result = ''
                print 'blanked'
        
    print 'Result', result
    
    resultstring = list(result)
    results = '['
    for j in resultstring:
        results += j + ', '
    if results[-1] == ' ':
        results = results[:-2]
    results += ']'
    print results
    
    
    

    output1 = results
    
    
        
    linein = str("Case #%d:" % (i + 1)) + str(' ') + str(output1) + str('\n')
    file_out.write(linein)

###  Algorithm End



file_out.close()