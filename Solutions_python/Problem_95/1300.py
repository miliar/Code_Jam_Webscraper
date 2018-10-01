import sys

input=[
"ejp mysljylc kd kxveddknmc re jsicpdrysi",
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
"de kr kd eoya kw aej tysr re ujdr lkgc jv"]

output=[
"our language is impossible to understand",
"there are twenty six factorial possibilities",
"so it is okay if you want to just give up"]


def get_map(input, output):
    map = {}
    assert len(input) == len(output)
    for i in range(len(input)):
        src = input[i]
        trg = output[i]
        assert len(src) == len(trg)
        for c in range(len(src)):
            if src[c] in map:
                assert map[src[c]] == trg[c], ([src[c]], trg[c])
            map[src[c]] = trg[c]
    map['q'] = 'z'
    allchars = []
    for i in range(26):
        z = chr(ord('a')+i)
        allchars.append(z)
    allchars2 = allchars[:]
    for i in range(26):
        z = chr(ord('a')+i)
        if z in map:
            m = map[z]
            allchars.remove(m)
            allchars2.remove(z)
    map[allchars2[0]] = allchars[0]
#    for key in sorted(map.keys()):
#        print `key`, `map[key]`
#    print len(map), len(set(map.keys())), len(set(map.values()))
    return map

def main(filename):
    map = get_map(input, output)
    f = open(filename)
    lines = f.readlines()
    f.close()
    T = int(lines[0])
    for i in range(1, T+1):
        line = lines[i]
        
        line = line.strip()
        new_line = []
        for c in line:
            new_c = map[c]
            new_line.append(new_c)
        res = ''.join(new_line)
        
        print "Case #%d: %s" % (i, res)

if __name__ == '__main__':
    main(sys.argv[1])