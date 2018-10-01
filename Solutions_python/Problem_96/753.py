
from itertools import * 


def ceiling(x):
    if (x % 3 == 0):
        return x / 3
    else:
        return x / 3 + 1
    
    
    
def get_sup(n):
    if (n == 0):
        return 0
    x = ceiling(n-1)
    return x+1
    
def get_nosup(n):
    x = ceiling(n)
    return x




def main():
    inpfile = open("B-small-attempt0.in", 'r')
    outfile = open('outfile', 'w')
    casenum = int(inpfile.readline().strip())
    for case in range(1, casenum + 1):
        line = inpfile.readline().strip()
        linelst = line.split()

        N = int(linelst[0])
        S = int(linelst[1])
        p = int(linelst[2])
        
        linelst = linelst[3:]
        
        perm = list(permutations(linelst, len(linelst)))
        #print perm
        
        Max = 0
        
        for pe in perm:
            
            pe = list(pe)
            a = pe[:S]
            b = pe[S:]
            #print "/////////////////"
            #print a
            #print b
            #print "................."
            
            temp = 0
            for ea in a:
                ea = int(ea)
                
                sup = get_sup(ea)
                if sup >= p:
                    temp += 1
            for eb in b:
                eb = int(eb)
                
                nosup = get_nosup(eb)
                if nosup >= p:
                    temp += 1
            if (temp > Max):
                Max = temp
                
        
        
        result = "Case #" + str(case) + ": " + str(Max)+"\n"
        print result
        outfile.write(result)
    inpfile.close()
    outfile.close()




if __name__ == "__main__":

    print get_sup(18)
    print get_sup(19)
    print get_sup(20)
    print get_sup(21)
    print get_sup(22)
    print get_sup(23)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~"
    
    print get_nosup(18)
    print get_nosup(19)
    print get_nosup(20)
    print get_nosup(21)
    print get_nosup(22)
    print get_nosup(23)
    
    main()
    

    
    