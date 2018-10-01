def find_letter(S, Q, X, L, start, letter):
    i = start
    p = '1'
    while i < X*L:
        p = Q[p + S[i%L] ]
        if letter != 'k' and p == letter :
            return i + 1
        elif letter == 'k' and p == letter and i == (X*L - 1) : 
            return 1
        i+=1
    return -1

def answer(S, Q, X, L):
    i = find_letter(S, Q, X, L, 0, 'i')
    if i == -1:
        return 'NO'
    j = find_letter(S, Q, X, L, i, 'j')
    if j == -1:
        return 'NO'
    k = find_letter(S, Q, X, L, j, 'k')
    if k == -1:
        return 'NO'
    return 'YES'
    
def reduceS(S, X, L):
    i = 0
    p = '1'
    for i in xrange(L):
        p = Q[p + S[i%L] ]
    if X % 4 == 0 or p == '1' or (X % 2 == 0 and p == '-1') :
        return False
    else:
        return True

if __name__ == '__main__':
    Q = {}
    
    Q['1i'] = 'i'
    Q['1j'] = 'j'
    Q['1k'] = 'k'
    Q['-1i'] = '-i'
    Q['-1j'] = '-j'
    Q['-1k'] = '-k'
    
    Q['ii'] = '-1'
    Q['ij'] = 'k'
    Q['ik'] = '-j'
    Q['-ii'] = '1'
    Q['-ij'] = '-k'
    Q['-ik'] = 'j'
    
    Q['ji'] = '-k'
    Q['jj'] = '-1'
    Q['jk'] = 'i'
    Q['-ji'] = 'k'
    Q['-jj'] = '1'
    Q['-jk'] = '-i'
    
    Q['ki'] = 'j'
    Q['kj'] = '-i'
    Q['kk'] = '-1'
    Q['-ki'] = '-j'
    Q['-kj'] = 'i'
    Q['-kk'] = '1'
    
    f = open('C-small-attempt1.in', 'r')
    o = open('C-small-attempt1.out', 'w')
    
    T = int(f.readline().strip())
    
    for i in range(1, T + 1):
        L, X = map(int, f.readline().strip().split())
        S = f.readline().strip()
        
        if(reduceS(S, X, L)):
            o.write('Case #' + str(i) + ': ' + answer(S, Q, X, L) + '\n')
        else:
            o.write('Case #' + str(i) + ': NO\n')