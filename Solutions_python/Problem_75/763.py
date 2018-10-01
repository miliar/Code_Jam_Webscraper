def merge( combine, oppose, base ):
    temp = []
    for i in range( 0, len( base ) ):
        temp.append( base[i] )
        if i == 0:
            continue
        j = 0
        while j < len( combine ):
            k = 1
            while k < len( temp ): 
                if temp[k-1] == combine[j][0] and temp[k] == combine[j][1]:
                    del temp[k-1]
                    del temp[k-1]
                    temp.insert( k-1, combine[j][2] )
                    j = 0
                    k = 1
                elif temp[k-1] == combine[j][1] and temp[k] == combine[j][0]:
                    del temp[k-1]
                    del temp[k-1]
                    temp.insert( k-1, combine[j][2] )
                    j = 0
                    k = 1
                k+=1
            j+=1
        l = 0
        while l < len( oppose ):
            try:
                temp.index( oppose[l][0] )
                temp.index( oppose[l][1] )
                temp = []
                l = 0
            except:
                l += 1
                continue
            l +=1
    return temp

def invoke( line ):
    arr = line.rstrip().split( ' ' )
    
    ncombine = int( arr[0] )
    combine = []
    for i in range(1, ncombine + 1):
        combine.append( [ arr[i][0], arr[i][1], arr[i][2] ] )
    
    noppose = int( arr[ncombine+1] )
    oppose = []
    for i in range(ncombine + 2, ncombine + noppose + 2):
        oppose.append( [ arr[i][0], arr[i][1] ])
    
    nbase = int( arr[ncombine+noppose+2] )
    base = list( arr[ncombine+noppose+3] )
    m = merge( combine, oppose, base )
    return m

def makeoutput( index, spell ):
    s = "Case #"+str(index)+": ["
    for i in range( 0, len( spell ) ):
        if i == len( spell ) - 1:
            s += spell[i]
        else:
            s += spell[i] + ', '
    return s + ']\n'

fout = open("output2.txt", "w")
file = []
for line in open( 'sample2.txt', 'r' ):
    file.append( line )
    
ntest = int( file[0] )
for i in range( 1, ntest+1 ):
    spell = invoke( file[i] )
    fout.write( makeoutput(i, spell ) )
