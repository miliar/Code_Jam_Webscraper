#/usr/bin/python

#file = open("A.in")
#file = open("A-small-attempt0.in")
#file = open("A-small-attempt2.in")
file = open("A-large.in")

lines = iter(map(lambda line: line.rstrip("\n"), file.readlines()))

T = int(lines.next())

for t in xrange(0, T):
    code = lines.next().strip(" ")
    
    symbols = set(code)
    meaning = {}
    
    base = max(2, len(symbols))
    
    possibs = list(reversed(xrange(0, base)))
    
    possibs[len(possibs)-1] = 1
    possibs[len(possibs)-2] = 0
    
    if len(symbols) == 1:
        possibs = [1]

    for x in xrange(0, len(code)):
        char = code[x]
        if not meaning.has_key(char):
            meaning[char] = possibs.pop()
    
    number = sum([meaning[char] * base**(digit) for digit,char in enumerate(reversed(code))])
        
    
    print "Case #%i: %i" % (t+1, number)

