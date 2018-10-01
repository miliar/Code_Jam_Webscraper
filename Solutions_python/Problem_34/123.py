#!/usr/bin/python

L,D,N = [int(x) for x in raw_input().split()]

# build prefix tree using nested dicts
prefix_tree = {}
for _ in xrange(D):
    word = raw_input()
    cur = prefix_tree
    for c in word:
        if c not in cur:
            cur[c] = {}
        cur = cur[c]

# solve each test case
for t in xrange(N):
    test_str = raw_input()
    # parse test str
    test_case = []
    pos = 0
    for i in xrange(L):
        if test_str[pos] != '(':
            test_case.append([test_str[pos]])
            pos+=1
        else:
            options=[]
            pos+=1 # skip opening parenthesis
            while test_str[pos] != ')':
                options.append(test_str[pos])
                pos+=1
            pos+=1 # skip closing parenthesis
            test_case.append(options)
    # search the prefix tree
    active = [prefix_tree]
    #print "active = ", active
    for i in xrange(L):
        new_active = []
        #print test_case[i]
        for node in active:
            for opt in test_case[i]:
                if opt in node:
                    new_active.append(node[opt])
        active = new_active
        #print "active = ", active
    print "Case #%d: %d"%(t+1, len(active))    



    





