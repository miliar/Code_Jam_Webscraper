#count=1
#
#max=14
#fillto = len(bin(2**max-1)[2:])
#
#for oc in range(1,max):
#    
#    for ic in range(1,-1,-1):
#        eq="2^%s%s"%(oc,"-1"if ic==1 else "")
#        last1=(count)/2 # this+1 is the location of the last light on
#        first0=last1+1 #this the location of the last light on
#        prev1=last1-1
#        seq=bin(2**oc-ic)[2:].zfill(fillto )[::-1]
#        
#        spmodel=seq[:last1]+"G"+seq[last1+1:]
#        if count%2==0:
#            pass
#            print "%s\t%s\t%s"%(count,eq,seq)
#        else:
#            print "%s\t%s\t%s\t%s"%(count,eq,spmodel,first0)
#        count+=1
        
#LOOKS GOOD BUT CHECK

def isOn(nthLight,kSnaps,model=False):

    seq=bin(kSnaps)[2:].zfill(nthLight)[::-1]
    s=sum([int(i) for i in seq][:nthLight])
    state=s==nthLight
    if model and kSnaps<10**2:
      light="Y" if (state) else "N"
      spmodel=seq[:nthLight-1]+light+seq[nthLight:]
      return (state,spmodel)
    else:
      return (state, None) 


if __name__=="__main__":
  import sys
  lines=open(sys.argv[1]).readlines()[1:]
  for i,l in enumerate(lines):
    t=[int(n) for n in l.split()]
    r,m=isOn(*t,model=False)
    light="ON" if (r) else "OFF"
    if m:
      print "Case #%s: %s\t%s\t%s %s"%(i+1,light,m,i,t)
    else:
      print "Case #%s: %s"%(i+1,light)

