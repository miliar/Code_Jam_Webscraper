class Q(object):
    #x = (1, "1") # sign, value
    def __init__(self, *args):
        if len(args)==1:
            s = args[0]
            sign = 1
            value = "1"
            if "i" in s:
                value = "i"
            if "j" in s:
                value = "j"
            if "k" in s:
                value = "k"
            if "-" in s:  
                sign = -1
            self.x=(sign, value)
        else:
            self.x=args

    def __mul__(self, other):
        sign = self.x[0]*other.x[0]
        q = {   "11": (1 , "1"),
                "1i": (1 , "i"),
                "1j": (1 , "j"),
                "1k": (1 , "k"),
                "i1": (1 , "i"),
                "ii": (-1, "1"),
                "ij": (1 , "k"),
                "ik": (-1, "j"),
                "j1": (1 , "j"),
                "ji": (-1, "k"),
                "jj": (-1, "1"),
                "jk": (1 , "i"),
                "k1": (1 , "k"),
                "ki": (1 , "j"),
                "kj": (-1, "i"),
                "kk": (-1, "1"),
                }[self.x[1]+other.x[1]]
        return Q(q[0]*sign, q[1])

    def __str__(self):
        sign="" if self.x[0]==1 else "-"
        return sign+self.x[1]
    def __eq__(self, other):
        return self.x[0]==other.x[0] and self.x[1]==other.x[1]

def f():
    from itertools import izip
    fin=open("data.in","r")
    fout=open("data.out","w")
    data = fin.readlines()

    for (i, gugu) in enumerate(izip(data[1::2], data[2::2])):
        aa, s = gugu
        l, x = map(int, aa.split())
        ss=s[:-1]*x
        fout.write("Case #%d: %s\n" % (i+1, "YES" if g(ss) else "NO"))

def g(ss):
    acc = Q("1")   
    i=0
#   import ipdb; ipdb.set_trace()
    while i<len(ss):
        acc=acc*Q(ss[i])
        i+=1
        if acc==Q("i"):
            break
    else:
        return False

    acc = Q("1")
    while i<len(ss):
        acc=acc*Q(ss[i])
        i+=1
        if acc==Q("j"):
            break
    else:
        return False

    acc = Q("1")
    while i<len(ss):
        acc=acc*Q(ss[i])
        i+=1
        if acc==Q("k"):
            break
    else:
        return False

    acc = Q("1")
    while i<len(ss):
        acc=acc*Q(ss[i])
        i+=1
    if acc==Q("1"):
        return True
    return False

if __name__ == "__main__":
    f()
