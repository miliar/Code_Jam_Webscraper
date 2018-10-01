import time

in_file = "A-large.in"
out_file = "A-large.out"

def start():
    f_in = file(in_file, "r")
    f_out = file(out_file, "w")    
    parts = f_in.readline().strip().split(" ")
    L = int(parts[0])
    D = int(parts[1])
    N = int(parts[2])

    words = []
    for i in xrange(D):
        w = f_in.readline().strip()
        words.append(w)

    #print words

    t1 = time.time()
    for i in xrange(N):
        pattern = f_in.readline().strip()
        #print pattern
        n = getNumOfWords(pattern, words, L, D)
        f_out.write("Case #" + str(i+1) + ": " + str(n) + "\n")

    f_in.close()
    f_out.close()
    
def getNumOfWords(pattern, words, L, D):
    parts = []
    inside = False
    part = set()
    for i in xrange(len(pattern)):
        p = pattern[i]
        if p == "(":
            inside = True
        elif p == ")":
            inside = False
            parts.append(part)
            part = set()
        elif inside == False:
            parts.append(set(p))
        else:
            part.add(p)

    #print parts

    count = 0
    for i in xrange(D):
        word = words[i]
        #print word
        #print parts
        if isWordInParts(word, parts, L):
            #print "True"
            count = count +1

    #print count
    return count
        

def isWordInParts(word, parts, L):
    for i in xrange(L):
        ch = word[i]
        if not parts[i].__contains__(ch):
            return False                    
    return True

t1 = time.time()   
start()
print "total time: " + str(time.time()-t1)
           
