import math
def get_node(idx, rootval):
    tree_path = []
    maxrow = int(math.floor(math.log(rootval, 2))+1)
    row = int(math.floor(math.log(idx, 2))+1)
    if row == maxrow:
        return (0,0)
    value = idx
    for i in range(0, row):
        tree_path.append(value)
        value = int(math.floor(value/2))

    nodes_in_path = []
    prevleft = rootval
    prevright = rootval
    for i in reversed(tree_path):
        if i%2 == 0:
            value = prevleft
        else:
            value = prevright
        if value == 1:
            left = 0
            right = 0
        else:
            value = float(value-1)
            left = int(math.ceil(value/2))
            right = int(math.floor(value/2))
        nodes_in_path.append((left, right))
        prevleft = left
        prevright = right

    #print "row %s/%s" % (row, maxrow)
    #print tree_path
    #print nodes_in_path
    return nodes_in_path[-1]


"""
value = 20

for i in range(1, value+1):
    print "%s %s" % (i, get_node(i, value))
"""

def get_node_bf(idx, rootval):
    # brute-force it
    stalls = []
    nodes = []
    for i in range(0, rootval):
        stalls.append('.')
        nodes.append((i, rootval-i-1))

    for person in range(0, idx):
        #print "".join(stalls)
        # each person comes in and evaluates each stall
        # first pass: find the max of min(L, R)
        maxMinLR = 0
        for i in range(0, rootval):
            # evaluate only empty stalls
            if stalls[i] == '.':
                thisMinLR = min(nodes[i])
                if thisMinLR > maxMinLR:
                    maxMinLR = thisMinLR
        # second pass: evaluate the set S that have the max min(L, R)
        #print "maxMinLR: " + str(maxMinLR)
        S = []
        maxMaxLR = 0
        for i in range(0, rootval):
            # evaluate only empty stalls
            if stalls[i] == '.':
                thisMinLR = min(nodes[i])
                thisMaxLR = max(nodes[i])
                if thisMinLR == maxMinLR:
                    S.append(i)
                    # also get the max of max(L, R) for the set S
                    if thisMaxLR > maxMaxLR:
                        maxMaxLR = thisMaxLR
        #print "maxMaxLR: " + str(maxMaxLR)
        chosen_stall = -1
        if len(S) == 1:
            chosen_stall = S[0]
        else:
            for i in S:
                # get first with max of maxLR
                thisMaxLR = max(nodes[i])
                if thisMaxLR == maxMaxLR:
                    chosen_stall = i
                    break
        # populate the chosen stall
        stalls[chosen_stall] = 'X' #'(%s)' % (person+1)
        # if this is the idx person, we can return
        #print "Person %s chooses stall %s with node (%s, %s)" % (person+1, chosen_stall, nodes[chosen_stall][0], nodes[chosen_stall][1])
        #print get_node(person+1, rootval)
        if person + 1 == idx:
            #print nodes
            #print "".join(stalls)
            return (max(nodes[chosen_stall]), min(nodes[chosen_stall]))
        # re-evaluate all the nodes
        for i in range(0, rootval):
            left = 0
            if i > 0:
                # count backwards from i
                for j in range(i-1, -1, -1):
                    if stalls[j] == '.':
                        left = left + 1
                    else:
                        break
            right = 0
            if i < rootval-1:
                for j in range(i+1, rootval):
                    if stalls[j] == '.':
                        right = right + 1
                    else:
                        break
            nodes[i] = (left, right)

    #print stalls
    #print nodes
    return (0, 0)

def get_node2(idx, rootval):
    maxrow = int(math.floor(math.log(rootval, 2))+1)
    row = int(math.floor(math.log(idx, 2))+1)
    if row == maxrow:
        return (0,0)
    # run through all the nodes in the row
    start = int(math.pow(2,row-1))
    end = int(math.pow(2,row))
    maxMinLR = 0
    otherMinLR = -1
    counts = { }
    nodes = { }
    for i in range(start, end):
        node = get_node(i, rootval)
        #print "%s: %s" % (i, node)
        thisMinLR = node[0] + node[1]
        if thisMinLR >= maxMinLR:
            maxMinLR = thisMinLR
        else:
            otherMinLR = thisMinLR
        if thisMinLR in counts:
            counts[thisMinLR] = counts[thisMinLR] + 1
        else:
            counts[thisMinLR] = 1
            nodes[thisMinLR] = node
    countMax = counts[maxMinLR]
    #print counts
    #print start

    if otherMinLR < 0 or start + countMax - 1 >= idx:
        return nodes[maxMinLR]
    else:
        return nodes[otherMinLR]

