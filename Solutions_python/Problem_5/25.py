import sys,os,glob

class MyError(RuntimeError):
    pass

def isHappy(possible,v):
    if sum(v) == 2*len(v): return True # test for all dontcares
    for i,val in enumerate(v):
        #~ print i,val,possible,possible & (2**i)

        if val == 2:
            continue
        else:
            if bool(possible & (2**i)) == val:
                return True

    return False

def printInt(b):
    if b:
        return '1'
    else:
        return '0'

#~ for i in [16]:
    #~ print i," ".join([printInt(i & (2**x)) for x in range(5)])
    #~ print isHappy(i,[2,2,2,2,1])
    #~ print isHappy(i,[2,2,2,0,0])
    #~ print isHappy(i,[2,2,2,2,2])
    #~ print

def bitify(v,N):
    ret = [2 for x in range(N)]
    for flavor,malted in v:
        if ret[flavor-1] != 2:
            ret[flavor-1] = 2
        else:
            ret[flavor-1] = malted
    #~ print v,ret
    return ret

def flavors_to_make(N,V):
    #~ print N,V
    for i in range(2**N):
        good = True
        for v in V:
            if not isHappy(i, bitify(v,N) ):
                good = False
                break
        if good:
            return i
    raise MyError()


    #~ possible_solutions = {}


    #~ for v in V[0]: # set up possibles from first guy
        #~ possible_solution = [0 for x in range(N)]
        #~ possible_solution[v[0]-1] = v[1]
        #~ possible_solutions[tuple(possible_solution)] = 1
    #~ print possible_solutions.keys()



    #~ sys.exit(0)
    #~ flavor_box = [0 for x in range(N)]
    #~ for v in V:
        #~ print v

    #~ return flavor_box

if __name__=='__main__':
    xxx = open(sys.argv[1]).readlines()

    #~ print xxx
    C = int(xxx.pop(0))
    #~ print T

    for i in range(C):
        #~ print "case",i
        N = int(xxx.pop(0))
        M = int(xxx.pop(0))
        #~ print N,M
        V = []
        for j in range(M):
            line = xxx.pop(0).split()
            T = int(line[0])
            Vcust = []
            V.append(Vcust)
            for k in range(T):
                X = int(line[k*2+1])
                Y = int(line[k*2+2])
                Vcust.append((X,Y))
        print "Case #%d:" % (i+1),
        try:
            val = flavors_to_make(N,V)
            print " ".join([printInt(val & (2**x)) for x in range(N)])
        except MyError:
            print "IMPOSSIBLE"

                #~ print k,X,Y
                #~ ,Y = [int(zzz) for zzz in xxx.pop(0).split()]
            #~ print "engine",j
        #~ V.append((xxx.pop(0).split(), xxx.pop(0).split()))
        #~ ret = figure([int(x) for x in xxx.pop(0).split()],
                      #~ [int(x) for x in xxx.pop(0).split()])

        #~ print V

