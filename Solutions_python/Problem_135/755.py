import os, sys
from operator import itemgetter, attrgetter

try:
    file = sys.argv[1]
except Exception as inst:
    print inst, '\n\nSyota avattava tiedosto parametrina!\n\n'
finally:
    file = sys.argv[1]
    fin = open(file, 'r')
    fout = open(file[:-2]+'out', 'w')
    cases = fin.readline()
    print 'Tapauksia ' + cases
    
    for case in range(0, int(cases)):
    #for case in range(0, 3):
        print ("\nCase " + str(case))
        lines = []
        for x in [0,1]:
            line = int(fin.readline())
            #print line, x
            for y in [1,2,3,4]:
                read = fin.readline()[:-1]
                if y == line:
                    lines.extend(read.split(" "))
        #print lines
        #print len(lines), len(set(lines))
        

        if len(lines)-1 == len(set(lines)):
            lines.sort()
            number = -1
            for x in xrange(0, len(lines)-1):
                if lines[x] == lines[x+1]:
                    #print (lines[x])
                    number = lines[x]
                    break
            print ('Case #'+str(case+1)+': '+ str(number) + '\n')
            fout.write('Case #'+str(case+1)+': '+ str(number) + '\n')
        elif len(lines) == len(set(lines)):
            print ('Case #'+str(case+1)+': Volunteer cheated!\n')
            fout.write('Case #'+str(case+1)+': Volunteer cheated!\n')
        else:
            print ('Case #'+str(case+1)+': Bad magician!\n')
            fout.write('Case #'+str(case+1)+': Bad magician!\n')

        
    fin.close()
    fout.close()
