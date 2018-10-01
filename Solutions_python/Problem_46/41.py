import numpy

def parse_cases(infile):
    n = int(infile.readline().strip())
    ret = []
    for i in range(n):
        t = int(infile.readline().strip())
        arr = []
        for i in range(t):
            arr.append(map(int,infile.readline().strip()))
        ret.append(arr)
    return ret

def handle_case(case):
    def rank_row(row):
        last_one = 0
        for cndx,val in enumerate(row):
            if val == 1:
                last_one = cndx
        return last_one
    def score_row(ndx,row):
        last_one = rank_row(row)
        return ndx - last_one
    def swap(ndx1,ndx2):
        temp = case[ndx1]
        case[ndx1] = case[ndx2]
        case[ndx2] = temp
    def is_legal():
        for ndx,row in enumerate(case):
            if score_row(ndx,row) < 0:
                return False
        return True
    def best_swap(scores,ranks):
        scores.sort(lambda a,b: a[1] - b[1])
        for (s,r),rank in zip(scores,ranks):
            if s < 0:
                not_legal = r
                break
        for ndx,rank in enumerate(ranks[not_legal:]):
            if rank <= not_legal:
                return ndx + not_legal - 1
        raise ValueError, "Impossible"
    nswaps = 0
    # print numpy.array(case, dtype='int')
    while not is_legal():
        ranks = [rank_row(row) for row in case]
        scores = [(score_row(ndx,row),ndx) for ndx,row in enumerate(case)]
        # print scores
        abs_scores = [(abs(s),n,s) for s,n in scores]
        swap_index = best_swap(scores,ranks)
        swap(swap_index, swap_index+1)
        # print numpy.array(case, dtype='int')
        nswaps += 1
            
    return nswaps



if __name__ == '__main__':
    import glob
    fname = glob.glob('A-large*.in')[0]
    infile = open(fname)
    cases = parse_cases(infile)
    for ndx,c in enumerate(cases):
        print "Case #%d: %d" % (ndx+1, handle_case(c))
