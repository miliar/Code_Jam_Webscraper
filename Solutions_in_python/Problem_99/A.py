from sys import stdin
import itertools

def make_prob_list(A,B,P):
    plist = []
    for elist in itertools.product(range(2),repeat=A):
        lpos = None
        prob = 1
        for pos,e in enumerate(elist):
            prob *= 1-P[pos] if e == 1 else P[pos]
            lpos = pos if e == 1 and lpos == None else lpos
        if lpos == None:
            lpos = B
        plist.append((lpos,prob))
    return plist
    
def readcase():
    try:
        while True:
            A,B = [int(x) for x in stdin.readline().split()]
            P = [float(x) for pos,x in enumerate(stdin.readline().split())]
            yield A,B,P
    except:
        pass

def process():
    stdin.readline() #omit cases count
    for case,(A,B,P) in enumerate(readcase()):
        plist = make_prob_list(A,B,P)
        best_expected = (B+1)*2
        for backoff in xrange(A+1):
            backpos = A-backoff
            stroke_count_non_error = backoff + (B - (A - backoff)) + 1
            stroke_count_error = stroke_count_non_error + B + 1
            expected = 0
            for epos,prob in plist:
                stroke_count = stroke_count_non_error if epos >= backpos else stroke_count_error
                expected += stroke_count*prob
            best_expected = expected if expected < best_expected else best_expected
        discard_expected = 1 + B + 1
        best_expected = discard_expected if discard_expected < best_expected else best_expected
        print "Case #%d: %.6f"%(case+1,best_expected)

if __name__=="__main__":
    process()
