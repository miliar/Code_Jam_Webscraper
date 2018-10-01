import re
from sys import argv
from dg import trace
zrl = lambda xs: zip(range(len(xs)), xs)

#@trace
def mkdirs(haves, wants):
    dirs = {}
    for h in haves:
        for p in prefixes(h):
            dirs[p] = True
    havect = len(dirs)
    #print dirs, havect
    for w in wants:
        for p in prefixes(w):
            dirs[p] = True
    wantct = len(dirs)
    #print dirs, wantct
    return wantct - havect

#@trace
def prefixes(d):
    fixes = d[1:-1].split('/')
    return ['/' + '/'.join(fixes[:i]) for i in xrange(1,len(fixes)+1)]

def memoize(f):
    cache = {}
    def real_f(*args):
        def do_the_work ():
            product = f(*args)
            cache[tuple(args)] = product
            return product
        return cache.get(tuple(args), do_the_work())
    return real_f

def parse_ints(count, line):
    gs = ('''(\d+)''',) * count
    expr = '''^\s*''' + ('''\s*'''.join(gs)) + '''\s*$'''
    m = re.search(expr, line)
    return [int(x) for x in m.groups()]

lines = open(argv[1], 'r').readlines()
casecount = int(re.search('''^\s*(\d+)\s*$''', lines[0]).group(1))

i = 1
casesprocessed = 0
while i < len(lines):
    havect, wantct = parse_ints(2, lines[i])
    i += 1
    haves = lines[ i : i+havect ]
    i += havect
    wants = lines[ i : i+wantct ]
    i += wantct
    casesprocessed += 1
    print "Case #%d: %s" % (casesprocessed, mkdirs(haves, wants))




