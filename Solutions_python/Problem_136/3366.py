#!/usr/bin/env python
# -*- coding: utf-8 -*-


src = u"B-small-attempt0.in"
#src = u"test-B.txt"
dst = "B-small.out"

def makeTimeFunc(C,X,F,firm):
    
    makeTime = F/(2.0+X*firm)
    while firm > 0:
        makeTime += C/(2.0+(firm-1)*X)
        firm -= 1
    return makeTime
    
def process(src, dst):
    
    fo = open(dst, 'w')
    itr = 0
    
    for line in open(src):
        line = line.strip()
        if itr == 0:
            T = int(line)
        else:
            (C, X, F) = line.split(' ')
            C = float(C)
            X = float(X)
            F = float(F)
            #print C, X, F
            
            preAnswer = makeTimeFunc(C,X,F,0)
            i = 1
            while (makeTimeFunc(C,X,F,i) - preAnswer) < 0:
                preAnswer = makeTimeFunc(C,X,F,i)
                #print preAnswer
                i += 1
            
            
            answer = "Case #" + str(itr) + ": " + str(preAnswer)
            #print answer
            fo.write(answer + "\n")

        itr += 1

    fo.close()
if __name__ == '__main__':
    
    process(src, dst)
            