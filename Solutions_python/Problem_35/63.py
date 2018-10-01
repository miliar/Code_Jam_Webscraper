import sys

def parse_map(H, W, input):
    result = {}
    for y in range(H):
        line = [int(t) for t in input.readline().split()]
        for x in range(W):
            result[(x, y)] = line[x]            
    return result 

def min_direction(pmap, center, north, west, east, south):
    min_d = None
    min_a = 1000000
    
    dlist = filter(lambda(x):(x in pmap), [south, east, west, north, center])
    
    for d in dlist:
        if pmap.get(d) <= min_a:
            min_d = d
            min_a = pmap.get(d)
    return min_d

label = 0

def solve(H, W, pmap):
    answer = {}
    global label
    label = 0
    chain = []
    
    def fall(pos):
        global label
        x,y = pos
        chain.append(pos)
        
        south = (x, y+1)
        east = (x+1, y)
        west = (x-1, y)
        north = (x, y-1)
        
        mind = min_direction(pmap, pos, north, west, east, south)
        if mind in answer:
            l = answer[mind]
            for c in chain:
                answer[c] = l
        elif mind == pos:
            #sink
            for c in chain:
                answer[c] = label
            label += 1
        else:
            fall(mind)
    
    for y in range(H):
        for x in range(W):
            if (x,y) in answer:
                continue
            
            chain = []
            fall((x,y))
            
    ord_a = ord('a')
    for y in range(H):
        print ' '.join([chr(answer[(x,y)] + ord_a) for x in range(W)])


def main():
    input = open(sys.argv[1])
    num_cases = int(input.readline())
    
    for n in range(1, num_cases+1):
        H, W = (int(t) for t in input.readline().split())
        m = parse_map(H, W, input)
        
        print 'Case #%d:' % n
        solve(H, W, m)
        
if __name__ == '__main__':
    main()
    