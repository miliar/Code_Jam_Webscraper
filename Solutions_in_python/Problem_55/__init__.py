def main():
    filename = 'small.in'
    
    inf = open(filename, 'r')
    outf = open(filename + '.out', 'w')
    case = 1
    for i, line in enumerate(inf):
        if i == 0:
            continue
        values = line.split()
        if i % 2 != 0:
            R = int(values[0])
            k = int(values[1])
            N = int(values[2])
            continue
        g = [int(v) for v in values]
#        print g    
        count = 0
        cur = 0
        earn = 0
        while count < R:
            start = cur
            passenger = 0
            while passenger + g[cur] <= k:
#                print str(g[cur]) + ' ',
                passenger += g[cur]
                cur += 1
                if cur == N:
                    cur = 0
                if start == cur:
                    break
#            print ''
            earn += passenger
            count += 1
            
        buf = 'Case #%d: %d\n' % (case, earn)
        outf.write(buf)
        case += 1
    inf.close()


if __name__ == '__main__':
    main()
    
