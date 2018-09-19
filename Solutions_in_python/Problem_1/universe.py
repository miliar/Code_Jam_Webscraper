import graph
import sys

"""
Uses python-graph at http://code.google.com/p/python-graph/
"""

def parse_cases (f):
    """Parse the cases"""
    num_cases = int(f.readline().rstrip())

    for i in range(1, num_cases + 1):
        engines = parse_items(f)
        queries = parse_items(f)
        g = build_graph(engines, queries)
        print "Case #" + str(i) + ": " + str(g.shortest_path("_source")[1]["_sink"])

def parse_items (f):
    """Parse a list of items prefaced by a number"""

    num_items = int(f.readline().rstrip())
    result = []
    for i in range(0, num_items):
        result.append(f.readline().rstrip())

    return result

def build_graph (engines, queries):
    """Constructs the graph"""
    gr = graph.graph()

    gr.add_nodes(engines)
    gr.add_nodes(queries)
    gr.add_nodes(["_source", "_sink"])

    prev_gen = ["_source"] * len(engines)
    i = 0
    for ind, q in enumerate(queries):
        i = ind
        curr_gen = []
        for en_index, e in enumerate(engines):
            prev = prev_gen.pop(0)
            curr = e + "_" + str(i)
            curr_gen.append(curr)

            if e == q:
                bad_engine = en_index
            else:
                gr.add_arrow(prev, curr, wt=0)

        gr.add_nodes(curr_gen)
        connect_gen(gr, curr_gen)

        prev_gen = curr_gen

    else:
        if i > 0:
            for e in engines:
                curr = e + "_" + str(i)
                gr.add_arrow(curr, "_sink", wt=0)
        else:
            gr.add_arrow("_source", "_sink", wt=0)

    return gr

def connect_gen (gr, gen):
    """Connect all nodes in gen to each other."""
    for e in gen:
        for o in gen:
            if e == o:
                pass
            else:
                gr.add_arrow(e, o)

parse_cases(file(sys.argv[1]))
