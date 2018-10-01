import sys
import operator
import networkx as nx


def read_int():
    return int(sys.stdin.next())


def read_ints():
    return map(int, sys.stdin.next().split(' '))


def read_float():
    return float(sys.stdin.next())


def read_floats():
    return map(float, sys.stdin.next().split(' '))


def answer(N, C, tickets):
    G = nx.Graph()

    for i, (pos1, customer1) in enumerate(tickets):
        for j, (pos2, customer2) in enumerate(tickets):
            if i >= j:
                continue
            if customer1 != customer2:
                if pos1 == 1 and pos2 == 1:
                    continue
                else:
                    weight = 1.0 if pos1 != pos2 else 0.5
                    G.add_edge((pos1, customer1, i), (pos2, customer2, j), weight=weight)


    match_dict = nx.max_weight_matching(G)
    #print match_dict

    rides = len(tickets) - len(match_dict)/2
    upgrades = 0
    for in_vertex, out_vertex in match_dict.iteritems():
        if in_vertex[0] == out_vertex[0]:
            upgrades += 1
    upgrades /= 2
    return '{} {}'.format(rides, upgrades)



if __name__ == "__main__":

    T = int(sys.stdin.next())
    queries = []
    for i in range(T):
        N, C, M = read_ints()
        tickets = []
        for j in range(M):
            pos, customer = read_ints()
            tickets.append((pos, customer))
        queries.append((N, C, tickets))
    for i, q in enumerate(queries):
        print "".join(["Case #", str(i + 1), ": ", str(answer(*q))])

