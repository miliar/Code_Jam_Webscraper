import math
import heapq
import sys
sys.setrecursionlimit(100000)

debug = False
# debug= True

def ls(n):
    if n%2==0:
        return n-(n/2)-1
    else:
        return n-(n+1)/2

    return res

def rs(n):
    if n%2==0:
        return n-(n/2)
    else:
        return n-(n+1)/2


def solve(N,K,round):

    while True:
        # print "solving for",N,K,round
        if K==1 or K-pow(2,round)<0:
            return max(ls(N), rs(N)), min(ls(N), rs(N))

        if K==N:
            return 0,0


        return solve(rs(N),K-pow(2,round),round+1)

def indexOfMax(segs):
    max = -1
    idxOfMax = -1
    for i in xrange(len(segs)):
        if segs[i]>max:
            max = segs[i]
            idxOfMax = i

    if debug:
        print "found max",max,"in index",idxOfMax,"in",segs
    return idxOfMax

def replaceWith(segs, maxIdx, v1, v2):
    newSegs =[]
    replacements = []
    if v1!=0 and v2!=0:
        replacements=[v1,v2]
    elif v1 != 0:
        replacements = [v1]
    elif v2!=0:
        replacements = [v2]


    if debug:
        print "replacing", segs, "with",replacements,"in index",maxIdx,"replaced value is ",segs[maxIdx]
    for i in xrange(len(segs)):
        if i != maxIdx:
            newSegs.append(segs[i])
        else:
            for r in replacements:
                newSegs.append(r)

    # print newSegs
    return newSegs

def replaceWith2(segs, max, v1, v2):
    newSegs =[]
    replacements = []
    if v1!=0 and v2!=0:
        replacements=[v1,v2]
    elif v1 != 0:
        replacements = [v1]
    elif v2!=0:
        replacements = [v2]

    count = 0

    if debug:
        print "replacing", segs, "with",replacements,"in indices of",max
    for i in xrange(len(segs)):
        if segs[i] != max:
            newSegs.append(segs[i])
        else:
            count = count+1
            for r in replacements:
                newSegs.append(r)

    # print newSegs
    return newSegs,count

def kth_largest(k, iter):
    return heapq.nlargest(k, iter)[-1]

def kth_smallest(k, iter):
    return heapq.nsmallest(k,iter)[-1]

def naive_solv(N,K):
    segments = [N]

    if K>N/2+3:
        return 0,0

    def rec(segments,K,lastMaxSeg):
        if debug:
            print "working rec on ",len(segments),K,segments

        if K<=0:
            print "got ",K,lastMaxSeg
            return max(ls(lastMaxSeg), rs(lastMaxSeg)), min(ls(lastMaxSeg), rs(lastMaxSeg))

        if K==1:
            maxSegment = kth_largest(1,segments)
            if debug:
                print "found max segment size",maxSegment
            return max(ls(maxSegment), rs(maxSegment)), min(ls(maxSegment), rs(maxSegment))

        # if len(segments) > K:
        #     seg = kth_largest(K, segments)
        #     return max(ls(seg), rs(seg)), min(ls(seg), rs(seg))

        maxIdx =indexOfMax(segments)
        maxSegment = max(segments)

        newSegments,replaced = replaceWith2(segments, maxSegment, ls(maxSegment),rs(maxSegment))
        print "replaced",replaced
        return rec(newSegments,K-replaced,maxSegment)

    return rec(segments,K,-1)

def replaceWith3(segs, max, v1, v2):
    newSegs ={}
    replacements = {}
    if v1==v2 and v1!=0:
        replacements={v1: 2}
    elif v1!=0 and v2!=0:
        replacements={v1:1,v2:1}
    elif v1 != 0:
        replacements = {v1:1}
    elif v2!=0:
        replacements = {v2:1}

    for k in segs.keys():
        if k != max:
            newSegs[k] = 0

    for r in replacements:
        newSegs[r] = 0
    count = segs[max]

    for k in segs.keys():
        if k==max:
            for r in replacements:
                newSegs[r] += segs[k]*replacements[r]
        else:
            newSegs[k] += segs[k]

    if debug:
        print segs,"->",newSegs,"replaced",count,"elements with",replacements
    return newSegs,count


def less_naive_solv(N,K):
    segments = {N:1}

    # if K>N/2+3:
    #     return 0,0

    def rec(segments,K,lastMaxSeg):
        if debug:
            print "working rec on ",len(segments),K,segments
        #
        # if kth_largest(1,segments.keys())==kth_smallest(1,segments.keys()):
        #     return max(ls(lastMaxSeg), rs(lastMaxSeg)), min(ls(lastMaxSeg), rs(lastMaxSeg))

        if K<=0:
            print "got ",K,lastMaxSeg
            return max(ls(lastMaxSeg), rs(lastMaxSeg)), min(ls(lastMaxSeg), rs(lastMaxSeg))

        if K==1:
            maxSegment = kth_largest(1,segments.keys())
            if debug:
                print "found max segment size",maxSegment
            return max(ls(maxSegment), rs(maxSegment)), min(ls(maxSegment), rs(maxSegment))

        # if len(segments) > K:
        #     seg = kth_largest(K, segments)
        #     return max(ls(seg), rs(seg)), min(ls(seg), rs(seg))

        # maxIdx =indexOfMax(segments)
        maxSegment = max(segments)

        newSegments,replaced = replaceWith3(segments, maxSegment, ls(maxSegment),rs(maxSegment))
        # print "replaced",replaced
        return rec(newSegments,K-replaced,maxSegment)

    return rec(segments,K,-1)



# filename ='C-small-1-attempt7.in'
filename ='C-large.in'
# filename ='3b.txt'
with open(filename) as f:
    content = f.readlines()

content =[x.strip() for x in content]
T=content[0]
out = []
for i in xrange(len(content)-1):
    # print i,content[i+1]
    N,K = content[i+1].split(" ")
    N=int(N)
    K=int(K)
    # y,z = solve(N,K,0)
    y,z = less_naive_solv(N,K)
    y =int(y)
    z= int(z)
    out.append("Case #%d: %s %s" % (i+1, y,z))
    print "Sol for",N,K,"is",y,z

solution = "\n".join(out)
# print solution

with open("Output3-cc.txt", "w") as text_file:
    text_file.write(solution)

