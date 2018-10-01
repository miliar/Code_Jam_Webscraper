import glob
import os
for fname in glob.glob("*.in"):
    fin=open(fname, "r")
    fout=open(fname + ".out", "w+")
    output=[]
    
    for i in range(1,1+int(fin.readline())):
        N,K=map(int,fin.readline().split())
        output.append("Case #%i: %s"%(i,"ON" if (K&((1<<N)-1))==((1<<N)-1) else "OFF"))

    fout.write("\n".join(output))
    fout.close()