# -*- coding: utf-8 -*-
fname = "A-large"
fin = open(fname+".in","r")
fout = open(fname+".out","w")
def gcj_read():
  linestr = fin.readline().strip()
  return [int(numb) for numb in linestr.split()]

numcases = gcj_read()[0]

def makeredmap(R,C,bluemap):
    redmap1 = set()     # Forward slashes
    redmap2 = set()     # Backward slashes
    for r in range(R):
        for c in range(C):
            if (r,c) in bluemap:
                toreplace = {(r,c), (r+1,c), (r,c+1), (r+1,c+1)}
                if toreplace.issubset(bluemap):
                    redmap1.update([(r,c), (r+1,c+1)])
                    redmap2.update([(r+1,c), (r,c+1)])
                    bluemap -= toreplace
                else:
                    return "Impossible"
    
    gettile = lambda x,y: "/" if (x,y) in redmap1 else "\\" if (x,y) in redmap2 else "."
    return "\n".join("".join(gettile(r,c) for c in range(C)) for r in range(R))
    

for caseno in range(numcases):
    R, C = gcj_read()
    bluemap = set()
    for r in range(R):
        row = fin.readline().strip()
        for c, piece in enumerate(row):
            if piece == "#":
                bluemap.add((r,c))
    
    outstr = makeredmap(R,C,bluemap)
    
    fout.write("Case #"+str(caseno+1)+":\n")
    fout.write(outstr + "\n")

fin.close()
fout.close()
