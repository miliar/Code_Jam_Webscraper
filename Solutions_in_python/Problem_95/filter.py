from string import lowercase
import sys

inputfile = open(sys.argv[1], 'rU')

###google2eng = {'y':'a', 'e':'o', 'q':'z'}

google2eng = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm'}

freeletters = set(lowercase)
for google, english in google2eng.iteritems():
    freeletters.discard(english)


T = int(inputfile.readline())
lines = []
for i in xrange(T):
    lines.append(inputfile.readline().rstrip())

solved = False
while not solved:
    solved = True
    for i, line in enumerate(lines):
        output = []
        for word in line.split():
            english = ""
            for char in word:
                if char in google2eng:
                    english += google2eng[char]
                else:
                    solved = False
                    english += char.upper()

            if english.islower():
                output.append(english)
            else:
                print english
                print " ".join(freeletters)
                
                translation = raw_input("unknown word line %d> " % i)
                if not translation:
                    continue

                new_info = set()
                for i, c in enumerate(english):
                    if c.isupper():
                        google = c.lower()
                        english = translation[i]
                        if google in google2eng and google2eng[google] != english:
                            print "Warning!", google, "=>", google2eng[google]
                            print "and you want", google, "=>", english
                        if english not in freeletters and english not in new_info:
                            print "Warning!", english, "google2eng is not a bijection!"
                        google2eng[google] = english
                        freeletters.discard(english)
                        new_info.add(english)


out = open('output.txt','w')

for i,line in enumerate(lines):
    new_line = ""
    for c in line:
        if c in google2eng:
            new_line += google2eng[c]
        else:
            new_line += c
    result = "Case #%d: %s" % (i + 1, new_line)
    print result
    out.write(result + "\n")
