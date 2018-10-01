#!/usr/bin/python
import sys

infile = "C-small-attempt0.in"

f    = open( infile )
fout = open( infile.replace("in","out") , "w" )

M = { "ij":("k",1), "ji":("k",-1), "ik":("j",-1), "jk":("i",1), "ki":("j",1), "kj":("i",-1), "ii":("",-1),"jj":("",-1), "kk":("",-1), }


def mult( a, b ):    
    
    if a[0] and b[0] :
        p= M[a[0]+b[0]]
    else:
        p = (a[0]+b[0],1)
    
    
    return (p[0],p[1]*a[1]*b[1])

have_i, have_ij, have_ijk = False, False, False

def mults( chars ):
    global have_i, have_ij, have_ijk
    have_i, have_ij, have_ijk = False, False, False

    w = ("",1)

    for c in chars:
        w = mult ( w , (c,1) )
        
        #print w
        if w == ("i",1)              : have_i = True
        if w == ("k",1) and have_i   : have_ij = True
        if w == ("", -1) and have_ij : have_ijk = True
    return w



def solve( s ):
    #print s
    prod = mults( s )
    
    #print s , " -> ", prod, have_ijk

    if prod  != ("",-1) :
        return "NO"
    if not have_ijk : return "NO"

    else :
        return "YES"

        

#print mult( ("i",1), ("j",1) )
#print mult( ("j",1), ("i",1) )

#mults( "ijk") 
#sys.exit()

T = int ( f.readline() )

for i in range( 1, T+1 ):
    
    L,X= [ int(x) for x in f.readline().split() ]
    s = f.readline().strip()

    ans = solve( s*X) 
    


    print "Case #%d: %s" % (i, ans)
    fout.write( "Case #%d: %s\n" % (i, ans))

fout.close()