def add_to_nodes(nodes, value, count):
    if value in nodes:
        nodes[value] = nodes[value] + count
    else:
        nodes[value] = count
    return nodes

def get_node_div(idx, rootval):
    maxrow = int(math.floor(math.log(rootval, 2))+1)
    trow = int(math.floor(math.log(idx, 2))+1)
    if trow == maxrow:
        return (0,0)

    row = 0
    nodes = { }
    nodes = add_to_nodes(nodes, rootval, 1)
    while row < trow:
        row = row + 1
        prevnodes = nodes
        nodes = { }
        for value in prevnodes:
            left = int(math.ceil(float(value-1)/2))
            right = int(math.floor(float(value-1)/2))
            count = prevnodes[value]
            nodes = add_to_nodes(nodes, left, count)
            nodes = add_to_nodes(nodes, right, count)

    # now we are at trow
    #print "Row %s: %s" % (row, nodes)
    start = int(math.pow(2,row-1))
    #print "This row starts with node %s" % start
    nodesonthisrow = 0
    maxcount = -1
    maxcountvalue = -1
    maxvalue = -1
    minvalue = rootval+1
    for value in nodes:
        count = nodes[value]
        nodesonthisrow = nodesonthisrow + count
        if count > maxcount:
            maxcount = count
            maxcountvalue = value
        if value > maxvalue:
            maxvalue = value
        if value < minvalue:
            minvalue = value
    nodesonthisrow = nodesonthisrow / 2
    #print "%s nodes on this row" % nodesonthisrow
    #print "Max count is %s for value %s" % (maxcount, maxcountvalue)
    if maxcountvalue == maxvalue:
        #print "Possible nodes are (%s, %s) and (%s, %s)" % (maxvalue, maxvalue, maxvalue, minvalue)
        greaternodecount = maxcount - nodesonthisrow
        #print "There should be %s nodes with value (%s, %s)" % (greaternodecount, maxvalue, maxvalue)
        if start + greaternodecount > idx:
            return (maxvalue, maxvalue)
        else:
            return (maxvalue, minvalue)
    else:
        #print "Possible nodes are (%s, %s) and (%s, %s)" % (maxvalue, minvalue, minvalue, minvalue)
        greaternodecount = nodesonthisrow*2 - maxcount
        #print "There should be %s nodes with value (%s, %s)" % (greaternodecount, maxvalue, minvalue)
        if start + greaternodecount > idx:
            return (maxvalue, minvalue)
        else:
            return (minvalue, minvalue)

    return (0, 0)

N = 20
K = 19
#print get_node_div(K, N)
#print get_node2(K, N)
#print get_node_bf(K, N)

"""
for i in range(1, K+1):
    row = int(math.floor(math.log(i, 2))+1)
    print "%s %s %s" % (i, row, get_node_div(i, N))
"""

lines = open("C-small-2-attempt1.in").readlines()
#lines = open("in.txt").readlines()
"""

T = int(lines[0])
caseno = 1
for line in lines[1:T+1]:
    line = line.lstrip().rstrip()
    N = int(line.split(" ")[0])
    K = int(line.split(" ")[1])
    #print "%s %s" % (N, K)
    ans = get_node_div(K, N)
    ans2 = get_node2(K, N)
    if (ans[0] != ans2[0]) or (ans[1] != ans2[1]):
        print "Failed on inputs %s, %s" % (K, N)
        print 'Case #%s: (%s, %s) vs BF: (%s, %s)' % (caseno, ans[0], ans[1], ans2[0], ans2[1])

    caseno = caseno + 1

"""
T = int(lines[0])
caseno = 1
for line in lines[1:T+1]:
    line = line.lstrip().rstrip()
    N = int(line.split(" ")[0])
    K = int(line.split(" ")[1])
    #print "%s %s" % (N, K)
    ans2 = get_node_div(K, N)
    print 'Case #%s: %s %s' % (caseno, ans2[0], ans2[1])

    caseno = caseno + 1
