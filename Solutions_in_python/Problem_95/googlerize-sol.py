

d = {'\n': '\n', ' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'q': 'z', 'z': 'q'}

def decode(entree):
    s=""
    for c in entree:
        s+=d[c]
    
    return s

with open("input.txt") as f:
    i =1
    lines = f.readlines()
    for line in lines[1:]:
        print "Case #"+str(i)+": "+decode(line[:-1])
        i+=1
