fd = open("snapper.in","r")
out = open("snapper.out","w")
lines = fd.readlines()
ans = {False:"OFF",True:"ON"}
for i,line in enumerate(lines[1:]):
    Nstr,kstr = line.split()
    N,k = int(Nstr),int(kstr)
    out.write("Case #%i: %s\n"%(i+1,ans[(k+1) % 2**N == 0]))
    
