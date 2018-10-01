'''
Created on Sep 3, 2009

@author: Robin
'''
import string, time

words = []
global cache
cache = {}
    
def count(what, inwhat):
    #print "trying to find",what,"in",inwhat,"lenwhat:",len(what)
    global cache
    if cache.has_key(what+":"+inwhat):
        return cache[what+":"+inwhat]
    if len(what) == 0:
        return 0
    if len(what) == 1:
        if what in inwhat:
            #print "returning 1"
            return string.count(inwhat, what)
        return 0
        
    pos = string.find(inwhat,what[0])  
    c = 0
    while pos != -1:
        c+= count(what[1:], inwhat[pos+1:])
        pos = string.find(inwhat,what[0],pos+1)
    cache[what+":"+inwhat] = c
    #print cache
    return c
    
startT = time.clock()
f=open('c.in', 'r')
lines = int(f.readline())
wel = "welcome to code jam"



for i in range(lines):
    s = f.readline()
    occ = count(wel, s)%10000
    #print count(wel, s)
    st = str(occ)
    if occ < 1000: st = "0"+st
    if occ < 100: st = "0"+st
    if occ < 10: st = "0"+st
    #if occ < 1: st = "0"+st
        
    print "Case #"+str(i+1)+":",st
#print time.clock()