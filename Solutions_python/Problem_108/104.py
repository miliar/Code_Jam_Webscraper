def solve(vines, distance_to_ledge):
    prev_results = [min(vines[0].x, vines[0].length)]
    can_reach_ledge = False
    for i in range(1, len(vines)):
        vi = vines[i]
        
        options = []
        for j in range(0, i):
            vj = vines[j]             
            if (prev_results[j] is not None and prev_results[j] >= vi.x - vj.x):
                options.append(vi.x - vj.x)

        if not options:
            res = None
        else:
            res = min(vi.length, max(options))

        prev_results.append(res)

    for i in range(len(vines)):
        vi = vines[i]
        if prev_results[i] is not None and vi.x + prev_results[i] >= distance_to_ledge:
            can_reach_ledge = True

    return can_reach_ledge

def yesno(b):
    if b: 
        return "YES"
    else:
        return "NO"

test_count = int(input())

class Vine(object):
    def __init__(self, x, length):
        self.x = x
        self.length = length

for t in range(test_count):
    vine_count = int(input())
    vines = []
    for i in range(vine_count):
        line = input().split(" ")
        vine = Vine(int(line[0]), int(line[1]))
        vines.append(vine)
    distance_to_ledge = int(input())
    can_reach = solve(vines, distance_to_ledge)

    print("Case #{}: {}".format(t + 1, yesno(can_reach)))
