import resource
import sys
# Increase max stack size from 8MB to 512MB


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]


def play(lnaomi, lken):
    #lnaomi = sorted(lnaomi)
    lken = lken[:]
    score = 0
    for n in lnaomi:
        f = filter(lambda x: x > n, lken)
        i = lken.index(min(f)) if len(f) else lken.index(min(lken))
        if n > lken[i]: score += 1
        #print (n, lken[i]), n > lken[i]
        del lken[i]
    return score

def play_dec(lnaomi, lken):
    lnaomi = lnaomi[:]
    lken = lken[:]
    score = 0
    while len(lnaomi):
        j = lken.index(min(lken))
        flnaomi = filter(lambda n: lken[j] < n, lnaomi)
        if len(flnaomi):
            i = lnaomi.index(min(flnaomi))
            #print (lnaomi[i], lken[j]), (lnaomi[i] > lken[j])
            del lnaomi[i]
            del lken[j]
            score += 1
        else: break
    while len(lnaomi):
        i = lnaomi.index(min(lnaomi))
        flken = filter(lambda n: lnaomi[i] < n, lken)
        if len(flken):
            j = lken.index(max(flken))
            #print (lnaomi[i], lken[j]), (lnaomi[i] > lken[j])
            del lnaomi[i]
            del lken[j]
    return score + play(lnaomi, lken)

f = open("D-large.in", "r")
contents = filter(lambda l: len(l) > 0, f.read().split("\n"))
contents = chunks(map(lambda l: map(float, l.split()), contents[1:]), 3)

plays = map(lambda l: (play_dec(l[1], l[2]), play(l[1], l[2])), contents)

for (i, (s1, s2)) in enumerate(plays):
    print "Case #{}: {} {}".format(i + 1, s1, s2)
