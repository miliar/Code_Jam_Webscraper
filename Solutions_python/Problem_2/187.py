#train timetable


def convert_time(times):
    x = times.split()
    y = []
    for time in x:
        hour = int(time[0:2])
        minute = int(time[3:])
        y.append([hour,minute])
#        print [hour,minute],
    return y

def increament(time,T):
    temp = time[:]
    temp[0] += (temp[1] + T)/60
    temp[1] = (temp[1] + T)%60
    return temp
    
if __name__ == '__main__':
    infile = open('input.in')
    outfile = open('output.out','w')
    case = int(infile.readline())
    for N in range(case):
#        print 'Case %d:'%(N+1)
        T = int(infile.readline())
        lines = infile.readline().split()
        [NA,NB] = [int(lines[0]),int(lines[1])]
        TA = [];TB = []
        for i in range(NA):
            lines = infile.readline()
            TA.append(convert_time(lines))
            TA.sort()
        #print TA
        for i in range(NB):
            lines = infile.readline()
            TB.append(convert_time(lines))
            TB.sort()
        #print TB
        A = B = 0
        while len(TA) != 0 or len(TB) != 0:
            if len(TA) == 0:
                B += len(TB);break
            if len(TB) == 0:
                A += len(TA);break
            if TA[0] < TB[0]:
                A += 1
                tmp = TA[0]
                TA.remove(tmp)
                TC = TB
            else:
                B += 1
                tmp = TB[0]
                TB.remove(tmp)
                TC = TA
            find = True
            while find:
                if len(TC) == 0 or increament(tmp[1],T) > TC[-1][0]:
                    find = False
                else:
                    for item in TC:
                        if item[0] >= increament(tmp[1],T):
                            TC.remove(item);tmp = item;
                            if TC is TA:
                                TC = TB
                            else:
                                TC = TA
                            break
#            print A,B
        outfile.write('Case #%d: %d %d\n'%(N + 1,A,B))
    infile.close()
    outfile.close()
    
            
            
            
            
        
        
            
            
