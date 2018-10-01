fname = "C-small-attempt0"
fin = open(fname + '.in', 'r')
fout = open(fname + '.out', 'w')

def harmonious(n):
    for note in freqs:
        if note % n != 0 and n % note != 0:
            return False
    return True

T = int(fin.readline())
for i in range(T):
    answer = "NO"
    N, L, H = [int(x) for x in fin.readline().split()]

    freqs = [int(x) for x in fin.readline().split()]

    for j in range(L, H+1):
        if harmonious(j):
            answer = j
            break
    
    fout.write('Case #{}: {}\n'.format(i+1, answer))

fin.close()
fout.close()
    
