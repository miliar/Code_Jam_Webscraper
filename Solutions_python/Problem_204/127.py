import math
from collections import defaultdict


# Python program for implementation of Ford Fulkerson algorithm
# From http://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/

class Graph:

    def __init__(self,graph):
        self.graph = graph # residual graph
        self. ROW = len(graph)
        #self.COL = len(gr[0])     

    '''Returns true if there is a path from source 's' to sink 't' in
    residual graph. Also fills parent[] to store the path '''
    def BFS(self,s, t, parent):

        # Mark all the vertices as not visited
        visited =[False]*(self.ROW)

        # Create a queue for BFS
        queue = []

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        # Standard BFS Loop
        while queue:

            #Dequeue a vertex from queue and print it
            u = queue.pop(0)

            # Get all adjacent vertices of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0 :
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        # If we reached sink in BFS starting from source, then return
        # true, else false
        return True if visited[t] else False

    # Returns tne maximum flow from s to t in the given graph
    def FordFulkerson(self, source, sink):

        # This array is filled by BFS and to store path
        parent = [-1]*(self.ROW)

        max_flow = 0 # There is no flow initially

        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent) :

            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while(s !=  source):
                path_flow = min (path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Add path flow to overall flow
            max_flow +=  path_flow

            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while(v !=  source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


def solve(N, P, R, Q):
    # print(N, P)
    # print(R)
    # print(Q)
    vals = []
    next_node_id = 1
    for needed, row in zip(R, Q):
        this_vals = []
        for i in range(P):
            have = row[i]
            least = have * 10. / 11 / needed
            most = have * 10. / 9 / needed
            least_serve = int(math.ceil(least))
            most_serve = int(math.floor(most))
            # print(needed, have, least, least_serve, most, most_serve)
            # row[i] = (have, [k for k in range(least_serve, most_serve + 1)])
            if least_serve <= most_serve:
                this_vals.append((next_node_id, least_serve, most_serve))
                next_node_id += 1
        vals.append(this_vals)

    graph = [[0] * (next_node_id + 1) for _ in range(next_node_id + 1)]
    for node_id, l_s, m_s in vals[0]:
        graph[0][node_id] = 1
    for node_id, l_s, m_s in vals[-1]:
        graph[node_id][next_node_id] = 1
    for i in range(len(vals) - 1):
        nodes = vals[i]
        next_nodes = vals[i + 1]
        for i_id, a, b in nodes:
            for j_id, c, d in next_nodes:
                if (c >= a and c <= b) or (d >= a and d <= b) or (a >= c and a <= d) or (b >= c and b <= d):
                    graph[i_id][j_id] = 1

    g = Graph(graph)
    source = 0
    sink = next_node_id
    return(g.FordFulkerson(source, sink))


if __name__ == "__main__":
    output = []
    fname = 'b-large'
    with open(fname + '.in') as f:
        inputs = [line.strip() for line in f]

    num_cases = int(inputs[0])
    line = [1]

    def next_line():
        text = inputs[line[0]]
        line[0] += 1
        return text

    for i in range(num_cases):
        N, P = map(int, next_line().split())
        R = [int(c) for c in next_line().split()]
        Q = []
        for j in range(N):
            Q.append([int(c) for c in next_line().split()])
        print("Case", i + 1)
        output.append("Case #%d: " % (i + 1) + str(solve(N, P, R, Q)))

    with open(fname + '.out', 'w') as f:
        f.write('\n'.join(output))
