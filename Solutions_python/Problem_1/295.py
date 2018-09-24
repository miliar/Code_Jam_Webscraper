    
def main():
    def p(line):
        print line
        fo.write(line + "\n")

    FILENAME = "A-large(2).in"
    fi = file("/Users/nishio/Desktop/" + FILENAME)
    #fi = file("foo.txt")
    fo = file("/Users/nishio/0", "w")

# main code here
    UPPER_BOUND = 10000 
    num_test = int(fi.readline())
    print num_test
    for test_id in range(num_test):
        num_engine = int(fi.readline())
        engines = [fi.readline() for i in range(num_engine)]
        num_query = int(fi.readline())
        
        # start DP
        scores = [0] * num_engine
        for i in range(num_query):
            q = fi.readline()
            if q in engines:
                # switch
                target = engines.index(q)
                target_score = scores[target]
                for i in range(num_engine):
                    if i == target:
                        scores[i] = UPPER_BOUND
                    else:
                        scores[i] = min(scores[i], target_score + 1)
            else:
                # no need to switch engine
                pass

        result = min(scores)
        p("Case #%d: %s" % (test_id + 1, result))
    
    fi.close()
    fo.close()

main()
