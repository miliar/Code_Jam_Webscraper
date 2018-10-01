# -*- coding: utf-8 -*-
"""
Created on Sat May 07 10:07:30 2011

@author: Shahar
"""

def C(inpfile):
    fin = open(inpfile, 'r')
    fout = open(inpfile+'.out', 'w')
    CNT = int(fin.readline())
    for iCNT in xrange(CNT):
        Case = map(int, fin.readline().rstrip('\n').split(' '))
        N = Case[0]
        L = Case[1]
        H = Case[2]
        Freqs = map(int, fin.readline().rstrip('\n').split(' '))
        
        iGoodFreq = -1
        for iFreq in xrange(L,H+1) :
            GoodFreq = True
            for jFreq in xrange(N) :
                if (iFreq % Freqs[jFreq]) != 0 and (Freqs[jFreq] % iFreq)  != 0 :
                    GoodFreq = False
                    break
            if GoodFreq :
                iGoodFreq = iFreq
                break
            
        if iGoodFreq > 0 :
            text = 'Case #' + str(iCNT+1) + ': ' + str(iGoodFreq)
        else :
            text = 'Case #' + str(iCNT+1) + ': NO'
        
        print text
        fout.write(text + '\n')

if __name__ == "__main__":
    #C(sys.argv[1]);
    #C('..\\test\\C-test.in');
    #C('..\\test\\C-small-attempt0.in');
    C('..\\test\\C-small-attempt1.in');
    #C('..\\test\\C-small-attempt2.in');
    #C('..\\test\\C-large.in');
