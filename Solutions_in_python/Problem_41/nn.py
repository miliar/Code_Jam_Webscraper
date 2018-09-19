

def f():
    fp = open('B-large.in', 'r')
    fo = open('B-large.out', 'w')
    T = int(fp.readline())
    for t in range(T):
        a = fp.readline().strip()
        seq = ['0',]
        seq[1::] = list(a)
        l = len(seq)
        large = seq[l-1]
        for i in (range(l-2,-1,-1)):
            if (seq[i] < large):
                seq1 = seq[i+1::]
                seq1.sort()
                seq = seq[:i+1:] + seq1
                ele = seq[i]
                j = i+1
                while (ele >= seq[j]):
                    j = j + 1
                seq[i] = seq[j]
                seq[j] = ele
                break
            else:
                large = seq[i]
        fo.write('Case #' + str(t+1) + ': ' + str(int(''.join(seq))) + '\n')
    fp.close()
    fo.close()
f()
        
            
