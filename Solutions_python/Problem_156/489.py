def f(a, i):
    if i == -1:
        return 0
    move = a[i]
    b = a[:]
    a[i/2] += move
    a[i-i/2-1] += move
    b[i/3] += move
    b[i-i/3-1] += move
    return min(f(a, i-1)+move, f(b, i-1)+move, i+1)
    
for tc in range(1, int(raw_input())+1):
    d = int(raw_input())
    plates = map(int, raw_input().split())
    tallest = max(plates)
    stacks = [0]*tallest
    for plate in plates:
        stacks[plate-1] += 1
    
    print 'Case #%d: %d' % (tc, f(stacks, tallest-1))
