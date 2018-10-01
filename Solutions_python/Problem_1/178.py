import sys

def go(name):
    f=file(name)

    line=f.readline().strip()
    total=int(line)
    for i in range(total):
        line=f.readline().strip()
        site_count=int(line)
        sites={}
        for j in range(site_count):
            line=f.readline().strip()
            sites[line]=None
        line=f.readline().strip()
        query_count=int(line)

        lsites=site_count
        switches=0

        for j in range(query_count):
            line=f.readline().strip()
            if lsites>0:
                if sites[line]==None:
                    sites[line]=1
                    lsites-=1
            
            if lsites==0:
                switches+=1
                lsites=site_count-1
                for k in sites: sites[k]=None
                sites[line]=1
        
        print "Case #%d: %d" %(i+1, switches)
    d=f.read().split("\n")
    f.close()

            
try:
    fn=sys.argv[1]
except:
    print "Usage:\n", "python", sys.argv[0]+" input_file_name"
    sys.exit(1)

go(fn)
