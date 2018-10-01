from __future__ import division

def readin():
    filez = open('input.in', 'r')
    return filez.readlines()

def writeout():
    global wfile
    wfile = open('out.out', 'w')

def main ():
    global inputs
    writeout()
    inputs = readin()
    cases = int(inputs[0])
    cases=cases
    for i in range(cases):
        temp=(inputs[i+1].split())
        c=float(temp[0])
        f=float(temp[1])
        x=float(temp[2])
        mintime=x/2
        currtime=0.0
        rate=2.0
        while currtime<mintime:
            currtime=currtime+c/rate
            rate=rate+f
            temptime=x/rate+currtime
            if temptime<mintime:
                mintime=temptime 
        stri = "Case #"+str(i+1)+": "+str(mintime)+"\n"        
        wfile.write(stri)            
    wfile.close()

if __name__ == "__main__":
    main()