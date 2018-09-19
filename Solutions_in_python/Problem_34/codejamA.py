# code jam A

import re

datain=open("A-large.in").read()
dataout=open("A-large.out","w")

data=[x for x in datain.split('\n') if x]
L,D,N=map(int,data[0].split())
words=data[1:1+D]
tests=data[1+D:]

wordstring='_'.join(words)
for i,t in enumerate(tests):
    pattern=t.replace('(','[').replace(')',']')
    text='Case #%d: %d'%(i+1,len(re.findall(pattern,wordstring)))
    dataout.write(text+'\n')
    if i%10==0:
        print i

dataout.close()

