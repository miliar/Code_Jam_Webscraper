import sys

_r = open(sys.argv[1], "r")
_w = open(sys.argv[1]+".out", "w")
def readline():
    return _r.readline().strip()
def writeline(str):
    print str
    _w.write(str + "\n")

####

def inv_flow(h,w,i):
    assert new_map[h][w] < 0
    new_map[h][w] = i
    for hh,ww in iflow[h][w]:
	inv_flow(hh,ww,i)
	iflow[h][w] = []

T = int(readline())

for t in range(T):
    X = t + 1
    H, W = readline().split()
    H = int(H); W = int(W)

    alt_map = []
    for h in range(H):
        alt_map.append(map(int, readline().split()))

    new_map = [[-1 for i in range(W)] for i in range(H)]
    iflow = [[[] for i in range(W)] for i in range(H)]
    sinks = []
    for h in range(H):
        for w in range(W):
            alt = alt_map[h][w]
            sink = True
            low_alt = alt
            # (Sink), North, West, East, South
            if h > 0 and low_alt > alt_map[h-1][w]:
                low_alt = alt_map[h-1][w]
                sink = False
		flowh, floww = (h-1,w)
            if w > 0 and low_alt > alt_map[h][w-1]:
                low_alt = alt_map[h][w-1]
                sink = False
		flowh, floww = (h,w-1)
            if w < W-1 and low_alt > alt_map[h][w+1]:
                low_alt = alt_map[h][w+1]
                sink = False
		flowh, floww = (h,w+1)
            if h < H-1 and low_alt > alt_map[h+1][w]:
                low_alt = alt_map[h+1][w]
                sink = False
		flowh, floww = (h+1,w)
            if sink:
                sinks.append((h,w))
            else:
		iflow[flowh][floww].append((h,w))
    i = 0
    for h,w in sinks:
	inv_flow(h,w,i)
	i += 1

    remap = [-1] * len(sinks)
    letter = 'a'
    for h in range(H):
        for w in range(W):
            m = new_map[h][w]
            r = remap[m]
            if r == -1:
                remap[m] = letter
                r = letter
                letter = chr(ord(letter)+1)
            new_map[h][w] = r

    writeline("Case #%s:" % X)
    for h in range(H):
        row = " ".join(new_map[h])
        writeline(row)

