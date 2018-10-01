# GCJ
# 2011
# Qualification Round
# Magicka

# This is a Python script.
# It works with Python 2.6 on Windows XP.
# It reads from stdin and writes to stdout.

oa = ord('A')
cti = lambda x: ord(x) - oa
itc = lambda x: chr(x + oa)
ntc = int(raw_input())

for tcn in range(1, ntc + 1):
    cm = [[-1] * 26 for ri in range(26)]
    oml = [0] * 26
    tcd = raw_input().split()
    nct = int(tcd[0])

    for cts in tcd[1:nct + 1]:
        ctl = map(cti, cts)
        cm[ctl[0]][ctl[1]] = cm[ctl[1]][ctl[0]] = ctl[2]

    nop = int(tcd[nct + 1])

    for ops in tcd[nct + 2:nop + nct + 2]:
        opl = map(cti, ops)
        oml[opl[0]] |= 1 << opl[1]
        oml[opl[1]] |= 1 << opl[0]

    eis = tcd[nop + nct + 3]
    eil = map(cti, eis)
    eol = []
    ocl = [0] * 26
    ocm = 0

    for pe in eil:
        if len(eol) > 0:
            eot = eol[-1]
            ce = cm[eot][pe]

            if ce >= 0:
                ocl[eot] -= 1

                if ocl[eot] == 0:
                    ocm -= 1 << eot
    
                eol[-1] = ce
                ocl[ce] += 1
                ocm |= 1 << ce
                continue

        if ocm & oml[pe]:
            eol = []
            ocm = 0
            ocl = [0] * 26
            continue

        eol.append(pe)            
        ocl[pe] += 1
        ocm |= 1 << pe

    print 'Case #{0}: [{1}]'.format(tcn, ', '.join(map(itc, eol)))
