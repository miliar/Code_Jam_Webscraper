import re
import sys
sys.stdout=open("A-large(1).out","w")
fi=open("A-large(1).in")
T=int(fi.readline())
def run(R,C,l):
#    print "\n".join(l)
#    print 
    l=[re.findall(".",re.sub(r"\#\#","/\\\\",r)) for r in l]
    l=["".join([l[r][c] for r in range(R)]) for c in range(C)]
    for c in l:
#        print "".join(c)
        if re.sub("\.|//|\\\\","",c):
            return False
    l=[re.findall(".",re.sub("//|\\\\\\\\",lambda x:"/\\" if x.group(0)=="//" else "\\/",r)) for r in l]
#    print
    for r in l:
#        print "".join(r)
        if re.sub("\.|/\\\\|\\\\/","","".join(r)):
            return False
    l=["".join([l[r][c] for r in range(C)]) for c in range(R)]
    return "\n".join(l)
for tn in range(T):
    R,C=map(int,fi.readline().split())
    l=[re.sub(r"\s","",fi.readline()) for r in range(R)]
    print "Case #%d:"%(tn+1)
    v=run(R,C,l)
    print v if v else "Impossible"
fi.close()
sys.stdout.close()