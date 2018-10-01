import sys
from numpy import *
from datetime import datetime

start = datetime.now()
print datetime.now()
iFName = "d:\\projekty\\google-jam\\runda-2\\a\\A-large.in"
outFN = "d:\\projekty\\google-jam\\runda-2\\a\\out-large.txt"

iFile = open(iFName, "r")
outF =  open(outFN, "w")

verbose = False
totalChanges = 0
tree = zeros ([3], dtype = bool) #True means AND operator
changeable = zeros ([3], dtype = bool)
chIdx = zeros ([3], dtype = int)
chMaxIdx = -1
output = zeros ([3], dtype = bool)
M = 0
def computeTC (desiredO, idx, chSF):
    if verbose:
        print 'idx ', idx, 'desired  ', desiredO, "output[idx] ", output[idx]
    if output[idx] == desiredO:
        return chSF
    else:
        if idx > ((M - 1)/2):
            return -1
        if desiredO == True :
            if not changeable[idx] :
                if tree [idx] : #AND operator
                    s1 = computeTC(True, 2 * idx, chSF)
                    if s1 == -1 :
                        return -1
                    s2 = computeTC(True, 2 * idx + 1, chSF)
                    if s2 == -1 :
                        return -1
                    else:
                        return chSF + s1 + s2
                else: #OR operator
                    s1 = computeTC(True, 2 * idx, chSF)
                    assert s1 != 0
                    s2 = computeTC(True, 2 * idx + 1, chSF)
                    assert s2 != 0
                    if (s1 == -1) and (s2 == -1):
                        return -1
                    if (s1 == -1):
                        return chSF + s2
                    if (s2 == -1):
                        return chSF + s1
                    return chSF + min (s1, s2)
            else: # changeable[idx]
                    dod = 0
                    if tree[idx] :
                        dod = 1                        
                    s1 = computeTC(True, 2 * idx, chSF)
                    s2 = computeTC(True, 2 * idx + 1, chSF)
                    if (s1 == -1) and (s2 == -1):
                        return -1
                    if (s1 == -1):
                        return chSF + s2 + dod
                    if (s2 == -1):
                        return chSF + s1 + dod
                    return chSF + min (s1, s2) + dod
        if desiredO == False :
            if not changeable[idx] :
                if tree [idx] : #AND operator
                    s1 = computeTC(False, 2 * idx, chSF)
                    assert s1 != 0
                    s2 = computeTC(False, 2 * idx + 1, chSF)
                    assert s2 != 0
                    if (s1 == -1) and (s2 == -1):
                        return -1
                    if (s1 == -1):
                        return chSF + s2
                    if (s2 == -1):
                        return chSF + s1
                    return chSF + min (s1, s2)
                else: #OR operator
                    s1 = computeTC(False, 2 * idx, chSF)
                    if s1 == -1 :
                        return -1
                    s2 = computeTC(False, 2 * idx + 1, chSF)
                    if s2 == -1 :
                        return -1
                    else:
                        return chSF + s1 + s2
            else: # changeable[idx]
                    dod = 0
                    if not tree[idx] : #OR operator
                        dod = 1                        
                    s1 = computeTC(False, 2 * idx, chSF)
                    s2 = computeTC(False, 2 * idx + 1, chSF)
                    if (s1 == -1) and (s2 == -1):
                        return -1
                    if (s1 == -1):
                        return chSF + s2 + dod
                    if (s2 == -1):
                        return chSF + s1 + dod
                    return chSF + min (s1, s2) + dod
                               
#how many cases?
N = int( iFile.readline())
print N
for case in range(N) :
    if verbose:
        print case
    S = iFile.readline()
    S = S.split()
    if verbose:
        print S
    M = int(S[0])
    V = int(S[1])
    print "CASE ***************"
    print case, datetime.now(), "M ", M, "V ", V
    
    tree = zeros ([M + 1], dtype = bool) #True means AND operator
    changeable = zeros ([M + 1], dtype = bool)
    chIdx = zeros ([M + 1], dtype = int)
    chMaxIdx = -1
    output = zeros ([M + 1], dtype = bool)
    if verbose:
        print changeable
    for i in range ((M - 1)/2):
        S = iFile.readline()
        S = S.split()
        G = S[0]
        C = S[1]
        if verbose:
            print "S ", S, "G ", G, "C ", C
        if G == '1' :
            tree[i + 1] = True
        if C == '1':
            changeable[i + 1] = True
            chMaxIdx = chMaxIdx + 1
            chIdx[chMaxIdx] = i + 1
    offset = ((M - 1)/2) + 1
    for i in range ((M+1)/2):
        S = iFile.readline()
        S = S.split()
        S = S[0]
        if verbose:
            print "S ", S
        if S == '1':
            tree [offset + i] = True
            output[offset + i] = True
    if verbose:
        print "tree ", tree[1:]
        print "changeable ", changeable [1:]
        print "chIdx ", chIdx 
        print "chMaxIdx ", chMaxIdx
        print "chIdx ", chIdx [0: chMaxIdx + 1]
    #wypelnienie output
    i = ((M - 1)/2) 
    while i > 0:
        output[i] = output[2*i] and output [2*i + 1] and tree[i] or\
                    (( output[2*i] or output [2*i + 1]) and (not tree[i]))
        i = i - 1
    if verbose:
        print "output ", output[1:]
    
    hm  = computeTC (V, 1, 0)
    print "Case #%(c)d: %(cnt)d" % {'c' : case + 1, 'cnt' : hm}
    if hm == -1:
        print >> outF , "Case #%(c)d: IMPOSSIBLE" % {'c' : case + 1}
    else:
        print >> outF , "Case #%(c)d: %(cnt)d" % {'c' : case + 1, 'cnt' : hm}
iFile.close()
outF.close()
print datetime.now()
print datetime.now() - start
