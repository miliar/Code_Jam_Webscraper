import math

def solve(fstr):
    outStr = ""
    ipt = fstr.strip().split('\n')
    ipt = ipt[1:]
    tcs = []
    for it in ipt:
        tcs.append(it.strip().split())
    
    print str(tcs)

    tcInd = 1
    for tc in tcs:
        f = float(eval(tc[0]))
        R = float(eval(tc[1]))
        t = float(eval(tc[2]))
        r = float(eval(tc[3]))
        g = float(eval(tc[4]))

        nh = (R-r-t)/(2*r+g)
        
        if (nh - int(nh) > 0):
            nh += 1
        
        nh = int(nh)
        
        a = 0
        
        if (g >= 2*f):
            Re = R-t-f
            for j in range(nh):
                y = r + j*(2*r+g)
                for i in range(nh):
                    x = r + i*(2*r+g)
                    xa = x+f
                    ya = y+f
                    xc = x+g-f
                    yc = y+g-f
                    xb = xa
                    yb = yc
                    xd = xc
                    yd = ya                
                    
                    abi = bci = dci = adi = yb - ya
                    
                    if (xa*xa + ya*ya >= Re*Re):
                        continue
                    
                    if (xc*xc + yc*yc <= Re*Re):
                        a += (xc-xa)*(yc-ya)
                        continue
            
                    if (xb*xb + yb*yb <= Re*Re):
                        y1 = yb
                        if (xb*xb + yb*yb == Re*Re):
                            bci = 0
                            x1 = xb
                        else:
                            th = math.acos(yb/Re)
                            x1 = Re*math.sin(th) 
                            bci = x1 - xb          
                    else:
                        x1 = xa
                        th = math.acos(xa/Re)
                        y1 = Re*math.sin(th) 
                        abi = y1 - ya     
    
                    if (xd*xd + yd*yd <= Re*Re):
                        x2 = xd
                        if (xd*xd + yd*yd == Re*Re):
                            dci = 0
                            y2 = yd
                        else:
                            th = math.acos(xd/Re)
                            y2 = Re*math.sin(th) 
                            dci = y2 - yd 
                    else:
                        y2 = yd
                        th = math.acos(yd/Re)
                        x2 = Re*math.sin(th) 
                        adi = x2 - xa 
                    
                    c2 = (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1)
                    
                    th = math.acos(1 - c2/(2*Re*Re))
                    
                    ac = Re*Re*(th - math.sin(th))/2
                    
                    if (xb*xb + yb*yb <= Re*Re):
                        if (xd*xd + yd*yd <= Re*Re):
                            a += abi*adi - (abi - bci)*(adi - dci)/2 + ac
                        else:
                            a += (bci + adi)*abi/2 + ac
                    else:
                        if (xd*xd + yd*yd <= Re*Re):
                            a += (dci + abi)*adi/2 + ac
                        else:
                            a += abi*adi/2 + ac
            
            p = 1 - 4*a/(R*R*math.pi)
        else:
            p = 1.0
        
        outStr += "Case #" + str(tcInd) +": " + '%.6f'%p + "\n"
        tcInd += 1
        
    return outStr
    

ipt = None
opt = None
try:
    prog = "C"
    fName = "C-large.in"
    iptF = file("e:\GCJ\\" + prog + "\\" + fName)
    outStr = solve(iptF.read())
    print outStr
    optF = file("e:\GCJ\\" + prog + "\output.txt",'w+')
    optF.write(outStr)
    optF.close()
    if (fName == "input.txt"):    
        otstF = file("e:\GCJ\\" + prog + "\outtest.txt")
        otst = otstF.read()
        otstF.close()
        if (otst == outStr):
            print "+++++++++++++++ CORRETO +++++++++++++++++"
        else:
            print "______________ INCORRETO ________________"
finally:
    if (iptF != None):
        iptF.close()
