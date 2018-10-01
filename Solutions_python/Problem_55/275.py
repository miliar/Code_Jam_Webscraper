from fractions import gcd
from itertools import izip

def money_current_round(nseat,groups):
    cval = 0
    for x,g in enumerate(groups):
        nval = cval + g
        if nval > nseat: break
        cval = nval
    return cval,x

def round_to_loopback(nseat,groups,rlimit):
    rval = 0
    rmoney = 0
    cgroups = groups[:]
    while rval < rlimit:
        cmoney,cpos = money_current_round(nseat,cgroups)
        cgroups     = cgroups[cpos:] + cgroups[:cpos]
        rval       += 1
        rmoney     += cmoney
        if cgroups == groups:
            break
    return rval,rmoney

def money(nround,nseat,groups):
    rloop,rmoney = round_to_loopback(nseat,groups,nround)
    if rloop == nround: return rmoney
    left_round = nround % rloop
    last_loop,last_money = round_to_loopback(nseat,groups,left_round)
    return rmoney * (nround/rloop) + last_money

def print_res(caseno,res):
    print "Case #%d: %s" %(caseno,res) 

def main():
    for case in xrange(1,int(raw_input())+1):
        r,k,Tn = [long(w) for w in raw_input().split(' ')]
        N = [long(w) for w in raw_input().split(' ')]
        print_res(case,money(r,k,N))

if __name__=="__main__":
    main()
