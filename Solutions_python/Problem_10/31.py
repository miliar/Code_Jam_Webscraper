def main():
    N = int(raw_input())
    for cur_case in xrange(N):
        cur_case = cur_case + 1

        line = raw_input()
        P, K, L = line.split()
        P = int(P)
        K = int(K)
        L = int(L)

        counts = raw_input()
        counts = [int(x) for x in counts.split()]

        counts.sort(reverse = True)

        iterations = L / K
        if L % K > 0:
            iterations += 1
        key_pressed = 0
        for idx in xrange(iterations):
            key_p = idx + 1
            key_pressed += sum(counts[idx * K: key_p * K]) * key_p
        
        print 'Case #%d: %d' % (cur_case, key_pressed)

if __name__ == '__main__':
    main()

