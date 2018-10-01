def solve():
    t = int(raw_input())
    for x in range(t):
        steps = 0
        current_rate = 2
        C, F, X = [float(y) for y in raw_input().split()]
        while True:
            buy = (C / current_rate) + (X / (current_rate + F))
            nobuy = X / current_rate
            if buy < nobuy:
                steps += C / current_rate
                current_rate += F
            else:
                steps += X / current_rate
                break
        print 'Case #%d: %.7f' % (x + 1, steps)
    return

if __name__ == '__main__': solve()

        
