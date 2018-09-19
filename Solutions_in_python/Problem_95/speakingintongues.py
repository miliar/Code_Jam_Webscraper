submap = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q', 'q' : 'z'}
n = int(raw_input(''))
inp = []
for i in range(0,n):
    inputstring = raw_input("")
    inp.append(inputstring)
for i in range(0,n):
    print "Case #" + str(i+1) + ":  ",
    for k in range(0,len(inp[i])):
        print "\b" + submap[inp[i][k]],
    print ''
