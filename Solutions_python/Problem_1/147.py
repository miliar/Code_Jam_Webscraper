def parse_time(time_str):
    tokens = time_str.split(":")
    hr = int(tokens[0])
    min = int(tokens[1])
    return hr * 60 + min

def get_min(p_list):
    min = 0
    sum = 0
    for itm in p_list:
        sum = sum + int(itm[1])
        if sum < min:
            min = sum
    return min

def comp(a, b):
    if a[0] != b[0]:
        return a[0] - b[0]
    return b[1] - a[1]


f = open("c:/users/roy/Downloads/A-large.in")
#f = open("C:/Users/Roy/Documents/gcj/search/test.in")

nCnt = 0
lines = f.readlines()

nCnt = int(lines[0])
#print "There are %i test cases." % nCnt
nCase = 0

nLineNo = 1
for nCase in range(1, nCnt+1):
    list_a = []
    list_b = []
    cnt_engines = int(lines[nLineNo])
    nLineNo = nLineNo + 1
    engines = []
    for n in range(1, cnt_engines+1):
        engines.append(lines[nLineNo].strip())
        nLineNo = nLineNo +1
    cnt_searches = int(lines[nLineNo])
    nLineNo = nLineNo +1
    switches = 0
    engines_copy = list(engines)
    for n in range(1, cnt_searches+1):
        search = lines[nLineNo].strip()
        nLineNo = nLineNo +1
        if search in engines_copy:
            engines_copy.remove(search)
        if len(engines_copy) == 0:
            switches = switches + 1
            engines_copy = list(engines)
            engines_copy.remove(search)
            #print "Switching at search %i" % n
    print "Case #%i: %i" % (nCase, switches)
        
