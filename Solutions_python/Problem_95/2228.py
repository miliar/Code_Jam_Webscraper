'''
Created on Apr 13, 2012

@author: jpsantos
'''

map = {
"a":"y",
"b":"h",
"c":"e",
"d":"s",
"e":"o",
"f":"c",
"g":"v",
"h":"x",
"i":"d",
"j":"u",
"k":"i",
"l":"g",
"m":"l",
"n":"b",
"o":"k",
"p":"r",
"q":"z",
"r":"t",
"s":"n",
"t":"w",
"u":"j",
"v":"p",
"w":"f",
"x":"m",
"y":"a",
"z":"q"
}


input = open("small.txt","r")
output = open("out_a.txt","w")

tests = int(input.readline())
for t in range(tests):
    g = input.readline()
    output.write("Case #%d: "%(t+1))
    for c in g:
        if c == ' ':
            output.write(' ')
            print ' '
        elif c == '\n':
            output.write('\n')
            print '\n'
        else:
            output.write(map[c])
            print map[c]
    #output.write("\n")
    
input.close()
output.close()
            