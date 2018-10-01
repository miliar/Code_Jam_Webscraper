'''
@author: Shawn McClelland
'''
import time
startt = time.time()

###  Enter filename for input and output
filename = 'A-test'
filename = 'A-small-attempt0'
filename = 'A-large'

file_in = open('%s.in' % filename)

####  Get first line of file as number of cases
number_cases = int(file_in.readline())

####  Get lists of data for each Case - 3 places to remove '#'
dataline_single_integer1 = []
#dataline_single_integer2 = []
#dataline_single_string1 = []
#dataline_multiple_integers1 = []
#dataline_multiple_integers2 = []
dataline_multiple_strings1 = []


for i in xrange(number_cases):
###  Get lists of data for each Case - 3 places to remove '#'
    dataline_single_integer1.append(int(file_in.readline()))
#    dataline_single_integer2.append(int(file_in.readline()))
#    dataline_single_string1.append(file_in.readline())
#    dataline_multiple_integers1.append(map(int, file_in.readline().split()))
#    dataline_multiple_integers2.append(map(int, file_in.readline().split()))
    tmpdataline = []
    for j in xrange(dataline_single_integer1[i]):
        tmpdataline.append(file_in.readline().split())
    dataline_multiple_strings1.append(tmpdataline)
    

file_in.close()
file_out = open('%s.out' % filename, 'w')


###  Iterate for each case
for i in xrange(number_cases):
###  Get lists of data for each Case - 3 places to remove '#'
    tmp_datas1 = dataline_single_integer1[i]
#    tmp_datas2 = dataline_single_integer2[i]

#    tmp_datass1 = dataline_single_string1[i]   ------------>>??need to get rid of '\n'?? 
#    if tmp_datass1 == '\n': tmp_datass1 = tmp_datass1[:-1]

#    tmp_datam1 = dataline_multiple_integers1[i]
#    tmp_datam2 = dataline_multiple_integers2[i]
    tmp_datams1 = dataline_multiple_strings1[i]



###  Algorithm Start

    wpset, owpset, oowpset = [],[],[]
    for j in tmp_datams1:
        wins = 0
        losses = 0
        for k in xrange(len(j[0])):
            #print j,j[0][k]
            if j[0][k] == '1':
                wins += 1
            if j[0][k] == '0':
                losses += 1
        owins, olosses = int(wins), int(losses)
        for k in xrange(len(j[0])):
            if j[0][k] == '1':
                owins += -1
                if owins+olosses != 0:
                    owp = float(owins) / (owins + olosses)
                else:
                    owp = 0
                owpset.append(owp)
                owins +=1
            if j[0][k] == '0':
                olosses += -1
                if owins+olosses != 0:
                    owp = float(owins) / (owins + olosses)
                else:
                    owp = 0
                owpset.append(owp)
                olosses +=1
            if j[0][k] == '.':
                owpset.append(-1)
            
        
        #print wins, losses
        if wins+losses != 0:
            wp = float(wins) / (wins + losses)
        else:
            wp = 0
        wpset.append(wp)
        
        towpset = []
        tow, counter =0,0
    for k in xrange(len(j[0])):
        for l in xrange(len(j[0])):
            #print owpset
            if owpset[k+l*len(j[0])] >= 0:
                tow += owpset[k+l*len(j[0])]
                counter += 1
        towpset.append(tow/counter)
        #print towpset
        tow, counter = 0, 0
    
    
    for j in tmp_datams1:
        toow, tool, counter = 0,0,0
        for k in xrange(len(j[0])):
            #print j,j[0][k]
            if j[0][k] == '1':
                toow += towpset[k]
                counter += 1
            if j[0][k] == '0':
                toow += towpset[k]
                counter += 1
        oowpset.append(toow/counter)
        
            
            
            
             
    #print wpset, 'owpset-', towpset
    #print oowpset
        

    #print tmp_datas1, tmp_datams1
    output1, output2 = 1, 1
    
    
        
    linein = str("Case #%d:" % (i + 1))+ str('\n')
    file_out.write(linein)
    for j in xrange(len(tmp_datams1)):
        rpi = 0.25 * wpset[j] + 0.50 * towpset[j] + 0.25 * oowpset[j]
        printer = '%.12f' % rpi
        printer = printer.rstrip('0')
        linein = printer + '\n'
        file_out.write(linein)

###  Algorithm End
    endt = time.time()
    print 'Case:', i+1, '%dm' % int((endt-startt)/60), '%ds' % int((endt-startt)%60)



file_out.close()