f = open('C:\\Users\\djspence\\Downloads\\C-large.in', 'r')

tries = int(f.readline())

for case in range(0, tries):
    lengths = {}
    vals = f.readline().strip().split(' ')
    n = int(vals[0])
    remaining = int(vals[1])
    lengths[n] = 1
    small = 0
    large = 0
    while remaining > 0:
        lk = lengths.keys()
        maxLen = max(lk)
        num = lengths[maxLen]
        del lengths[maxLen]
        if maxLen%2 == 1:
            small = maxLen/2
            large = maxLen/2
            if small in lk:
                lengths[small]=lengths[small]+2*num
            else:
                lengths[small]=2*num
        else:
            small = maxLen/2-1
            large = maxLen/2
            if small in lk:
                lengths[small]=lengths[small]+num
            else:
                lengths[small]=num
            if large in lk:
                lengths[large]=lengths[large]+num
            else:
                lengths[large]=num
        remaining = remaining - num
    print("Case #" + str(case+1)+": " + str(large) + " " + str(small))
        
        
        
    