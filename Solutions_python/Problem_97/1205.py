import sys, math
import fileinput
input_file=sys.argv[1]


def rotate(l, x):
  return l[-x:] + l[:-x]

line_count=0

fo = open("result.txt", "wb")

for line in fileinput.input(input_file):
    if line_count > 0:
        word_count = 0
        select = 0 
        fo.write( "Case #" + str(line_count) + ": ")
        rline=line.rstrip('\n\r')
        thisline = rline.split(" ");
        for word in thisline:
            word_count = word_count +1
            if word_count == 1:
                A = int(word)
            elif word_count == 2:
                B = int(word)
                a = A

                array = []
                while a <= B:
                    A_str = str(a)
                    size = len(A_str)
                    i=1
                    while i < size:
                        c=rotate(A_str,i)
                        skip=0
                        i=i+1
                        if int(c) <= B and int(c) > a and c[0] != 0 and int(c) >= A and a <= B and a >= A:
                            set="(" + str(a) + "," + str (c) + ")"
                            for sets in array:
                                if set == sets:
                                    skip=1
                                    break
                            if skip == 0:
                                select=select+1
                            array.append(set)

                            #fo.write( "(" + str(a) + "," + str (c) + ")")
                            

                    a=a+1

                print "select= " + str(select)
                fo.write(str(select))
                fo.write("\n")

    line_count = line_count+1

fo.close()






 
        
