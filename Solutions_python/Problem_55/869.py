import sys

def main():
    
    case_count = int(raw_input())
    
    i = 0
    store = {}
    while i < case_count:
        i += 1
        
        r, k, n = raw_input().split(' ')
        r = int(r)
        k = int(k)
        n = int(n)
        g = raw_input().split(' ')
        
        store.clear()
        
        rr = 0
        index = 0
        total = 0
        while rr < r:
            #print store
            if store.has_key(index):
                total += store[index]['t']
                index = store[index]['n']
            else:
                start = index
                sub_total = 0
                while True:
                    sub_total += int(g[index])
                    if sub_total > k:
                        sub_total -= int(g[index])
                        store[start] = {'t': sub_total, 'n':index}
                        break
                    else:    
                        index += 1
                        if index > n - 1:
                            index = 0
                            if start == index:
                                store[start] = {'t': sub_total, 'n':index}
                                break
                            
                total += sub_total
            
            rr += 1
        print 'Case #%d: %d' % (i, total)
    return 0


if __name__ == "__main__":
    sys.exit(main())