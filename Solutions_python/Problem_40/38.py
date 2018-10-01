import sys
import psyco
psyco.full()

test = """2
3
(0.5 cool
  ( 1.000)
  (0.5 ))
2
anteater 1 cool
cockroach 0
13
(0.2 furry
  (0.81 fast
    (0.3)
    (0.2)
  )
  (0.1 fishy
    (0.3 freshwater
      (0.01)
      (0.01)
    )
    (0.1)
  )
)
3
beaver 2 furry freshwater
trout 4 fast freshwater fishy rainbowy
dodo 1 extinct
"""
#test = sys.stdin.read()


test = open( "A-small-attempt0 (1).in" ).read()

class TreeNode:
    def __init__( self ):
        self.P = None
        self.left = None
        self.right = None
        self.feature = None

    def count( self, features ):
        if self.feature in features:
            if self.left:
                return self.P * self.left.count( features )
            else:
                return self.P
        else:
            if self.right:
                return self.P * self.right.count( features )
            else:
                return self.P

ofile = open( "log.txt", 'w' )
offset = 0
def ParseTree( body , root ):
#    print body, root
    ofile.write( str( ( body, root ) ) + "\n" )
    global offset

    rindex = body.index( "(" )
    try:
        r2index = body.index( "(", rindex + 1 )
    except:
        r2index = 999999999

    lindex = body.index( ")", rindex )

    if lindex < r2index:
        # it's a root
#        print body, rindex, lindex
        P = float( body[rindex:lindex].replace( "(", "" ) )
        root.P = P
        return body[lindex:]
    else:
        content = body[rindex: r2index].split( " " )
        P = float( content[0].replace( "(", "" ) )
        feature = content[1].strip()
        node = TreeNode()
        node.P = P
        node.feature = feature

        root.P = P
        root.feature = feature
        root.left = TreeNode()

        leftbody = ParseTree( body[r2index:], root.left )

        root.right = TreeNode()

        return ParseTree( leftbody, root.right )

lines = test.split( "\n" )

N = int( lines[0] )

offset = 1
for n in range( N ):
    L = int( lines[offset] )
    tree = lines[offset + 1: offset + 1 + L ]
    A = int( lines[offset + 1 + L] )
#    print L, tree, A

    tree = "".join( tree )
#
    root = TreeNode()
    ParseTree( tree, root )

    print "Case #%s:" % ( n + 1 )

    for x in range( A ):
        z = lines[offset + 2 + L + x].split( " " )
        features = z
#        print features,
        print root.count( features )


    offset += 2 + L + A



