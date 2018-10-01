d = {'y':'a',
     'n':'b',
     'f':'c',
     'i':'d',
     'c':'e',
     'w':'f',
     'l':'g',
     'b':'h',
     'k':'i',
     'u':'j',
     'o':'k',
     'm':'l',
     'x':'m',
     's':'n',
     'e':'o',
     'v':'p',
     'z':'q',
     'p':'r',
     'd':'s',
     'r':'t',
     'j':'u',
     'g':'v',
     't':'w',
     'h':'x',
     'a':'y',
     'q':'z',
     ' ':' ',
     '\n':'\n'}
f = open("A-small-attempt0.in")
output = open("output","w")
i = 0
for line in f:
    if not i:
        line = line.split()
        T = int(line[0])
        
    else :
        if i > T:
            break
        else: 
            temp = ""
            for l in line:
                temp += d[l]
            output.write("Case #"+str(i)+": "+temp)
            
    i += 1     
output.close()
f.close()    
