#
#Input
#
#Output
#
#4
#1 9
#10 40
#100 500
#1111 2222
#Case #1: 0
#Case #2: 3
#Case #3: 156
#Case #4: 287

def alter(st):
    st = st[1:] + st[0]
    return st


f = open('input', 'r')
fw = open('output', 'w')
len = f.readline()
#print len.rstrip()
i=0
for x in range(int(len)):
    i+=1
    line = f.readline()
    line = line.rstrip()
    x = line.split()
    small= int(x[0])   #small number
    large = int(x[1])  #large number
    count = 0
    for x in range(small,large+1):
        x = str(x)
        y = alter(x)
        while y != x:
            if small <= int(x) and int(x) < int(y) and int(y) <= large:
                count += 1
                #print str(small) +' - ' + str(x) + ' - '  + str(y) + ' - ' + str(large)
            y = alter(y)
            #print str(small) +' - ' + str(x) + ' - '  + str(y) + ' - ' + str(large)

    #print 'Case #'+str(i)+': '+line
    print 'Case #'+str(i)+': '+ str(count)
    fw.write( 'Case #'+str(i)+': '+ str(count)+'\n')
