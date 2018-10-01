# -*- coding: utf-8 -*-

import csv
f = open("/home/daichi2/ドキュメント/python/A-small-attempt7.in")
no = 0
output = []
for row in f :
    no = no +1
    print(row)
    s = len(row)
    s = int(int(s))
    # print(s)
    k = int(row[s-2])
    if k == 0 : k = 10
    # print(k)
    row1 = [str(i) for i in row]
    del row1[s-3 : s]
    # print(row1)
    # print(len(row1))
    pu = ['+']
    mi = ['-']
    for i in range(k-1):
        pu = pu + ['+']
        mi = mi + ['-']
    c = 0
    j = 0
    while len(row1) >= k :
        print(row1)
        print(j)
        #print(len(row1))
        # print(row1[0:k])
        #print (c + k)
        # print (mi)
        # print(c)
        
        if row1[0:k] == pu :
            del row1[0:k]
            #print("DP")
            c = 0
            continue

        if row1[0:k] == mi :
            del row1[0:k]
            c = 0
            j = j + 1 
            #print("DMj")
            #print(row1)
            continue

        if len(row1) < c + k : break
        
        if row1[c] == '+':
            c = c +1
            #print(row1[c])
            #print(row1)
            #print(c)
        else :
            j = j + 1
            for i in range(k):
                if row1[c + i] == '+': row1[c + i] = '-'
                else : row1[c + i] = '+'
                #print(i)
                #print(row1)
            continue

    # print(row1)
        
    for i in range(len(row1)) :
        if row1[i] == '-' : j = "IMPOSSIBLE" 
           
    print(j)
    f = open('out.txt', 'a')
    f.write('Case #' + str(no) + ': ' + str(j)+'\n')

