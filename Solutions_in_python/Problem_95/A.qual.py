infile = open('M:\input1.in')
outfile = open('M:\output1.out', 'w', 0)
N = int(infile.readline())
for t in range(0, N):
    line = infile.readline()
    line = list(line)
    for i in range(0, len(line)):
        if line[i] == 'a':
            line[i] = 'y'
        elif line[i] == 'b':
            line[i] = 'h'
        elif line[i] == 'c':
            line[i] = 'e'
        elif line[i] == 'd':
            line[i] = 's'
        elif line[i] == 'e':
            line[i] = 'o'
        elif line[i] == 'f':
            line[i] = 'c'
        elif line[i] == 'g':
            line[i] = 'v'
        elif line[i] == 'h':
            line[i] = 'x'
        elif line[i] == 'i':
            line[i] = 'd'
        elif line[i] == 'j':
            line[i] = 'u'
        elif line[i] == 'k':
            line[i] = 'i'
        elif line[i] == 'l':
            line[i] = 'g'
        elif line[i] == 'm':
            line[i] = 'l'
        elif line[i] == 'n':
            line[i] = 'b'
        elif line[i] == 'o':
            line[i] = 'k'
        elif line[i] == 'p':
            line[i] = 'r'
        elif line[i] == 'q':
            line[i] = 'z'
        elif line[i] == 'r':
            line[i] = 't'
        elif line[i] == 's':
            line[i] = 'n'
        elif line[i] == 't':
            line[i] = 'w'
        elif line[i] == 'u':
            line[i] = 'j'
        elif line[i] == 'v':
            line[i] = 'p'
        elif line[i] == 'w':
            line[i] = 'f'
        elif line[i] == 'x':
            line[i] = 'm'
        elif line[i] == 'y':
            line[i] = 'a'
        elif line[i] == 'z':
            line[i] = 'q'
    outfile.write( "Case #{}: {}\n".format(t+1,"".join(line[:len(line)-1])))
infile.close()
outfile.close()
