from sys import maxint as INF

fd = open('/home/amrik/Desktop/A-large.in', 'r')
s = fd.read()
fd.close()
s = s.split('\n')

class TestCase:
    def __init__(self, engines, queries):
        self.engines = engines
        self.queries = queries


cases = []

num_cases = int(s[0])
s = s[1:]

while len(s) > 0:
    if s[0] == '':
        s = s[1:]
        continue
    num_engines = int(s[0])
    engines = s[1:num_engines+1]
    num_queries = int(s[num_engines+1])
    queries = s[num_engines+2:num_engines+2+num_queries]
    c = TestCase(engines, queries)
    cases.append(c)
    s = s[num_engines+2+num_queries:]

counter = 0

for c in cases:
    counter +=1
    queries = c.queries
    engines = c.engines
    num_queries = len(queries)
    num_engines = len(engines)

    if num_queries == 0: # handle base case
        print 'Case #%d: %d' %(counter,0)
        continue

    block = [[0 for x in xrange(num_engines)] for level in xrange(num_queries+1)]

    current_level = 0
    
    while current_level < num_queries:

        current_level += 1 # move to next level

        for i in xrange(num_engines):
            s = engines[i]
            if s == queries[current_level-1]:
                # cant feed an engine to itself
                block[current_level][i] = INF
            else:
                other_guys = block[current_level-1]
                stored = other_guys[i]
                other_guys = [x+1 for x in other_guys] # add 1 for switch
                other_guys[i] = stored # no cost for switching if same
                block[current_level][i] = min(other_guys)

    real_cost = min(block[num_queries])
    print 'Case #%d: %d' %(counter,real_cost)

