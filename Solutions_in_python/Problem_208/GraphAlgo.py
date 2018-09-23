import MinHeap

class GraphBase(object):
    def getSuccessors(self, node):
        """Returns a list of (node, dist)"""
        pass


class ExplicitGraph(GraphBase):
    """A graph that contains a nested dict: {node: {successor: weight}}"""
    def __init__(self):
        self.nodeSuccessors = {}

    def getSuccessors(self, node):
        return self.nodeSuccessors.get(node, {}).items()

    def getEdge(self, source, target, default=None):
        if source in self.nodeSuccessors and target in self.nodeSuccessors[source]:
            return self.nodeSuccessors[source][target]
        return default

    def setEdge(self, source, target, weight):  # Sets the edge weight, whatever value it has.
        self.nodeSuccessors.setdefault(source, {})[target] = weight

    def removeEdge(self, source, target):  # Okay to remove an edge that doesn't exist.
        if source in self.nodeSuccessors and target in self.nodeSuccessors[source]:
            del self.nodeSuccessors[source][target]

    def addToEdgeWeight(self, source, target, delta):
        """If the weight becomes 0, deletes the edge."""
        newval = self.getEdge(source, target, 0) + delta
        if newval == 0:
            self.removeEdge(source, target)
        else:
            self.setEdge(source, target, newval)

    def importNodes(self, originGraph, nodes):
        """Adds the given nodes and theit outgoing edges (this, implicitly, adds their successors, but without further edges)."""
        for node in nodes:
            for neigh, weight in originGraph.getSuccessors(node):
                self.setEdge(node, neigh, weight)

    def importSubgraph(self, originGraph, root):
        self.importNodes(originGraph, [root])
        self.importNodes(originGraph, almostDFS(originGraph, root).keys())


class AStarNodeInfo:
    def __init__(self):
        self.father = None
        self.distFromRoot = 0
        self.heuristic = 0

    def __eq__(self, other):
        return self.father == other.father and self.distFromRoot == other.distFromRoot and self.heuristic == other.heuristic

    def __ne__(self, other):
        return not self.__eq__(other)


def almostDFS(graph, root):
    """
    Returns {node: parent} dict.
    A relatively efficient way to scan all nodes reachable from 'root'.
    The scan order has some BFS-like influence.
    calls graph.getSuccessors(node) when it enters a node for the first time (including the root)."""
    data = {}
    openSet = []
    # If a node is in *data but not in openSet, then it's in the close set.

    # Enter the root
    data[root] = root
    openSet.append(root)

    # Loop
    while openSet:
        curr = openSet.pop()
        successors = graph.getSuccessors(curr)
        for succ, _ in successors:
            if succ not in data:
                data[succ] = curr
                openSet.append(succ)

    return data


def dfs(graph, root):
    """
    Returns {node: parent} dict.
    Runs a proper DFS, but a bit less efficient than almostDFS.
    calls graph.getSuccessors(node) when it enters a node for the first time (including the root),
    and graph.leaveNode(node) (if exists) when it leaves a node.
    """
    # TODO:  Not tested !!!!!

    def reversedSuccessors(node):
        successorsWithDist = graph.getSuccessors(node)
        return [succ for succ, _ in successorsWithDist[::-1]]

    data = {}
    currentPath = []
    leave = getattr(graph, 'leaveNode', lambda node: None)

    # Enter the root
    data[root] = root
    currentPath.append((root, reversedSuccessors(root)))

    # Loop
    while currentPath:
        curr, successors = currentPath[-1]
        while successors:
            succ = successors.pop()
            if succ not in data:
                data[succ] = curr
                currentPath.append((succ, reversedSuccessors(succ)))
                break
        else:
            # Checked all the successors and all were already visited
            currentPath.pop()
            leave(curr)

    return data


def topologicSort(graph, root):
    """Returns a list of all the nodes."""
    nodes = almostDFS(graph, root).keys()
    incoming = {node: 0 for node in nodes}
    for node in nodes:
        for succ, _ in graph.getSuccessors(node):
            incoming[succ] += 1
    order = [node for node, inc in incoming.iteritems() if inc == 0]
    i = 0
    while i < len(order):
        for succ, _ in graph.getSuccessors(order[i]):
            incoming[succ] -= 1
            if incoming[succ] == 0:
                order.append(succ)
        i += 1
    if len(order) < len(nodes):
        raise Exception("The graph contains a cycle.")
    return order


def aStar(graph, root, goal = None, h = lambda x: 0):
    """returns {node: AStarNodeInfo} dict"""
    data = {}
    openSet = MinHeap.UpdatableMinHeap()
    # If a node is in *data but not in openSet, then it's in the close set.

    # Enter the root
    data[root] = AStarNodeInfo()
    data[root].distFromRoot = 0
    data[root].heuristic = h(root)
    openSet.add(root, data[root].distFromRoot + data[root].heuristic)

    # Loop
    while openSet.size() > 0:
        curr = openSet.extractMin()
        if curr == goal:
            return data

        currDist = data[curr].distFromRoot
        successors = graph.getSuccessors(curr)
        for succ, dist in successors:
            newDist = currDist + dist
            succData = data.get(succ)
            updateFather = False
            if succData is None:
                succData = AStarNodeInfo()
                data[succ] = succData
                updateFather = True
                succData.heuristic = h(succ)
            else:
                if newDist < succData.distFromRoot:
                    if succ not in openSet:
                        raise Exception("A* should have updated a node in the close set!")
                    updateFather = True

            if updateFather:
                succData.distFromRoot = newDist
                succData.father = curr
                openSet.addOrUpdate(succ, succData.distFromRoot + succData.heuristic)

    return data

def dijkstra(graph, root):
    return aStar(graph, root)

def maxFlow(graph, source, sink):
    """Returns the flow value (a number)."""
    residue = ExplicitGraph()
    residue.importSubgraph(graph, source)
    totalFlow = 0

    ##@@
    import time
    _start = time.time()
    _niters = 1
    while True:
        #@@
        #print _niters, (time.time() - _start) / _niters
        _niters += 1

        data = aStar(residue, source, sink)  # It wastes energy on finding the shortest path, but leave it for now.
        if sink not in data:
            return totalFlow
        data[source] = AStarNodeInfo()
        curr = sink
        flow = currDist = data[sink].distFromRoot
        while curr != source:
            prev = data[curr].father
            prevDist = data[prev].distFromRoot
            flow = min(flow, currDist - prevDist)
            curr = prev
            currDist = prevDist
        curr = sink
        while curr != source:
            prev = data[curr].father
            residue.addToEdgeWeight(prev, curr, -flow)
            residue.addToEdgeWeight(curr, prev, flow)
            curr = prev
        totalFlow += flow
