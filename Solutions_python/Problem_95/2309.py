
file = open("/home/rahul/Documents/codeJam2012/A-small-attempt0.in",  "r")
fileOut = open("/home/rahul/Documents/codeJam2012/A-small-attempt0.out", "w") 
 
map = {}
map['a'] = 'y'
map['b'] = 'h'
map['c'] = 'e'
map['d'] = 's'
map['e'] = 'o'
map['f'] = 'c'
map['g'] = 'v'
map['h'] = 'x'
map['i'] = 'd'
map['j'] = 'u'
map['k'] = 'i'
map['l'] = 'g'
map['m'] = 'l'
map['n'] = 'b'
map['o'] = 'k'
map['p'] = 'r'
map['r'] = 't'
map['s'] = 'n'
map['t'] = 'w'
map['u'] = 'j'
map['v'] = 'p'
map['w'] = 'f'
map['x'] = 'm'
map['y'] = 'a'
map['q'] = 'z'
map['z'] = 'q'
map[' '] = ' '



n = int(file.readline())

for i in range(n):
    line = file.readline()
    resLine = 'Case #' + str(i+1) + ': '
    for i in range(len(line)):
        st = ''
        if line[i] == '\n':
            st = line[i]
            break
        resLine += map[line[i]]
#    print resLine
    fileOut.write(resLine + st) 

file.close()
fileOut.close()
