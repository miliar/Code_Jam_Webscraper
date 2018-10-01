translate = {'y': 'a', 'n': 'b', 'f': 'c', 'i': 'd', 'c': 'e', 'w': 'f', 'l': 'g', 'b': 'h', 'k': 'i', 'u': 'j', 'o': 'k', 'm': 'l', 'x': 'm', 's': 'n', 'e': 'o', 'v': 'p', 'z': 'q', 'p': 'r', 'd': 's', 'r': 't', 'j': 'u', 'g': 'v', 't': 'w', 'h': 'x', 'a': 'y', 'q': 'z', ' ': ' '}

def trnslt(c):
    print '# '+c
    if c=='\n':
        ret = ''
    else:
        ret = translate[c]
    return ret

count = 1
infile = open('a')
outfile = open('b', 'w')   # write mode; creates the file
infile.readline()
for line in infile:
    outfile.write('Case #'+str(count)+': ')
    outfile.write(''.join(map(trnslt, list(line))))
    outfile.write('\n')
    count += 1
infile.close()                   # not strictly required; done automatically
outfile.close()

