from __future__ import division
import time
#t0=time.clock()

t = int(raw_input())  # read a line with a single integer
for tr in xrange(1, t + 1):
    N, R, O, Y, G, B, V = [int(s) for s in raw_input().split(" ")]

    if (R==0) and (G==0) and (Y==0) and (V==0) and (B==O):
        sofar=['BO']*O
        sofarstr=''.join(sofar)
        print "Case #{}: {}".format(tr, sofarstr)
    elif (R==0) and (G==0) and (Y==V) and (B==0) and (O==0):
        sofar=['YV']*Y
        sofarstr=''.join(sofar)
        print "Case #{}: {}".format(tr, sofarstr)
    elif (R==G) and (V==0) and (Y==0) and (O==0) and (B==0):
        sofar=['RG']*G
        sofarstr=''.join(sofar)
        print "Case #{}: {}".format(tr, sofarstr)

        
    elif ((O>=B) and (O>=1)) or ((G>=R) and (G>=1)) or ((V>=Y) and (V>=1)):
        print "Case #{}: {}".format(tr, 'IMPOSSIBLE')
        
    else:
        newr=R-G
        newy=Y-V
        newb=B-O
        #print newr,newb,newy
        if (newr>newb+newy) or (newb>newr+newy) or (newy>newb+newr):
            print "Case #{}: {}".format(tr, 'IMPOSSIBLE')
        else:            
            r1=['R','G']*G
            y1=['Y','V']*V
            b1=['B','O']*O
            
            mm=max(newr,newb,newy)
            
            if newr==mm:
                cyc=newy+newb-newr
                newr-=cyc
                newy-=cyc
                newb-=cyc
                mid=['R','Y','B']*cyc
                end=['R','Y']*newy+['R','B']*newb
            elif newy==mm:
                cyc=newr+newb-newy
                newr-=cyc
                newy-=cyc
                newb-=cyc
                mid=['Y','B','R']*cyc
                end=['Y','R']*newr+['Y','B']*newb
            else:
                cyc=newr+newy-newb
                newr-=cyc
                newy-=cyc
                newb-=cyc
                mid=['B','Y','R']*cyc
                end=['B','R']*newr+['B','Y']*newy
            
            sofar=mid+end+['R','Y','B']
            rindex=sofar.index('R')
            sofar=sofar[:rindex]+r1+sofar[rindex:]
            yindex=sofar.index('Y')
            sofar=sofar[:yindex]+y1+sofar[yindex:]
            bindex=sofar.index('B')
            sofar=sofar[:bindex]+b1+sofar[bindex:]
            
            sofar=sofar[:N]
        
            sofarstr=''.join(sofar)
       
            print "Case #{}: {}".format(tr, sofarstr)
#print time.clock()-t0