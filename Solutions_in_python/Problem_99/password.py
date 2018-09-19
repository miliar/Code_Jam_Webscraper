import pprint
import codecs
import copy

file = codecs.open("password.small.in", encoding="utf-8", mode="r")
outfile = codecs.open("password.small.out", encoding="utf-8", mode="w")
totalCases = int(file.readline())
for case in range(totalCases):
    line = file.readline().rstrip('\n').split(' ')
    A = int(line[0])
    B = int(line[1])
    PS = file.readline().rstrip('\n').split(' ')
    print A
    print B
    print PS
    list = [B+2, A+A+B-A+1]
    for i in range(0,A):
        print "i: " + str(i)
        product = float(PS[0])
        for j in range(0,A-i-1):
            print "  j: " + str(i)
            product *= float(PS[j+1])
        print "product: " + str(product)
        sum = product * (2 * i + B - A +1) + (1-product) * (2*i + 2*B - A +2)
        list.append(sum)
        print sum
    print "Case #" + str(case+1) + ": " + str(min(list))
    outfile.write("Case #" + str(case+1) + ': ' + str(min(list)) + '\n')
