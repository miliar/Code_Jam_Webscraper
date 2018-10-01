import sys;


target = 'welcome to code jam'

def last_four(n):
    string = str(n)[-4:]
    lst = ['0']*4
    for i in range(len(string)):
        lst[-(i+1)] = string[-(i+1)]
    return ''.join(lst)

def print_case(case, num):
    print("Case #{0}: {1}".format(case, last_four(num)))

ncases = int(sys.stdin.readline().rstrip())
cases = [x + 1 for x in range(ncases)]

for case in cases:
    idxmap = dict([(c,[]) for c in target])
    line = sys.stdin.readline().rstrip()
    for i in range(len(line)):
        chr = line[i]
        if chr in idxmap:
            idxmap[chr].append((i,0))
    pathlist = [list(idxmap[c]) for c in target]
    pathlist.reverse()
    pathlist[0] = [(i,n+1) for i,n in pathlist[0]] #set n=1 for last row

    for current in range(len(pathlist)-1):
        for (idx,paths) in pathlist[current]:
            #for every lower index in previous row, add the paths through this
            #index to the paths through that index.
            prev = pathlist[current+1]
            for n in range(len(prev)):
                i,j = prev[n]
                if i < idx:
                    prev[n] = (i,j+paths)
        pathlist[current+1] = [(x,y) for x,y in prev if y > 0]

    total = sum(n for i,n in pathlist[-1])
    print_case(case, total)
