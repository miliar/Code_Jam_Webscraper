
inputs = int(raw_input())
i = 1

def count(bla):
    if not bla:
        return 0
    return reduce(lambda a,b:a+b, bla)

def stupid(repeats, wagonsize, groups):
    wagon = []
    result = 0
    for ignore in range(repeats):
        for j in range(len(groups)):
            if count(wagon) + groups[j] <= wagonsize:
                wagon.append(groups[j])
            else:
                break
        if groups == wagon:
            result += count(wagon)
            wagon = []
            continue
        groups = groups[j:]
        result += count(wagon)
        groups = groups + wagon
        wagon = []
    return result

while i <= inputs:
    repeats, wagonsize, group_len = map(int, raw_input().split())
    groups = map(int, raw_input().split())
    #control = stupid(repeats, wagonsize, groups)
    groups.reverse()
    loop = []
    total = 0
    wait_queue = [x for x in groups]
    if reduce(lambda a,b:a+b,groups) <= wagonsize:
        very_boring = True
    else:
        very_boring = False
    if not very_boring:
        while repeats:
            current_trip = 0
            while (wait_queue[-1] + current_trip) <= wagonsize:
                current_trip += wait_queue.pop()
                if len(wait_queue) == 0:
                    wait_queue = [x for x in groups]
            loop.append(current_trip)
            repeats -= 1
            if len(wait_queue) == group_len:
                mult, remain = divmod(repeats, len(loop))
                total = mult * reduce(lambda a, b: a+b, loop)
                if remain:
                    total += reduce(lambda a, b: a+b, loop[:remain])
                break
        total += reduce(lambda a, b:a+b, loop)
        result = total
    else:
        result = reduce(lambda a,b:a+b,groups) * repeats
    #if result != control:
    #    print result, control
    print 'Case #%i: %s' % (i, result)
    i += 1
