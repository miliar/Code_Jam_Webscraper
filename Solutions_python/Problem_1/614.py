#!/usr/bin/python

N = input()


#print N, S


for i in range(N):

    S = input()
    engines = []
    for k in range(S):
        s = raw_input()
        engines.append(s)
    #print "Engines are"
    #print engines
    #print ""

    queries = []
    Q = input()

    for j in range(Q):
        q = raw_input()
        queries.append(q)

    remainder={}
    for e in engines:
        remainder[e] = True 


    #print remainder
    # loop to figure out long strings
    switches = 0
    #print "Queries are"
    #print queries 
    #print ""
    for q in queries:
        if remainder.has_key(q):
            if len(remainder) is 1:
                switches += 1  
                # restore remainder
                remainder={}
                for e in engines:
                    remainder[e] = True 
                remainder.pop(q)
            else:
                remainder.pop(q)
        #print remainder

    print 'Case #'+str(i+1)+": "+str(switches)
