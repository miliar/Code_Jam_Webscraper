import os, sys


d = {'a' : 'y' ,
     'b' : 'h',
     'c':'e',
     'd':'s',
     'e':'o',
     'f':'c',
     'g':'v',
     'h':'x',
     'i':'d',
     'j':'u',
     'k':'i',
     'l':'g',
     'm':'l',
     'n':'b',
     'o':'k',
     'p':'r',
     'q':'z',
     'r':'t',
     's':'n',
     't':'w',
     'u':'j',
     'v':'p',
     'w':'f',
     'x':'m',
     'y':'a',
     'z':'q',
     ' ': ' '}


if __name__ == "__main__":
    #run main 
    lines = open( "A-small-attempt2.in" ).readlines()
    #lines = sys.stdin.readlines()
    out = open( "A-small-attempt2.out" , 'w' )
    x = int( lines[0] )
    count = 0
    output = "Case #{0}: {1}\n"
    for G in lines[1:]:
        if count == x:
            break
        count += 1
        translation = ""
        for char in G.strip( '\n' ):
            translation += d[char]
        out.write( output.format( count, translation ) )

    out.close()
