# -*- coding: utf-8 -*-

## read input file
txt = open('input2.txt')

nb_cases = int(txt.readline())
cases = []

for i in range(0, nb_cases):
    line = txt.readline()
    cases.append(line[:-1])

#print cases
txt.close()

## process data

output = open('output.txt', 'w')

for i in range(0, nb_cases):
#    print cases[i]
    line = cases[i].split(' ')
#    print line
    shy_max = int(line[0])
    digits = line[1]
    answer = 0
#    print shy_max
#    print digits
    cumulative_count = 0 
    answer = 0
    for j in range(1, shy_max + 1) :
        cumulative_count = cumulative_count + int(digits[j-1])
#        print "cumul=%d" %cumulative_count
        if cumulative_count < j :
#            print "processing... "
            added = j - cumulative_count
            answer = answer + added
            cumulative_count = cumulative_count + added
#        else :
#            print "ok"
#    print "answer=%d" % answer


##  write output   
    towrite = 'Case #%d: ' % (i+1)
    output.write(towrite)
    output.write(str(answer))
    output.write('\n')

output.close()
