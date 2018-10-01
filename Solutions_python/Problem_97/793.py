def num( a, b ):
    cntr = 0
    num1 = a
    while ( num1 <= b ):
        checker = set()
        s = str(num1)
        j = 1
        while ( j < len(s) ):
            d = s[j:] + s[:j]
            num2 = int(d)
            if d[:1] != "0" and num2 <= b and num1 < num2:
                checker.add( num2 )
            j += 1
        cntr += len( checker ) 
        num1 += 1
    return cntr

# print num(1, 9)
# print num(10, 40)
# print num(100, 500)
# print num(1111, 2222)

f = open( "input", "r")
cntr = int( f.readline() )

j = 1
for i in range(cntr):
    data = f.readline().split(" ")
    print "Case #" + str(j) + ": " + str( num( int(data[0]), int(data[1]) ) )
    j += 1
