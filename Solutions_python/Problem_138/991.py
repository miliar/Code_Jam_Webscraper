#!/usr/bin/python

# War for the google code jam
# Emilio Unda <unda91@gmail.com>

import sys


def war(naomi_o, ken_o):
    naomi = naomi_o[:]
    ken = ken_o[:]
    naomi.sort()
    ken.sort()
    
    wins = 0
    while len(naomi) > 0 :
        last = len(naomi) - 1

        if naomi[last] > ken[last]:
            # she wins but ken uses his smallest block
            wins += 1
            naomi.pop(last)
            ken.pop(0)
        else:
            #ken wins and he uses his biggest block
            naomi.pop(last)
            ken.pop(last)
    return wins


def deceitful_war(naomi_o, ken_o):
    naomi = naomi_o[:]
    ken = ken_o[:]
    naomi.sort()
    ken.sort()
    
    wins = 0
    
    while len(naomi) > 0 :
        last = len(naomi) -1

        if naomi[0] > ken[0] :
            # naomi wins and forces ken to use his smallest block
            wins += 1
            naomi.pop(0)
            ken.pop(0)
        else :
            # she wont win but she uses her smallest block and forces
            # him to use his biggest block
            naomi.pop(0)
            ken.pop(last)
    return wins


def main(argv):
    infile = open(argv[1], "r")
    out = open(argv[2], "w")

    testcases = int(infile.readline().strip())
    for i in range(testcases) :
        n = int(infile.readline().strip())
        
        words = infile.readline().split()
        naomi = map(float, words)
        
        words = infile.readline().split()
        ken = map(float, words)

        result_war = war(naomi, ken)
        result_dwar = deceitful_war(naomi, ken)

        out.write("Case #{0}: {1} {2}\n".format(i+1, result_dwar, result_war) )



if __name__ == "__main__" :
    main(sys.argv)
