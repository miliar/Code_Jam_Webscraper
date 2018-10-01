class Dict(object):
    def __init__(self):
        self.root = {}
        self.end = 0
    def __str__(self):
        return self.str('')
    def str(self,indent):
        ret = ''
        for key,val in self.root.iteritems():
            ret += indent+key+'\n'
            ret += self.root[key].str(indent+' ')
        return ret
    def insert(self,word):
        if word == "":
            self.end = 1
            return
        if word[0] not in self.root:
            self.root[word[0]] = Dict()
        self.root[word[0]].insert(word[1:])
    def count(self,query):
        if len(query)==0: return self.end
        sum = 0
        for letter in query[0]:
            if letter in self.root:
                sum += self.root[letter].count(query[1:])
        return sum
        
dictionary = Dict()

l,d,n = (int(i) for i in raw_input().split())

for _ in xrange(d):
    dictionary.insert(raw_input())

for i in xrange(n):
    line = raw_input()
    inside = False
    query = []
    for c in line:
        if c == '(':
            inside = True
            query.append([])
        elif c == ')': inside = False
        elif inside: query[-1].append(c)
        else: query.append([c])
    print "Case #%d: %d" % (i+1,dictionary.count(query))
