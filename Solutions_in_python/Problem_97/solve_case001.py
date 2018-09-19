# This script was written by Norio TAKEMOTO 2012-4-13



def solve_case(imin, imax):

    numpair=0
    for ii in range(imin, imax+1):
        dd = [elm for elm in '%i'%(ii)]
        numdigit=len(dd)
        cand=[]
        for s in range(1,numdigit):
            ai=''
            for j in range(numdigit):
                ai = ai+dd[(j+s)%numdigit]

            ri = int(ai)
            if ii < ri and ri <= imax:
                flg_dup=False
                for elm in cand:
                    if elm == ri:
                        flg_dup = True
                        break
                if not flg_dup:
                    cand.append(ri)
        numpair += len(cand)
    return numpair
