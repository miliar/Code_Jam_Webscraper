import psyco
psyco.full()

def main():
    def gcf(a,b):
        if b==0:
            return a
        else:
            return gcf(b,a%b)
    
    cases = int(raw_input())
    for i in xrange(0, cases):
        list = map(int, raw_input().split(" "))
        list.pop(0)
        y=0
        g=0
        small=min(list)
        dlist=[x-small for x in list]
        g=reduce(gcf, dlist)
        f=list[0]
        if f%g != 0:
            y=(f/g + 1)*g - f     
        
        res=y
        print "Case #%i: %i" % (i+1, res)
    
           
main()