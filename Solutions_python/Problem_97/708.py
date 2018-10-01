
def mprint(a):
    if None:
        print (a)

def lprint(bool,a):
    if bool:
        print a

def shift(s):
    a = s[len(s)-1] + s[:len(s)-1]
    return a

def shifts(a_str):
    result = {}
    result[a_str] = a_str
    dummy = a_str
    for i in range(1,len(a_str)):
        dummy = shift(dummy)
        result[dummy] = dummy
    mprint(result)
    return result
        

def pairs(a,b):
    count = 0
    for n in range(a,b-1):
        a_str = str(n)
        all_shifts = shifts(a_str)
        for k,v in all_shifts.iteritems():
            if (int(k) > n) and (int(k) <= b):
                count+=1
                mprint("found " + str(n) + " and " + str(k))
    return count


#f = open("recycle.test","r")
f = open("C-small-attempt0.in","r")

s = f.readline()
ntrials = int(s)

i =0

fout = open("recycle.out","w")

for line in f:
    i+=1
    fields = line.split()
    a = int(fields.pop(0))
    b = int(fields.pop(0))
    result = pairs(a,b)
    print "Case #" + str(i) + ": "  + str(result)
    fout.write("Case #" + str(i) + ": "  + str(result) +"\n")

    
