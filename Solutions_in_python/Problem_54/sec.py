def common_span(span,t):
    tmp = 1
    stop = span/2
    while tmp <= stop:
        val = span/tmp
        if t%val == 0 and span%val == 0:
            return val
        tmp = tmp + 1
    
    return 1

def max_time(n,times):
    span = None
    times.sort()

    for i in range(1,n):
        t = times[i] - times[i-1]
        if t != 0:
            if span == None:
                span = t
            elif span > t:
                # max common
                span = common_span(t,span)
            elif span < t:
                span = common_span(span,t)

    if span == None:
        return '0'
    
    start = times[0]
        
    real_time = (start + span - 1)/span

    real_time = real_time * span

 
    past_time = real_time - start

    return str(past_time)

f = open('B-large.in')
fw = open('resultB.out','w+')

n = int(f.readline())

for i in range(n):
    fw.write('Case #')
    fw.write(str(i+1))
    fw.write(': ')
    line = f.readline().replace('\n','')
    data = line.split(' ')
    n = int(data[0])
    times = [long(x) for x in data[1:len(data)]]
    l = max_time(n,times)
    fw.write(l)
    fw.write('\n')

f.close()
fw.close()
