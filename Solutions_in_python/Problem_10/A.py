import math
import sys
import random

def processCase(P,K,L,freq):
    if (L>P*K):
        return "Impossible"
    result = 0
    freq.sort(reverse=True)
    for i in range(0,L):
        result += freq[i]*(1+i/K)
    return repr(result)
            
    
def processFile(source, target):
    sf = open(source)
    tf = open(target,"w")
    num_cases = int(sf.readline())
    for case in range(1,num_cases+1):
        [P,K,L] = sf.readline().strip('\n').split(' ')
        P = int(P)
        K = int(K)
        L = int(L)
        freqs = sf.readline().strip('\n').split(' ')
        freq = [int(e) for e in freqs]
        result = processCase(P,K,L,freq)
        newline = 'Case #' + repr(case) + ': ' + result
        #print(newline)
        tf.write(newline)
        if not case==num_cases: tf.write('\n')
    sf.close
    tf.close

def main(argv = None):
    if argv is None:
        argv = sys.argv
    if (len(argv)>2):
        processFile(argv[1], argv[2])
    
if __name__ == "__main__":
    main()
    
