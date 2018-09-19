import os
import sys



def max_yield(search_engine, search_terms):
    try:
        return search_terms.index(search_engine)
    except ValueError:
        return len(search_terms)

def yield_based(search_engines, search_terms):
    count = -1
    resultant_search_engines = []
    #print search_engines
    #print search_terms
    while search_terms:
        dist, search_engine = max([ ( max_yield(search_engine, search_terms), search_engine) for search_engine in search_engines])
        resultant_search_engines.append(search_engine)
        search_terms = search_terms[dist:]
        #print len(search_terms), search_terms[:5]
    #print resultant_search_engines
    return len(resultant_search_engines) - 1
        
def main(filename):
    if not os.path.exists(filename):
        raise SystemExit("File %s does not exist" %filename)


    fl = open(filename, 'r')
    count = int(fl.readline().strip())
    for i in range(1, count+1):
        search_engines = []
        search_engines_count = int(fl.readline().strip())
        for j in range(search_engines_count): 
            search_engines.append(fl.readline().strip())
        search_terms_count = int(fl.readline().strip())
        search_terms = []
        for k in range(search_terms_count):
            term = fl.readline().strip()
            search_terms.append(term)
        shift = yield_based(search_engines, search_terms)
        if shift < 0: shift = 0
        print "Case #%d: %d" %(i, shift)

        




if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print "Usage: python %s inputfile" %(sys.argv[0])
