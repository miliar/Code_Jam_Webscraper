inputs = open("C:\Users\Jaychandran\Documents\A-small-attempt0.in", 'r')
inputs.seek(0,0)
N = int(inputs.readline())
for d in range(0,N):
    charlist = list(inputs.readline())
    charlist = charlist[:-1]
    words = []
    j = 0
    while j < len(charlist):
        word = ""
        while j< len(charlist) and charlist[j] != ' ':
            word += charlist[j]
            j += 1
        j +=1
        words.append(word)
    for j in range(0, len(words)):
        string = words[j]
        s = list(string)
        for i in range(0, len(s)):
            if s[i] == 'a':
                s[i] = 'y'
                continue
            if s[i] == 'b':
                s[i] = 'h'
                continue
            if s[i] == 'c':
                s[i] = 'e'
                continue
            if s[i] == 'd':
                s[i] = 's'
                continue
            if s[i] == 'e':
                s[i] = 'o'
                continue
            if s[i] == 'f':
                s[i] = 'c'
                continue
            if s[i] == 'g':
                s[i] = 'v'
                continue
            if s[i] == 'h':
                s[i] = 'x'
                continue
            if s[i] == 'i':
                s[i] = 'd'
                continue
            if s[i] == 'j':
                s[i] = 'u'
                continue
            if s[i] == 'k':
                s[i] = 'i'
                continue
            if s[i] == 'l':
                s[i] = 'g'
                continue
            if s[i] == 'm':
                s[i] = 'l'
                continue
            if s[i] == 'n':
                s[i] = 'b'
                continue
            if s[i] == 'o':
                s[i] = 'k'
                continue
            if s[i] == 'p':
                s[i] = 'r'
                continue
            if s[i] == 'q':
                s[i] = 'z'
                continue
            if s[i] == 'r':
                s[i] = 't'
                continue
            if s[i] == 's':
                s[i] = 'n'
                continue
            if s[i] == 't':
                s[i] = 'w'
                continue
            if s[i] == 'u':
                s[i] = 'j'
                continue
            if s[i] == 'v':
                s[i] = 'p'
                continue
            if s[i] == 'w':
                s[i] = 'f'
                continue
            if s[i] == 'x':
                s[i] = 'm'
                continue
            if s[i] == 'y':
                s[i] = 'a'
                continue
            if s[i] == 'z':
                s[i] = 'q'
                continue
        words[j] = "".join(s)

    number = str(d+1)
    case = "Case #"+number+": "+" ".join(words)
    print case


            


                
            
            
        
