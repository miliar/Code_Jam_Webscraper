import sys


def get_input(filename):
    with open(filename, 'r') as f:
        T = int(f.readline())
        cases = []
        for t in range(T):
            [N, Q] = [int(x) for x in f.readline().split()]
            horses = []
            for n in range(N):
                horses.append([int(x) for x in f.readline().split()])
            distances = []
            for n in range(N):
                distances.append([int(x) for x in f.readline().split()])
            deliveries = []
            for q in range(Q):
                deliveries.append([int(x) for x in f.readline().split()])
            cases.append([N, Q, horses, distances, deliveries])
        return T, cases


def print_output(res, T, filename):
    with open(filename, 'w') as f:
        for t in range(T):
            line = "Case #{0}: {1}".format(t+1, ' '.join([str(x) for x in res[t]]))
            print(line)
            f.write(line + "\n")


def find_simple_minimum_time(s):
    [N, horses, simple_distances] = s

    [E, S] = horses[0]
    possibilities = [[E - simple_distances[0], simple_distances[0] / S, S]]

    for n in range(1, N-1):
        [E, S] = horses[n]
        new_possibilities = []
        t_min = possibilities[0][1]
        for possibility in possibilities:
            [Ec, t, Sc] = possibility
            if t < t_min:
                t_min = t
            if Ec - simple_distances[n] >= 0:
                new_possibilities.append([Ec - simple_distances[n], t + simple_distances[n] / Sc, Sc])
        if E - simple_distances[n] >= 0:
            new_possibilities.append([E - simple_distances[n], t_min + simple_distances[n] / S, S])
        possibilities = new_possibilities

    t_min = possibilities[0][1]
    for possibility in possibilities:
        [Ec, t, Sc] = possibility
        if t < t_min:
            t_min = t
    return t_min


def find_minimum_time_for_deliveries(s):
    [N, Q, horses, distances, deliveries] = s
    simple_distances = [distances[i][i+1] for i in range(N-1)]
    minimum_time = find_simple_minimum_time([N, horses, simple_distances])

    return [minimum_time]


if __name__ == '__main__':
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    T, cases = get_input(input_filename)
    res = [find_minimum_time_for_deliveries(s) for s in cases]
    print_output(res, T, output_filename)
