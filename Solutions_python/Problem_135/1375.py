def main():
    a = open('A-small-attempt1.in', 'r')
    test = a.read()
    test2 = test.replace('\n', ',')
    allinfo = test2.split(',')
    testcase = int(allinfo[0])
    b = open ('result2.in', 'w')
    for i in range (1, testcase + 1):
        first_num = int(allinfo[10 * i - 9])
        second_num = int(allinfo[10 * i -4])
        #the dumb way
        actual_pos = 10 - (first_num + 1)
        first = allinfo[10 * i - actual_pos]
        
        actual_pos2 = 4 - second_num
        second = allinfo[10 * i - actual_pos2]
        
       
        first_tuple = first.split(' ')
        second_tuple = second.split(' ')
        intersec = set(first_tuple).intersection(second_tuple)
        intersection = len(set(first_tuple).intersection(second_tuple))
        
        if intersection == 0:
            print ("Case #%d: Volunteer cheated!"%(i))
            b.write("Case #%d: Volunteer cheated!\n"%(i))
            
        elif intersection == 1:
            pop = int(intersec.pop())
            print ("Case #%d: %d" % (i, pop))
            b.write("Case #%d: %d\n" % (i, pop))
        elif intersection > 1:
            print ("Case #%d: Bad magician!" % (i))
            b.write("Case #%d: Bad magician!\n" % (i))
    b.close()
                   
main()

        
