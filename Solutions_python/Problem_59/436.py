'''
Created on 22 Mei 2010

@author: firman
'''
def contains(list, filter):
    for x in list:
        if filter(x):
            return True
    return False

if __name__ == '__main__':
    
    fin = open("A-large.in","r")
    fout = open("A-large.out","w")
    T = int(fin.readline());
    '''
    Logic here 
    '''
    
    for t in range(1,T+1) :
        count = 0
        line = fin.readline().split(" ")
        N = int(line[0])
        M = int(line[1])
        
        exist = {"/":{}}
        new = None
        
        for n in range(N) :
            #print n , 
            line = fin.readline().split("/")
            line[-1] = (line[-1].split("\n"))[:1][0] 
            #print "last",line[-1]
            #dir = line.split("/")
            line_long = len(line)
            now = exist["/"]
            for l in range (1,line_long):
                if ( not contains(now.keys(),lambda x: x == line[l] )):
                    now["%s"%line[l]] = {}
                now = now[line[l]] 
                
            
        #print "exist",exist
        
        for m in range (M):
 


            line = fin.readline().split("/")
            line[-1] = (line[-1].split("\n"))[:1][0] 

            #dir = line.split("/")
            line_long = len(line)
            now = exist["/"]
            for l in range (1,line_long):
                if ( not contains(now.keys(),lambda x: x == line[l] )):
                    now["%s"%line[l]] = {}
                    count = count+1
                now = now[line[l]] 
            
            
        #print count,exist
        fout.write( "Case #%s: %s\n"%(t,count))
    
    
    
    
    fout.close()
    fin.close()
    pass