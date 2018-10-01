#!/usr/bin/python3

#$Id:$

# Google code jam 2014
# problem 4 - Deceitful war

import getopt
import sys

def usage():
    print('''
    Deceitful war (task 4)

Options:
-h (--help) 
-v (--verbose)
-f (--input) filename
''')


if __name__ == "__main__":

    verbose = False
    fname = "input.txt"

    if sys.version_info[0] < 3:
        print("This script requires Python 3. (You are running %d.%d)" % (
            sys.version_info[0], sys.version_info[1])) 
        sys.exit()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hvf:",
                                   ["verbose","help","input="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print (str(err)) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-v", "--verbose"):
            verbose = True
        elif o in ("-f", "--input"):
            fname = a
        else:
            usage()
            sys.exit()


    # reading input
    # first line: number of test cases. T cases follow
    # each test case:
    # one line containing integer number of blocks (N) - 1000 max
    # one line containing N floats (naomi blocks)
    # one line containing N floats (ken blocks)
    # sample:
    # 4
    # 1
    # 0.5
    # 0.6
    # 2
    # 0.7 0.2
    # 0.8 0.3
    # 3
    # 0.5 0.1 0.9
    # 0.6 0.4 0.3
    # 9
    # 0.186 0.389 0.907 0.832 0.959 0.557 0.300 0.992 0.899
    # 0.916 0.728 0.271 0.520 0.700 0.521 0.215 0.341 0.458


    f = open(fname, "rt")
    ncases = int(f.readline())
    if verbose:
        print("%s: %d cases." % (fname, ncases))

        # input
    for c in range(ncases):
        N = int(f.readline())
        Naomi = [float(x) for x in f.readline().split()] 
        Ken = [float(x) for x in f.readline().split()]

        Naomi.sort()
        Ken.sort()

        if verbose:
            print("Case %d: N: %d" % (c+1, N))
            print(Naomi)
            print(Ken)

        # solve
        # war result: take smallest item of naomi and match it with just
        # bigger block of ken

        i = 0
        j = 0
        score = 0

        while(i < N and j < N):
            if verbose:
                print ("W Naomi[%d]: %.3f Ken[%d]: %.3f" % (i, Naomi[i], j, 
                                                            Ken[j]), end = "")
            if (Ken[j] > Naomi[i]):
                score += 1
                if verbose:
                    print (' +')
                i += 1
            else :
                if verbose:
                    print()
            j += 1

        if verbose:
            print("War score: %d" % (N - score))
            
        # deceitful war new
        # compare smallest -- if naomi smallest smaller than Ken:
        # match smallest of naomi with largest remaining from Ken (Ken scores)
        # else
        # match smallest item of naomi with smallest of Ken (Naomi scores)
        i = 0
        j = 0
        dscore = 0
    
        while(i < N and j < N):
            if verbose:
                print ("W Naomi[%d]: %.3f Ken[%d]: %.3f" % (i, Naomi[i], j, 
                                                            Ken[j]), end = "")
            if (Ken[j] > Naomi[i]):
                dscore += 1
                if verbose:
                    print (' +')
            else :
                if verbose:
                    print(' -')
                j += 1
            i += 1
                

        if verbose:
            print("New DWar score: %d" % (N - dscore))

        print("Case #%d: %d %d" % (c+1, N - dscore, N - score))

        



        

        




