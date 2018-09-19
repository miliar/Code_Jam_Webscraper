from UserString import MutableString
rp = open('input','r')
wp = open('output','w+')
i=30
j=0
write = ''
num = rp.readline()
while i>0:
    read = rp.readline()
    j=0
    write += 'Case #'+str(30-i+1)+': '
    while j < len(read):
        if read[j] == 'a':
            write += 'y'
        elif read[j] == 'b':
            write += 'h'
        elif read[j] == 'c':
            write += 'e'
        elif read[j] == 'd':
            write += 's'
        elif read[j] == 'e':
            write += 'o'
        elif read[j] == 'f':
            write += 'c'
        elif read[j] == 'g':
            write += 'v'
        elif read[j] == 'h':
            write += 'x'
        elif read[j] == 'i':
            write += 'd'
        elif read[j] == 'j':
            write += 'u'
        elif read[j] == 'k':
            write += 'i'
        elif read[j] == 'l':
            write += 'g'
        elif read[j] == 'm':
            write += 'l'
        elif read[j] == 'n':
            write += 'b'
        elif read[j] == 'o':
            write += 'k'
        elif read[j] == 'p':
            write += 'r'
        elif read[j] == 'q':
            write += 'z'
        elif read[j] == 'r':
            write += 't'
        elif read[j] == 's':
            write += 'n'
        elif read[j] == 't':
            write += 'w'
        elif read[j] == 'u':
            write += 'j'
        elif read[j] == 'v':
            write += 'p'
        elif read[j] == 'w':
            write += 'f'
        elif read[j] == 'x':
            write += 'm'
        elif read[j] == 'y':
            write += 'a'
        elif read[j] == 'z':
            write += 'q'
        elif read[j] == ' ':
            write += ' '
        j += 1
    write += '\n'
    #print write
    i -= 1
wp.write(write)
rp.close()
wp.close()
    
