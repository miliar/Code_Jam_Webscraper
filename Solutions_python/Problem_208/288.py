import sys
import networkx as nx


def step(world_map, city_horses, s, t, chk, chs, time):
    dis = world_map[s][t]
    nhk = city_horses[s][0]
    nhs = city_horses[s][1]

    if dis > chk or (nhk >= chk and nhs >= chs):
        chk = nhk
        chs = nhs
        time += float(dis) / chs
        chk -= dis
        return [(time, chk, chs)]
    if nhk < chk and nhs < chs:
        time += float(dis) / chs
        chk -= dis
        return [(time, chk, chs)]
    return [(time + float(dis) / chs, chk - dis, chs), (time + float(dis) / nhs,  nhk - dis, nhs)]


def recursive(world_map, city_horses, path, time, chk, chs):
    if len(path) < 2:
        return [time]

    s = path[0]
    t = path[1]

    ns = step(world_map, city_horses, s, t, chk, chs, time)
    times = []
    for n in ns:
        times.extend(recursive(world_map, city_horses, path[1:], n[0], n[1], n[2]))

    return times


def solve(world_map, city_horses, targets, case_number):
    results = []

    world_graph = nx.DiGraph()
    world_graph.add_nodes_from(range(0, len(world_map)))
    for i, tos in enumerate(world_map):
        for j, d in enumerate(tos):
            if d > -1:
                world_graph.add_edge(i, j)

    for target in targets:
        s = target[0] - 1
        t = target[1] - 1
        times = []
        # FIXME: Simple path (no node appears more than once) is not good for large data set
        for path in nx.all_simple_paths(world_graph, source=s, target=t):
            times.extend(recursive(world_map, city_horses, path, 0, city_horses[path[0]][0], city_horses[path[0]][1]))
        results.append(min(times))

    print("Case #%d: %s" % (case_number, " ".join(map(str, results))))


def main():
    f = sys.stdin
    if len(sys.argv) > 1:
        f = open(sys.argv[1], 'r')

    total_cases = f.readline()
    for case_number in range(1, int(total_cases) + 1):
        n, q = map(int, f.readline().strip().split(' '))
        city_horses = []
        world_map = []
        targets = []
        for _ in range(0, n):
            k, s = map(int, f.readline().strip().split(' '))
            city_horses.append((k, s))
        for _ in range(0, n):
            world_map.append(map(int, f.readline().strip().split(' ')))
        for _ in range(0, q):
            u, v = map(int, f.readline().strip().split(' '))
            targets.append((u, v))
        solve(world_map, city_horses, targets, case_number)


if __name__ == "__main__":
    main()
