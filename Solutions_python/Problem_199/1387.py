def flip_count(inp, k):
    count = 0
    inp = list(inp)
    i = 0
    while True:
        if len(inp) - i == k:
            break
        p = inp[i]
        if p == '-':
            count += 1
            for j in range(i, i + k):
                inp[j] = '-' if inp[j] == '+' else '+'
        i += 1
    last = inp[len(inp)-k:]
    if '+' in last and '-' in last:
        return 'IMPOSSIBLE'
    if '-' in last:
        count += 1
    return count

if __name__ == "__main__":
    n = int(raw_input())
    for i in range(0, n):
        inp = raw_input().strip().split(' ')
        print "Case #%d: %s" % ( i + 1, flip_count(inp[0], int(inp[1])))
