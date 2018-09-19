test = """3
elcomew elcome to code jam
wweellccoommee to code qps jam
welcome to codejam"""


pattern = "welcome to code jam"


test = file( "C-small-attempt0.in" ).read()

doc = test.split( "\n" )
N = int( doc[0] )

samples = []
for n in range( N ):
    samples.append( doc[1 + n] )

#print samples
index = 1
for s in samples:
    oldarray = [0] * len( s )
    darray = [0] * len( s )
    for x in range( len( pattern ) ):
        key = pattern[-1 - x]
        v = 0
#        print key
        for b in range( len( s ) ):
            if s[-1 - b] == key:
                if - 1 - b + 1 < len( s ):
                    if x == 0:
                        darray[-1 - b] = darray[-1 - b + 1] + 1
                    else:
                        darray[-1 - b] = darray[-1 - b + 1] + oldarray[-1 - b]
                else:
                    darray[-1 - b] = oldarray[-1 - b]
            else:
                if - 1 - b + 1 < len( s ):
                    darray[-1 - b] = darray[-1 - b + 1]
                else:
                    darray[-1 - b] = 0

#            print darray
#        break
#        print key, darray

        oldarray = darray
        darray = [0] * len( s )

    value = str( oldarray[0] % 1000 )

    print "Case #%s: %s" % ( index, "0" * ( 4 - len( value ) ) + value )
    index += 1
#        print darray
#    break


