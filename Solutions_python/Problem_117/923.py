def rotate(data):
    row = len(data)
    col = len(data[0])
    for r in data:
        assert len(r) is col
    return [[data[row-1-i][j] for i in xrange(row)] for j in xrange(col)]

def printf(data):
    for r in data:
        print " ".join(str(r))

def get_min(data):
    return [[min(r)] * len(r) for r in data]

def get_cut(data):
    return [[100 - j for j in i] for i in data]

def zip_max(data1, data2):
    assert len(data1) is len(data2)
    row = len(data1)
    col = len(data1[0])
    assert col is len(data2[0])
    return [[max(data1[i][j], data2[i][j]) for j in xrange(col)] for i in xrange(row)]

def solve(data):
    cut = get_cut(data)
    min_1 = get_min(cut)
    min_2 = rotate(rotate(rotate(get_min(rotate(cut)))))
    return cut == zip_max(min_1, min_2)

def main(f):
    T = int(f.readline().strip())
    for i in xrange(T):
        row, col = [int(x) for x in f.readline().strip().split()]
        data = [[int(number) for number in f.readline().strip().split()] for j in xrange(row)]
        if solve(data):
            result = "YES"
        else:
            result = "NO"

        print "Case #{0}: {1}".format(i+1, result)
        

if __name__ == '__main__':
    with open('B-large.in','r') as f:
        main(f)