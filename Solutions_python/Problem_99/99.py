#speaking in Tongues
import itertools 
f = open("A-large.in","r")
f2 = open("A-large.out","w")
T = int(f.readline().strip())

def getMin(A,B,probs):
    _min = B+2 #enter + B + enter

    #step by step A
    now = 1.0
    for i in xrange(A):
        current_key = i+1
        now*=probs[i]
        back_key = A-current_key
        flow1 = back_key + (B - current_key) + 1 #enter + now
        flow2 = back_key + (B - current_key) + 1 + B+1 #enter + (1-now)
        new_p = flow1*now + flow2*(1-now)
        if ( _min > new_p):
            _min = new_p
    return _min
for TT in xrange(T):
    A,B = tuple(map(int,f.readline().strip().split()))
    probs = map(float,f.readline().strip().split())
    
    f2.write( "Case #%d: %f\n" % ((TT+1),getMin(A,B,probs) ) )

f2.close()

f.close()
