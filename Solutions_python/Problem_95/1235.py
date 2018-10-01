'''
Created on 14/apr/2012

@author: matteo
'''

maps = dict()

    

def mapping(input,output):
    for i in xrange(len(input)):
        ch = input[i]
        if ch != ' ':
            maps[ch] = output[i]

def convert(s):
    o = ''
    for i in xrange(len(s)):
        ch = s[i]
        if ch == ' ':
            o += ' '
        else:
            o += maps[ch]
    return o

def test(ifp):
    nrows = int(ifp.readline())
    ofp = open("../speaking/out.txt" ,"w")
    for i in xrange(1,nrows+1):
        line = (ifp.readline().strip())        
        msg = "Case #%d: %s" % (i,convert(line))
        print msg
        ofp.write(msg + '\n')
    ofp.close() 

        

if __name__ == "__main__":
    i1 = 'ejp mysljylc kd kxveddknmc re jsicpdrysi'
    o1 = 'our language is impossible to understand'
    i2 = 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
    o2 = 'there are twenty six factorial possibilities'
    i3 = 'de kr kd eoya kw aej tysr re ujdr lkgc jv'
    o3 = 'so it is okay if you want to just give up'
    mapping(i1,o1)
    mapping(i2,o2)
    mapping(i3,o3)
    print maps
    maps['q']='z'
    maps['z']='q'    
    
    
    ifilename = '../speaking/A-small-attempt2.in' # sys.argv[1]
    if ifilename != "":
        print ifilename
        ifp = open(ifilename, "r")        
        test(ifp)      
        ifp.close()
    