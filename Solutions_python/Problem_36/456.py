f = open('C-small-attempt0.in')

lines = [line.strip('\n') for line in f.readlines()]

N = int(lines.pop(0))

msg = 'welcome to code jam'

count = 0

def findall(string, sub, listindex, offset):
    if (string.find(sub) == -1):
        return listindex
    else:
        offset = string.index(sub)+offset
        listindex.append(offset)
        string = string[(string.index(sub)+1):]
        return findall(string, sub, listindex, offset+1)

def search(s,line):
    global count
    i = len(s)
    if len(s) == 19:
        count += 1
        return
    
    l = msg[i]
    indices = findall(line,l,[],0)

    for index in indices:
        _s = s[:]
        _s.append(index)
        search(_s,line[index:])

s = []
for line,i in zip(lines,range(len(lines))):
    count = 0
    search(s, line)
    print 'Case #%i: %s'%(i+1, str(count)[-4:].zfill(4))
