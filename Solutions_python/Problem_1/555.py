FNAME = "A-large.in"

class Case(object):
    def __init__(self, engines, queries):
        self.engines = engines
        self.queries = queries
    def __str__(self):
        print "Engines: "
        for engine in self.engines:
            print engine
        print "Queries: "
        for query in self.queries:
            print query
        return ""

class Memoize(object):
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, *args):
        import cPickle
        str = cPickle.dumps(args)
        if not self.memo.has_key(str):
            self.memo[str] = self.fn(*args)
        return self.memo[str]

def getfreqs(l, engines):
    freqs = {}
    for engine in engines:
        freqs[engine] = 0
    for elem in l:
        freqs[elem] += 1
    return freqs

def getorderedfreqs(l, engines):
    return sorted(getfreqs(l, engines).items(), key = lambda x: x[1])

def getminelems(queries, engines):
    ordfreqs = getorderedfreqs(queries, engines)
    i = 0
    minfreq = ordfreqs[0][1]
    minelems = []
    while i < len(ordfreqs) and ordfreqs[i][1] == minfreq:
        minelems.append(ordfreqs[i][0])
        i += 1
    return minelems
        
def shorten(l):
    if not l:
        return []
    acc = [l[0]]
    for elem in l[1:]:
        if not elem == acc[-1]:
            acc.append(elem)
    return acc

def nswitches(queries, engines):
    if not queries:
        return 0
    queries = shorten(queries)
    return getswitches(queries, engines)

def nextoccur(queries, engine):
    for i, query in enumerate(queries):
        if query == engine:
            return i
    return len(queries)

def getswitches(queries, engines):
    s = 0
    i = 0
    while i < len(queries):
        occur = max(nextoccur(queries[i:], engine) for engine in engines)
        i += occur
        if not queries[i:]:
            break
        s += 1
    return s

def nswitches_recur(queries, engines, curr_engine):
    l = len(queries)
    if not queries:
        return 0
    for i, query in enumerate(queries):
        if query == curr_engine:
            return min((1 + nswitches_recur(queries[i + 1:], engines, engine)) for engine in engines if engine != curr_engine)
        elif i == l - 1:
            return 0

def parse(lines):
    cases = []
    i = 1
    while i < len(lines):
        nengines = int(lines[i])
        i += 1
        end = i + nengines
        engines = lines[i:end]
        i = end
        nqueries = int(lines[i])
        i += 1
        end = i + nqueries
        queries = lines[i:end]
        i = end
        engines = map(lambda x: x.replace('\n', ''), engines)
        queries = map(lambda x: x.replace('\n', ''), queries)
        cases.append(Case(engines, queries))        
    return cases

cases = parse(file(FNAME).readlines())

answers = [nswitches(case.queries, case.engines) for case in cases]

#print str(cases[9])
#print nswitches(cases[9].queries, cases[9].engines)

#answers = []
#for i, case in enumerate(cases):
#    answers.append(nswitches(case.queries, case.engines))
#    print "Case #%d: %d" %(i + 1, answers[i]) 

file(FNAME + ".out", "w").writelines("Case #" + str(index + 1) + ": " + str(item) + "\n" for index, item in enumerate(answers))
            
