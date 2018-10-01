#!/usr/bin/python

import string
import sys

train1 = 'ejp mysljylc kd kxveddknmc re jsicpdrysi'
train2 = 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
train3 = 'de kr kd eoya kw aej tysr re ujdr lkgc jv'

ans1 = 'our language is impossible to understand'
ans2 = 'there are twenty six factorial possibilities'
ans3 = 'so it is okay if you want to just give up'


alpha = [' ']*256;

lenstr = len(train1)

def trainer( train_str, ans_str ):
    for i in range(0,len(train_str)):
        alpha[ ord(train_str[i]) ] = ans_str[i]

def translate( str ):
    trstr= ''
    for i in range(0,len(str)):
        trstr += alpha[ ord(str[i])]
    return trstr

alpha[ ord('q') ] = 'z'
alpha[ ord('z') ] = 'q'

trainer( train1, ans1 )
trainer( train2, ans2 )
trainer( train3, ans3 )


# translate

numTest = sys.stdin.readline()
f = open('translateOutput','w')

i = 1
for line in sys.stdin.readlines():
    f.write( 'Case #' + str(i) + ': ' + translate(line) + '\n')
    i = i+1

#################################

#print translate(train1)
#print translate(train2)
#print translate(train3)

#total = 0
#for c in string.lowercase:
#    if alpha[ ord(c) ] == ' ':
#        print c
#    else:
#        total = total+1

#for c in string.lowercase:
#    for el in alpha:
#        if el == c:
#            print el
     
#total = 0
#for el in alpha:
#    if el != ' ':
#        total = total + 1
#        print el

#print total

