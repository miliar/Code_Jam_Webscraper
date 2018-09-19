import sys
sys.setrecursionlimit(3000)

def log(*args, sep=" ", end="\n", file= sys.stderr, flush= False):
    file.write(sep.join(str(a) for a in args) + end)
    if flush:
        file.flush()

class Quaternion:
    def __init__(self, abs, sgn= 1):
        assert abs in ("1", "i", "j", "k")
        self.abs= abs
        self.sgn= sgn
    
    def __mul__(self, other):
        sgn= self.sgn * other.sgn
        abs= ""
        if self.abs == "1": return Quaternion(other.abs, sgn)
        elif other.abs == "1": return Quaternion(self.abs, sgn)
        elif self.abs == other.abs: return Quaternion("1", -sgn)
        elif self.abs == "i" and other.abs == "j": return Quaternion("k", sgn)
        elif self.abs == "j" and other.abs == "k": return Quaternion("i", sgn)
        elif self.abs == "k" and other.abs == "i": return Quaternion("j", sgn)
        elif self.abs == "j" and other.abs == "i": return Quaternion("k", -sgn)
        elif self.abs == "k" and other.abs == "j": return Quaternion("i", -sgn)
        elif self.abs == "i" and other.abs == "k": return Quaternion("j", -sgn)
        else:
            assert False
    
    def  __eq__(self, other):
        return self.abs == other.abs and self.sgn == other.sgn

one= Quaternion("1")
mOne= Quaternion("1", -1)
qI= Quaternion("i")
qJ= Quaternion("j")
qK= Quaternion("k")

def prod(qls):
    p= one
    for q in qls:
        p= p * q
    return p

def getPossible(s):
    if prod(s) != mOne: # i*j*k == -1
        return False #product cannot change
    prefix= one
    i= 0
    #get shortest prefix == "i" and shortest postfix == "k"
    try:
        while prefix != qI:
            prefix= prefix * s[i]
            i+= 1
        #prefix == s[:i]
        postfix= one
        j= len(s)
        while postfix != qK:
            j-= 1
            postfix= s[j] * postfix
        #postfix == s[j:]
    except IndexError:
        #not even prefix == "i" and postfix == "k"
        return False
    if i >= j:
        return False #pointers crossed, no room for infix "j"
    #if not infix == "j" then s == "ijk" not possible
    return prod(s[i:j]) == qJ


if __name__ == "__main__":
    nCases= int(input())
    for iCase in range(1, nCases + 1):
        l, x= map(int, input().split())
        s= list(Quaternion(c) for c in (input() * x))
        
        possible= getPossible(s)

        print("Case #{:d}: {:s}".format(iCase, "YES" if possible else "NO"))