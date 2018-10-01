import sys

def read_input(infile):
    count = 0
    in_cases = []
    with open(infile, 'r') as f:
        lines = f.readlines()
        count = int(lines[0])
        for i in range(count):
            in_cases.append(lines[i+1])
    return in_cases

def find_ls_rs(stalls, i):
    ls = 0
    rs = 0
    for l in range(i-1, 0, -1):
        if not stalls[l]:
            break
        else:
            ls += 1
    for r in range(i+1, len(stalls)):
        if not stalls[r]:
            break
        else:
            rs += 1
    return (ls, rs)        

"""
def last_stalls_config(N,K):
    import pdb
    pdb.set_trace()
    stalls = [1 for x in range(N+2)]
    stalls[0] = 0 # Occupied
    stalls[-1] = 0 # Occupied
    empty_stalls = []
    chosen_stalls = []
    for i,stall in enumerate(stalls):
        if stall:
            ls_rs = find_ls_rs(stalls, i)
            empty_stalls.append([i, min(ls_rs), max(ls_rs)])
    empty_stalls.sort(key=lambda x: x[1], reverse=True)
    for stalls in empty_stalls
    for i, config in empty_stalls.items():
        print(i, config)
    return (N,K)
"""

def fill_up_stalls(N, K):
    if N==K:
        return (0,0)
    stalls_occupied = [0, N+1]
    for i in range(K):
        stalls_occupied.sort()
        #print(stalls_occupied)
        largest_gap = 0
        stalls_range = [1, N]
        for j,x in enumerate(stalls_occupied):
            #print(j, x)
            if j==0:
                continue
            gap = x - stalls_occupied[j-1]
            if gap>largest_gap:
                stalls_range = [stalls_occupied[j-1]+1, x-1]
                largest_gap = gap
            #print(stalls_range)    
        next_stall_occupied = int((stalls_range[1]+stalls_range[0])/2)
        stalls_occupied.append(next_stall_occupied)
        if i == K-1:
            ls = next_stall_occupied - stalls_range[0]
            rs = stalls_range[1] - next_stall_occupied
            max_, min_ = max(ls,rs), min(ls,rs)
    return (max_, min_)

def divide_stalls(N, K):
    partition_length = N/(K-1)


def solve(in_cases, outfile):
    for index,case in enumerate(in_cases):
        print(index,case)
        N, K = case.split()
        max_, min_ = fill_up_stalls(int(N), int(K))
        with open(outfile, 'a') as f:
            f.write("Case #%s: %s %s\n" %(index+1, max_, min_))
    return 


if __name__ == "__main__":
    filename = sys.argv[1]
    outfile = sys.argv[2]
    in_cases = read_input(filename)
    print(in_cases)
    solve(in_cases, outfile)

