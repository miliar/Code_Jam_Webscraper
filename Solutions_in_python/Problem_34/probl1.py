l, d, n = 0,0,0
dic = []
words = []

with open("a-large.in") as f:
    l, d, n = [int(e) for e in f.readline().split(" ")]
    #print l, d, n
    dic = [f.readline().strip() for i in range(d)]
    #print dic
    words = [f.readline().strip() for i in range(n)]
    #print words
    
tree = {}

def build(ws):
    if ws == ['']: return {}
    
    tr = {}

    for word in ws:
        try:
            tr[word[0]].append(word[1:])
        except:
            tr[word[0]] = [word[1:]]
      
    for e in tr:
        tr[e] = build(tr[e])      
    return tr
    
tree = build(dic)
#print tree

def match(tr, word):
    #print "Enter match======================"
    #print "Tree:", tr, "Word:", word
    matches = 0
    ltrs = []
    i = 0
    if word[0] == '(':
        while 1:
            c = word[i]
            if c == ')': break
            ltrs.append(c)
            i += 1
    else:
        ltrs = [word[0]]
        
    for l in ltrs:
        if l in tr:
            if tr[l] == {}:
                matches += 1
            else:
                matches += match(tr[l], word[i+1:])
    
    return matches
    
out = open("output-large.txt","w")
for (i,w) in enumerate(words):
    print >> out, "Case #%d: %d" % (i+1, match(tree, w))
    
out.close()
                
            
            
    