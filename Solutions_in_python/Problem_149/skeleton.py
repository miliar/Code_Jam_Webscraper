def do():
    times = input()
    for i in xrange(times):
        print 'Case #%d:'%(i+1),
        calculate()

def calculate():
    N = input()
    L = map(int,raw_input().split())

    count = 0

    while L:
        min_value = min(L)
        min_index = L.index(min_value)
        if min_index*2 < len(L):
            count += min_index
        else:
            count += len(L)-min_index-1
        L.remove(min_value)
    
    print count


if __name__ == '__main__':
    do()

