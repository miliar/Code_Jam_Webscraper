execfile('utils.py')

H = dict([(i,{}) for i in range(2,11)])

def process(fn):
    cases = [x.strip() for x in read1(fn)[1:]]
    res = [processCase(x) for x in cases]
##    print res
    write2(fn+".out",res)

def processCase(num):
    if num == 0:
        return "0"
    snum = str(num)
    index = len(snum)-1
    while index>=1 and snum[index]<=snum[index-1]:
        index -= 1

##    print "index", index
    if index == 0:
        ssnum = "".join(sorted(snum))
        firstdigitindex = 0
        while ssnum[firstdigitindex] == '0':
            firstdigitindex += 1
        firstdigit = ssnum[firstdigitindex]
##        print "firstdigit",firstdigit
        return firstdigit+'0'+ssnum[:firstdigitindex]+ssnum[firstdigitindex+1:]
    else:
        # find smallest which is bigger
        big = snum[index-1]
        smallindex = len(snum)-1
        while snum[smallindex] <= big:
            smallindex -= 1
            
        return snum[:index-1] + snum[smallindex] + "".join(sorted(snum[index-1]+snum[index:smallindex]+snum[smallindex+1:]))
