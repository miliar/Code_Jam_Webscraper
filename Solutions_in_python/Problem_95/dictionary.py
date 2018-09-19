import sys
dictionary = {' ': ' ', 'a': 'y', 'c': 'f', 'b': 'n', 'e': 'c', 'd': 'i', 'g': 'l', 'f': 'w', 'i': 'k', 'h': 'b', 'k': 'o', 'j': 'u', 'm': 'x', 'l': 'm', 'o': 'e', 'n': 's', 'p': 'v', 's': 'd', 'r': 'p', 'u': 'j', 't': 'r', 'w': 't', 'v': 'g', 'y': 'a', 'x': 'h', 'z': 'q', 'o': 'e', 'q': 'z'}

dictionary = dict([(v,k) for k,v in dictionary.items()])

input = sys.argv[1]
result = open("result.txt", "w")

for i,line in enumerate(open(input).xreadlines()):
    if i == 0:
        continue
    oline = ["Case #%d: " %i]
    for c in line:
        if c == "\n":
            oline.append(c)
        else:
            oline.append(dictionary.get(c, "_"))
    result.write( "".join(oline))
result.close()
        

