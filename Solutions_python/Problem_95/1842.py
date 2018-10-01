def googlerese(filename):
    try:
        f = file(filename, 'r')
    except:
        print "Could not open the file"
        return
    
    googleDic = {'a':'y', 'b':'h', 'c':'e', 'd':'s', 'e':'o','f':'c', 'g':'v',
                 'h':'x', 'i':'d', 'j':'u', 'k':'i', 'l':'g', 'm':'l', 'n':'b', 'o':'k',
                 'p':'r', 'q':'z', 'r':'t', 's':'n', 't':'w', 'u':'j', 'v':'p', 'w':'f',
                 'x':'m', 'y':'a', 'z':'q', ' ':' ', '\n':'\n'}
    
    lines = f.readlines()
    num = int(lines[0])
    lines = lines[1:]
    counter = 1
    myOutput = ''
    
    for line in lines:
        myLine = ''
        for char in line:
            myLine = myLine + googleDic[char]
        myOutput = myOutput + 'Case #' + str(counter) + ': ' + myLine
        counter = counter + 1    
        
    out = file('myOutput.txt', 'w')
    out.write(myOutput)
    
    
    