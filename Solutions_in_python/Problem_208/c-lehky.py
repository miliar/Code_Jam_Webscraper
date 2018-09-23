t = int(input())

for c in range(t):
    N, Q = [int(item) for item in input().split()]
    horses = [[0, 0] for i in range(N)]
    ways = [0 for i in range(N - 1)]
    spaces = [[] for i in range(N)]
    for i in range(N):
        horses[i] = [int(item) for item in input().split()]
    for i in range(N - 1):
        ways[i] = int(input().split()[i + 1])
    input()
    input()
    spaces[0] = [[0, 0, 0]]
    for i in range(N - 1):
        for space in spaces[i]:
            if ways[i] <= space[0]:
                new_space = [space[0] - ways[i], space[1], space[2] + ways[i] / space[1]]
                for for_space in spaces[i + 1]:
                    if for_space[0] <= new_space[0] and for_space[1] <= new_space[1] and for_space[2] >= new_space[2]:
                        del spaces[i + 1][spaces[i+1].index(for_space)]
                    elif for_space[0] >= new_space[0] and for_space[1] >= new_space[1] and for_space[2] <= new_space[2]:
                        new_space = False
                        break
                if new_space:
                    spaces[i + 1].append(new_space)
            if ways[i] <= horses[i][0]:
                spaces[i + 1].append([horses[i][0] - ways[i], horses[i][1], space[2] + ways[i] / horses[i][1]])
    minimum = spaces[-1][0][2]
    for i in range(len(spaces[-1])):
        minimum = min(minimum, spaces[-1][i][2])
    if minimum == int(minimum):
        print("Case #%d: %d" % (c + 1, minimum))
    else:
        print("Case #%d: %f" % (c + 1, minimum))
