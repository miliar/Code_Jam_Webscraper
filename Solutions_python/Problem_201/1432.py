from sys import stdin
T = int(input())

def go_to_stall(stall_groups):
    place = (len(stall_groups) - 1) // 2
    new_groups = [ stall_groups[:place], stall_groups[place+1:] ]
    return tuple([ len(x) for x in new_groups ]) + (new_groups,)

for t in range(1, T+1):
    line = stdin.readline().split()
    N, K = line
    N = int(N)
    K = int(K)
    m, M, new_groups = go_to_stall(range(N))
    for _ in range(K-1):
        biggest_size = -1
        biggest = -1
        for i,group in enumerate(new_groups):
            if len(group) > biggest_size:
                biggest_size = len(group)
                biggest = i
        m, M, new_groups_tmp = go_to_stall(new_groups[biggest])
        del new_groups[biggest]
        for x in new_groups_tmp[::-1]:
            new_groups.insert(biggest, x)
    print("Case #{:d}: {:d} {:d}".format(t, M, m))
