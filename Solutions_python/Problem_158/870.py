import re

f = open('D-small-attempt3.in')

h = 0
count = 1
for line in f:
    if h!=0:
        data = re.split('\s', line)
        if (int(data[1])*int(data[2]))%int(data[0])!=0:
            print "Case #%d: %s" % (count, "RICHARD")
        else:
            if (int(data[1])==1 or int(data[2])==1) and int(data[0])>2:
                print "Case #%d: %s" % (count, "RICHARD")
            else:
                if int(data[1])<int(data[0]) and int(data[2])<int(data[0]):
                    print ("Case #%d: %s") % (count, "RICHARD")
                else:
                    if int(data[0]) == 4 and int(data[1]) * int(data[2])==8:
                        print "Case #%d: %s" % (count, "RICHARD")
                    else:
                        print "Case #%d: %s" % (count, "GABRIEL")
        count+=1
    else:
        h+=1
f.close()