def move(arr, srcndx, trgndx):
    end = arr[trgndx+1:]
    mid = [arr[srcndx]]
    start = arr[:srcndx] + arr[srcndx + 1:trgndx+1]
    start.sort()
    start.reverse()
    return start + mid + end
    
def insert_zero(arr):
    best = 10
    bestndx = None
    for ndx,ele in enumerate(arr):
        if ele < best and ele != 0:
            best = ele
            bestndx = ndx
    arr.remove(best)
    arr.sort()
    arr.reverse()
    arr.append(best)
    return arr[:-1] + [0, arr[-1]]

def intify(arr):
    a = 0
    arr = list(arr)
    arr.reverse()
    for ele in arr:
        a *= 10
        a += ele
    return a

def increment_numbers(arr):
    first = arr[0]
    choices = []
    for ndx,ele in enumerate(arr):
        for ndx2,ele2 in enumerate(arr[ndx:]):
            ndx2 += ndx
            if ele > ele2:
                choices.append(intify(move(arr, ndx, ndx2)))
    if len(choices) == 0:
        return intify(insert_zero(arr))
    else:
        return min(choices)

def parse_input(fn):
    infile = open(fn)
    ncases = int(infile.readline())
    cases = [map(int, l.strip()) for l in infile.readlines()]
    infile.close()
    assert len(cases) == ncases
    return cases

def handle_case(c):
    c.reverse()
    out = increment_numbers(c)
    return out

if __name__ == '__main__':
    import glob
    fname = glob.glob("B-large*.in")[0]
    cases = parse_input(fname)
    for ndx,c in enumerate(cases):
        print "Case #%d: %d" % (ndx+1, handle_case(c))

