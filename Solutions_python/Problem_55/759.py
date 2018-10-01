import sys

def main():
    
    case_count = int(raw_input())
    
    ii = 0
    store = {}
    while ii < case_count:
        ii += 1
        
        r, k, n = raw_input().split(' ')
        r = int(r)
        k = int(k)
        n = int(n)
        g = raw_input().split(' ')
        
        index = 0
        seq = []
        seq.append(0)
        seq1 = []
        taken = []
        
        sub_total = 0
        stop = 0
        
        while True:

            sub_total += int(g[index])
            
            if sub_total > k or index in taken:
                sub_total -= int(g[index])
                seq1.append(sub_total)
                
                if index in seq:
                    stop = index
                    break;
                
                sub_total = int(g[index])
                seq.append(index)
                taken = []
                
            taken.append(index)

            index += 1
            if index > n - 1:
                index = 0
        
        seq_len = len(seq)
        repeat_start = seq.index(stop)
        repeat_len = seq_len - repeat_start
        repeat_times, rest_len = divmod(r - repeat_start, repeat_len)

        total = 0
        for i in range(0, repeat_start):
            total += seq1[i]
        
        rest_total = 0
        repeat_total = 0
        for i in range(repeat_start, seq_len):
            repeat_total += seq1[i]
            if rest_len > 0 and rest_len == i - repeat_start + 1:
                rest_total = repeat_total
        
        total += repeat_total * repeat_times + rest_total
        
        print 'Case #%d: %d' % (ii, total)
    return 0


if __name__ == "__main__":
    sys.exit(main())