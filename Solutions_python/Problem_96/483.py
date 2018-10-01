
def main():
    
    t = int( raw_input() )
    
    for tc in range(t):
        nums = [ int(s) for s in raw_input().split(' ') ]
        n = nums[0]
        s = nums[1]
        p = nums[2]
        t = nums[3:]
        sure = 0
        maybe = 0
        for v in t:
            if v >= 3*p-2: sure += 1
            elif v >= 3*p-4: maybe += 1
        total = sure
        if p >= 2: total += min(s, maybe)
        print 'Case #%s: %s' % (tc+1, total)


if __name__ == '__main__':
    main()
