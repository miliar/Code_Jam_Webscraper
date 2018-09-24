import sys
import copy

def main():
    f = open (sys.argv[1])
    
    nCases = int (f.readline())

    for cases in range (nCases):
        nSearchEngines = int (f.readline())
        searchEngines = []
        for se in range (nSearchEngines):
            searchEngines.append(f.readline().rstrip())
        
        nQueries = int (f.readline())
        queries = []
        for q in range (nQueries):
            queries.append (f.readline().rstrip())

        submitable = []
        for q in queries:
            l = set()
            for se in searchEngines:
                if q != se:
                    l.add(se)
            submitable.append(l)
        
        
        count = 0
        if len(submitable) > 0:
            s = submitable[0]
            for i in range(1, len(submitable)):
                s = s.intersection(submitable[i])
                if len(s) == 0:
                    s = submitable[i]
                    count += 1
            #        print s
            

     #   print 'Case #%(case): %(c)' % {'case': cases + 1, 'c': count}
        print "Case #" + str(cases + 1) + ": " + str(count)
        
                

    f.close()

if __name__ == "__main__":
    sys.exit(main())
