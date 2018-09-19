# Code Jam Qualifier
# 2/9/2009
# B

inname = 'E:\B.in'

fin = open(inname, 'r')
fout = open('E:\B.out.txt', 'w')

maps = int(fin.readline().strip())

INFINITY = 10001

def get_alt(cords, mapp, h, w):
    if cords[0] < h and cords[0] >= 0 and cords[1] < w and cords[1] >= 0:
        return mapp[cords[0]][cords[1]]
    return INFINITY

def set_sinks(sink, current, flows_to_x, flow_map):
    flow_map[current] = sink    
    if current in flows_to_x:
        for y in flows_to_x[current]:
            set_sinks(sink, y, flows_to_x, flow_map)
    
case_num = 1
for m in range(0, maps):
    print(case_num)
    [h, w] = [int(x) for x in fin.readline().strip().split(' ')]
    mapp = []
    flow_map = {} # store which sink x flows to
    flows_to_x = {} # store which cells flow to x
    sinks = set()
    for i in range(0, h):
        mapp.append([int(x) for x in fin.readline().strip().split(' ')])

    for r in range(0, h):
        for c in range(0, w):
            alt = mapp[r][c]
            
            north = (r - 1, c)
            west = (r, c - 1)
            east = (r, c + 1)
            south = (r + 1, c)

            minalt = min([get_alt(n, mapp, h, w) for n in [north, west, east, south]])
            minn = None
            for n in [north, west, east, south]:
                if get_alt(n, mapp, h, w) == minalt:
                    minn = n
                    break

            if minalt < alt:
                flow_map[(r, c)] = minn
                if not minn in flows_to_x:
                    flows_to_x[minn] = []
                flows_to_x[minn].append((r, c))
            else:
                sinks.add((r, c))

    # determine the sink for all the cells
    for r in range(0, h):
        for c in range(0, w):
            if (r, c) in sinks:
                set_sinks((r, c), (r, c), flows_to_x, flow_map)                   

    # label the sinks
    label_map = {}
    labelled_sinks = set()
    pointer = 0

    for k in 'abcdefghijklmnopqrstuvwxyz':
        done = False
        while pointer < h * w and not done:
            (r, c) = (pointer / w, pointer % w)
            sink = flow_map[(r, c)]
            if not sink in labelled_sinks:
                labelled_sinks.add(sink)
                label_map[sink] = k
                done = True
            pointer += 1

    # output
    fout.write('Case #' + str(case_num) + ':\n')
    for r in range(0, h):
        fout.write(' '.join([label_map[flow_map[(r, c)]] for c in range(0, w)]) + '\n')
    case_num += 1
    

fin.close()
fout.close()
