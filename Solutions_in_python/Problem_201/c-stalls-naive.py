from sys import stdin


def read_str(): return stdin.readline().rstrip('\n')
def read_strs(): return stdin.readline().rstrip('\n').split()
def read_int(): return int(stdin.readline())
def read_ints(): return map(int, stdin.readline().split())
def read_floats(): return map(float, stdin.readline().split())


def solve_case():
    N, K = read_ints()
    
    if N == K:
        return '0 0'
    
    len_stalls = N + 2
    
    stalls = [False] * len_stalls
    stalls[0] = True
    stalls[-1] = True
    
    last_value = None
    for i in range(K):
        values = [None] * len_stalls
        for j in range(len_stalls):
            if not stalls[j]:
                ls = 0
                for k in range(j - 1, -1, -1):
                    if not stalls[k]:
                        ls += 1
                    else:
                        break
                rs = 0
                for k in range(j + 1, len_stalls):
                    if not stalls[k]:
                        rs += 1
                    else:
                        break
                values[j] = (ls, rs)
        
        farthest = []
        maximal = 0
        for j in range(len_stalls):
            if values[j] is not None:
                minimal = min(values[j])
                if minimal > maximal:
                    maximal = minimal
                    farthest = [j]
                elif minimal == maximal:
                    farthest.append(j)
        
        last_stall = -1
        if len(farthest) == 1:
            last_stall = farthest[0]
        else:
            maximal = -1
            maximal_j = -1
            for j in farthest:
                m = max(values[j])
                if m > maximal:
                    maximal = m
                    maximal_j = j
            last_stall = maximal_j
            
        stalls[last_stall] = True
        last_value = values[last_stall]
    
    return ' '.join(map(str, (max(last_value), min(last_value))))

    
def main():
    cases = read_int()
    for case in range(1, cases + 1):
        print('Case #{}: {}'.format(case, solve_case()))

        
if __name__ == '__main__':
    main()
