'''
Created on 21/05/2011

@author: joan
'''
import sys

if __name__ == '__main__':
    infile = sys.stdin
    #infile = open("/home/joan/workspace/codejam1B/src/mini.txt")
    ncases = int(infile.readline())
    
    #print "cases: ", ncases
    
       
    for case in range(ncases):
        nteams = int(infile.readline())
        
        wpmatrix = []
        resmatrix = []
        for n in range(nteams):
            
            lres = []
            res = infile.readline().replace('\n','');
            
            ngames = 0
            nwin = 0
                
            for m in range(len(res)):
                
                #print res[m], "-",
                if res[m] != '.':
                    lres.append((m,int(res[m])))
                    if res[m] == "1":
                        nwin += 1
                    ngames += 1
            resmatrix.append(lres)
            
            wpmatrix.append((nwin,ngames))
            
            
            
        #print resmatrix
        
        #Compute WP
        lowp = []
        lwp = []
        
        for n in range(nteams):
            wp = 0
            owp = 0
            oowp = 0 
            
            wp = (float(wpmatrix[n][0])/wpmatrix[n][1])
            
            lwp.append(wp)
            owpcount = 0
            for (t,r) in resmatrix[n]:
                
                nwin = wpmatrix[t][0]
                nplay = wpmatrix[t][1]-1
                if r == 0:
                    nwin -= 1
                
             #   print "owp (%d, %d) = %f (%d,%d)"% (n,t, float(nwin/nplay),nwin,nplay)
                
                owpcount+=float(nwin)/nplay    
            
            #print owpcount, len(resmatrix[n])       
            owp=owpcount/len(resmatrix[n])
            
            lowp.append(owp)
            
        print "Case #%d:" % (case+1)
        for n in range(nteams):
                oowp = 0
                for (t,r) in resmatrix[n]:
                                      
                    oowp+=lowp[t]
                     
                oowp /= len(resmatrix[n])
                
                
                rpi = 0.25*lwp[n] + 0.5*lowp[n]+0.25*oowp
                #print n, lwp[n], lowp[n], oowp,rpi
                print rpi
                
                