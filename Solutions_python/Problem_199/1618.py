def main():
    T = int(input())
    for case in range(1, T+1):
        S, k = input().split()
        n_pancakes = len(S)
        griddle = int(base=2, x=''.join('1' if b == '-' else '0' for b in S))

        k = int(k)
        flipper = 0
        for i in range(k):
            flipper <<= 1
            flipper |= 1

        flips = 0
        while(griddle):
            if griddle & 1:
                flips += 1
                griddle ^= flipper
            griddle >>= 1
            if flips > n_pancakes - k + 1:
                flips = 'IMPOSSIBLE'
                break
            
        print('Case #{}: {}'.format(case, flips))
            
if __name__ == '__main__':
    main()
