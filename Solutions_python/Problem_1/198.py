def process_data_files(fin, fout):
    """Read input data from 'fin' and write results into 'fout'"""

    N = int(fin.readline())
    

    for i in xrange(N):
        s_names = set()           # empty set of 'search engine' names
        cur_switches=0          # current count of switches

        S = int(fin.readline())
        for s in xrange(S):
            s_names.add(fin.readline().replace('\n', ''))

        all_s_names = s_names.copy() # make copy

        # now process queries
        Q = int(fin.readline())
        for q in xrange(Q):
            query = fin.readline().replace('\n', '')
            
            s_names.discard(query)
            if len(s_names) == 0: # switch needed
                cur_switches += 1
                s_names = all_s_names.copy()
                s_names.discard(query)

        fout.write("Case #%d: %d\n" % (i+1, cur_switches))
                




