d = {
     'y' : 'a',
     'n' : 'b',
     'f' : 'c',
     'i' : 'd',
     'c' : 'e',
     'w' : 'f',
     'l' : 'g',
     'b' : 'h',
     'k' : 'i',
     'u' : 'j',
     'o' : 'k',
     'm' : 'l',
     'x' : 'm',
     's' : 'n',
     'e' : 'o',
     'v' : 'p',
     'z' : 'q',
     'p' : 'r',
     'd' : 's',
     'r' : 't',
     'j' : 'u',
     'g' : 'v',
     't' : 'w',
     'h' : 'x',
     'a' : 'y',
     'q' : 'z',
     ' ' : ' '
     }

out = ''
lineCounter = 1
with open('input/1sample.txt', 'r') as f:
    f.readline()
    while 1:
        line = f.readline()
        if not line:
            break
        out += "Case #"
        out += str(lineCounter)
        lineCounter += 1
        out += ": "
        for i in line:
            if '\n' not in i:
                out += d[i]
        out += '\n'
print out

fo = open('q1output', "w")
fo.write(out)
fo.close()