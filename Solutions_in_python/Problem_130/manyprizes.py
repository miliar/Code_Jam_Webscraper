from gcjbase import *
import decimal

def read_input(filename):
    data = []
    with open(filename, "r") as f:
        cases = read_ints(f)[0]
        # =============================================
        for _ in xrange(cases):
            N, P = read_ints(f)
            data.append({"N": N,
                         "P": P})
        # =============================================
    return data

def make_output(fname, output):
    CASE_PRFX = "Case #%s: "
    fname = fname + time.strftime("%H%M%S") + ".out"
    with open(fname, "w") as f:
        # =============================================
        restext = []
        print "Output content ==============="
        for i, (guar, cld) in enumerate(output):
            line = CASE_PRFX % (i+1,) + str(guar) + " " + str(cld) + "\n"
            print line[:-1]
            restext.append(line)
        print "=" * 30
        f.writelines(restext)
        # =============================================

# ----------------------------------------------------------------------

@timeit
@memoizeit
def single_team(i, N):
    
    # 0 = Win 1 = Lose
    FULL = (0x1 << N) - 1 
    BCS = 0
    WCS = FULL
    mask = 0x1 << N
    Abv = i
    Blw = 2 ** N - Abv - 1
    for n in xrange(1, N+1):
        S = 2 ** (N-n+1) - 1 
        if n != 1:
            #bcs
            if BCS & mask:
                # last round lost
                Abv = Abv / 2
            else:
                Abv = Abv % 2 + Abv / 2
            #wcs
            if WCS & mask:
                # last round lost
                Blw = Blw % 2 + Blw / 2
            else:
                Blw = Blw / 2
            
        mask = mask >> 1
        
        #bcs
        if S <= Abv:
            #lose
            BCS = BCS | mask
        
        #wcs
        if S <= Blw:
            #win
            WCS = WCS & (~(FULL & mask))
        
    return BCS, WCS


def solvesmall(case):
    max_guar = 0
    max_cld = 0
    for i in xrange(2 ** case['N']):
        BCS, WCS = single_team(i, case['N'])
        if WCS < case['P']:
            max_guar = i
        if BCS < case['P']:
            max_cld = i
    return max_guar, max_cld


def solvelarge(case):
    N = case['N']
    P = case['P']
    # look for guaranteed - the last to have guaranteed
    max_guar = 0
    
    chunk = [0, 2**N-1]
    while (chunk[1] - chunk[0] > 1):
        i = chunk[0] + (chunk[1] - chunk[0]) / 2
        _, WCS = single_team(i, N)
        if WCS < P:
            max_guar = i
            chunk[0] = i
        else:
            chunk[1] = i
        
    _, WCS1 = single_team(chunk[0], N)
    _, WCS2 = single_team(chunk[1], N)
    if WCS2 < P:
        max_guar = chunk[1]
    else:
        max_guar = chunk[0]
        
        
    # look for could - the last to have could
    max_cld = 0
    
    chunk = [0, 2**N-1]
    while (chunk[1] - chunk[0] > 1):
        i = chunk[0] + (chunk[1] - chunk[0]) / 2 
        BCS, _ = single_team(i, N)
        if BCS < P:
            max_cld = i
            chunk[0] = i
        else:
            chunk[1] = i

    BCS1, WCS1 = single_team(chunk[0], N)
    BCS2, WCS2 = single_team(chunk[1], N)
    if BCS2 < P:
        max_cld = chunk[1]
    else:
        max_cld = chunk[0]
        
        
        
    return max_guar, max_cld


@timeit
def solveit(case):
    return solvelarge(case) 

@timeit
def main(fname):
    data = read_input(fname)
    output = []
    for i, case in enumerate(data):
        statreset() # reset cache stats
        # =============================================
        res = solveit(case)
        output.append(res)
        # =============================================
    make_output(fname, output)


if __name__ == '__main__':
    #main("sample.in")
#    main("test.in")
    main("B-large.in")
#    main("B-small-attempt0.in")
#    main("A-large.in")