#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os.path

def sm(ch, r):
    global Num
    global Length
    global Lang
    global Mess
    Q = 0
    for c in Lang:
        try:
            if c.find(ch)==0:
                break
        except:
            pass
    else:
        print 'not found', ch
        Q = 1
    if Q == 0:
        if r >= Length:
            try:
                k = Lang.index(ch)
                print ch, k
                Num += 1
            except:
                pass
        else:
            for x in Mess[r]:
                sm(ch+x,r+1)

# Входной файл
if len(sys.argv) < 2:
    sInputFileName = '/home/evm/Документы/codejam/A-small.in'
    #sys.exit()
else:
    sInputFileName = sys.argv[1]
print sInputFileName
# Выходной файл
sOutputFileName = os.path.splitext( sInputFileName )[0]+'.out'
print sOutputFileName
InDataFile = open( sInputFileName )
OutDataFile = open( sOutputFileName, 'wt' )

L, D, N = map(int, InDataFile.readline().rstrip().split(' '))

print L, D, N


Lang = []
for Word in range(D):
    Lang.append(InDataFile.readline().rstrip())
print Lang

for tMess in range(N):
    Message = InDataFile.readline().rstrip()
    print Message
    Mess = []
    while Message:
        if Message[0]=='(':
            Mess.append(Message[1:Message.find(')')])
            Message = Message[Message.find(')')+1:]
            continue
        Mess.append(Message[0])
        Message = Message[1:]
        
    print Mess
    Num = 0
    Length = len(Mess)
    for m in Mess[0]:
        sm(m,1)
    print 'Case #%d: %d' % (tMess+1,Num)
    OutDataFile.write('Case #%d: %d\n' % (tMess+1,Num))
OutDataFile.close()    
InDataFile.close()

