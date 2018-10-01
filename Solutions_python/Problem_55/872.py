'''
Created on May 7, 2010

@author: Melvin Kanasseril
'''

if __name__ == '__main__':
    f=open("C-small-attempt0.in")
    f1=open("C-small.out","w")
    T=f.readline()
    T=int(T.strip())
    
    for x in range(T):
        line1=f.readline().strip()
        values=[int(i) for i in line1.split(" ")]
        N=values.pop()
        k=values.pop()
        R=values.pop()
        #R=values[0],k=values[1],N=values[2]
        y=0
        line2=f.readline().strip()
        queue=[int(i) for i in line2.split(" ")]
        queue.reverse()
        while R>0:
            groupi=queue.pop()
            occupied=0
            i=1
            while k-occupied>=groupi and i<=N:
                occupied+=groupi
                queue.insert(0,groupi)
                i+=1
                groupi=queue.pop()
            
            y+=occupied    
            queue.append(groupi)
            R-=1
              
        f1.write("Case #"+str(x+1)+": "+str(y)+"\n")
    f.close()
    f1.close()
        