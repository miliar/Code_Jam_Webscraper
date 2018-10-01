import math

def solve(R, Q):
    Q_servings = []
    for i, ing_packs in enumerate(Q):
        Q_servings.append([])
        for p in ing_packs:
            servings_max = math.floor(p / 0.9 / R[i])
            servings_min = math.ceil(p / 1.1 / R[i])
            if servings_min <= servings_max:
                Q_servings[-1].append((servings_min, servings_max))

    merged = [(i, j, k, s)
        for i, ing_pack_serv in enumerate(Q_servings)
        for j, t in enumerate(ing_pack_serv)
        for k, s in enumerate(t)]

    msorted = sorted(merged, key=lambda t: (t[3], t[2]))

    cur = [0] * len(R)
    result = 0
    needed = [0] * len(R)
    for t in msorted:
        ing, pack, is_end, val = t
        if is_end == 0:
            cur[ing] += 1
            if all(cur):
                result += 1
                for i in range(len(R)):
                    cur[i] -= 1
                    needed[i] += 1
        else:
            if needed[ing]:
                needed[ing] -= 1
            else:
                cur[ing] -= 1
    return result


def main():
    num_cases = int(input())
    for t in range(num_cases):
        N, P = map(int, input().split())
        R = list(map(int, input().split()))
        Q = [list(map(int, input().split())) for i in range(N)]
        print('Case #{}: {}'.format(t + 1, solve(R, Q)))

main()
