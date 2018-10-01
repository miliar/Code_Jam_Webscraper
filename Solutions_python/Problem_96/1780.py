lines = file("B-large.in").read().split('\n')

def possible_trips(score):
    f = score/3
    s = f
    t = score - (f+s)

    x = f+1 if (score % 3) != 1 else f-1
    y = (score - x)/2
    z = score - (x+y)
    
    return [(f,s,t), (x,y,z)]

def surprise(trip):
    return max(trip)-min(trip) == 2
    
x = 1
out = ""
for line in lines[1:-1]:
    ints = [int(n) for n in line.split()]
    number = ints[0]
    max_surprised= ints[1]
    min_best = ints[2]

    y = 0
    surprised = 0
    for score in ints[3:]:
        trips = possible_trips(score) if score != 0 else [(0,0,0)]
        not_surprised = set([t for t in trips if not surprise(t)])
        is_surprised = set([t for t in trips if surprise(t)])
        greater_than_min = set([t for t in trips if max(t)>=min_best])
        if not_surprised & greater_than_min:
            y += 1
        elif (is_surprised & greater_than_min) and surprised < max_surprised:
            surprised += 1
            y += 1
        else:
            pass

    out += "Case #%s: %s\n" % (x,y) 
    x += 1

open("output", "w").write(out[:-1])
