def first(mushrooms):
    result = 0
    for i in xrange(len(mushrooms)-1):
        a, b = mushrooms[i+1], mushrooms[i]
        if a < b:
            result += b-a
        else:
            continue
    return result
            

def second(mushrooms):
    result = 0
    max_diff = 0
    for i in xrange(len(mushrooms)-1):
        a, b = mushrooms[i+1], mushrooms[i]
        if a < b:
            if b - a > max_diff:
                max_diff = b - a
    for i in xrange(len(mushrooms)-1):
        a, b = mushrooms[i+1], mushrooms[i]
        if b <= max_diff:
            result += b
        else:
            result += max_diff
    return result
        

f = open('a.in', 'r')
g = open('output_a.txt', 'w')

data = [line for line in f]
T = data.pop(0)

response = 0
for case, d in enumerate(data[::2]):
    N = int(d)
    mushrooms = [int(i) for i in data[case*2 + 1].strip().split()]
    a = first(mushrooms)
    b = second(mushrooms)

    print 'Case #%d: %d %d' %(case + 1, a, b)
    g.write('Case #%d: %d %d\n' %(case + 1, a, b))
f.close()
g.close()
