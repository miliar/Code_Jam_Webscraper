import random

f = open("B-small-attempt4.in", "r")
fout = open("out.txt", "w")

def out(*args, sep=' ', end='\n'):
    print(*args, sep=sep, end=end)
    print(*args, sep=sep, end=end, file=fout)

def overlap(x1,y1,d1,x2,y2,d2):
    return (d1+d2)**2 > (x1-x2)**2 + (y1-y2)**2

def conflict(pos, d, loc):
    for l in loc:
        if overlap(pos[0],pos[1],d,l[0],l[1],l[2]):
            return True
    return False

def process(T):
    [N, W, L] = [int(i) for i in f.readline().rstrip().split(' ')]
    rs = [int(i) for i in f.readline().rstrip().split(' ')]
    loc = []
    for d in rs:
        pos = (random.randint(0,W), random.randint(0,L))
        while conflict(pos, d, loc):
            pos = (random.randint(0,W), random.randint(0,L))
        loc.append((pos[0], pos[1], d))

    out(('Case #%d: ' % T) + ' '.join([str(l[0]) + " " + str(l[1]) for l in loc]))

if __name__ == '__main__':
    for t in range(1, int(f.readline())+1):
        process(t)

f.close()
fout.close()