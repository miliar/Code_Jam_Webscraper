__author__ = 'fcueto'
# Copyright 2014 Fernando Gonzalez del Cueto. Subject to the MIT License.
# Google Code Jam Round 1B 2014
# Problem A: The Repeater

import numpy as np

file_in  = 'A-small-attempt0.in'
file_out = file_in.replace('.in', '.out')
fid_in  = open(file_in, 'r')
fid_out = open(file_out,'w')

N_cases = int(fid_in.readline().strip())

for i in range(N_cases):

    N_words = int(fid_in.readline().strip())

    X = []

    #Read words
    wl = list()
    wc = list()

    for j in range(N_words):
        word = fid_in.readline().strip()

        letter = []
        letter.append(word[0])
        lettercount = []
        lettercount.append(1)

        for k in range(1,len(word)):
            if word[k]==letter[-1] :
                lettercount[-1] = lettercount[-1] +1
            else:
                letter.append(word[k])
                lettercount.append(1)

        wl.append(tuple(letter))
        wc.append(lettercount)

    #analyze words
    count = 0
    if len(set(wl))>1:
        #Fegla Won
        line = "Case #%i: Fegla Won\n" % (i+1)
    else:
        #Compute least number

        N_letters = len(wl[0])

        for j in range(N_letters):
            tmp = [x[j] for x in wc]
            val = np.array( tmp , dtype=np.float)
            vmean = val.mean()
            nval = np.round(val-vmean+1e-6)
            c = np.sum(np.abs(nval))
            count = count + int(c)

        line = "Case #%i: %i\n" % ((i+1), count)
    print(line.strip())
    fid_out.write(line)