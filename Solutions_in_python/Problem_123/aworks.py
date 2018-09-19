from math import *

def soln(armin, motes):
    motes.sort()
    ops=0
    i=0
    length=len(motes)
    first=True
    
    mincase=length
        
    if armin==1:
        return length
    
    while i < length:
        this = motes[i]
        if armin > this:

            armin += this
            i += 1
        else:
            remain = length-i
            if first:
                    #We could just remove them all
                mincase = remain
                first=False
            
            armin = armin*2 -1
            ops += 1

            
            return min(mincase,1 + soln(armin,motes[i:]))

    return ops
        

        
    


#-----------------Main------------------------
                             
def a(filename = "a.in"):
    txt = open(filename, "rU")
    solution = open("solution.txt","w")
    #Read topline info
    topline=txt.readline()
    noCases = int(topline.strip())

    

    
    #For each game:
    for case in range(1,noCases+1):
        print "Case #{0}:".format(case)
        armline = txt.readline().strip() #Chews the line
        armin = int(armline.split(" ")[0])

        moteline = txt.readline().strip() #Chews the line
        motes = [int(x) for x in moteline.split(" ")]
        
        if case==noCases:
            solution.write("Case #{0}: {1}".format(case, soln(armin, motes)) )
        else:
            solution.write("Case #{0}: {1}\n".format(case, soln(armin, motes)) )
        
    txt.close()
    solution.close()
    print "Done"
