#!/usr/bin/python
def TidyNum():
    T = int(raw_input())
    for i in xrange(1,T+1):
        N = int( raw_input() )
        #print N
        # TN  = large(N)
        TN2 = large2(N)
        print "Case #"+ str(i)+ ":",
        print TN2

def large2(N):
    if istidy(N): 
        return N
    else:
        i = 10
        TN = N
        while not istidy(TN):
            TN = (N/i - 1)*i + i-1
            i *= 10
        return TN


def large(N):
    for i in xrange(N,0,-1):
        if istidy(i):
            return i

def istidy(N):
    s = str(N)
    for i in range(len(s)-1):
        if ord(s[i]) > ord(s[i+1]):
            return False
    return True






if __name__ == "__main__":
    # istidy(232345234)
    TidyNum()




