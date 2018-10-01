a = {
        '1': {'1': '1', 'i': 'i', 'j': 'j', 'k': 'k'},
        'i': {'1': 'i', 'i': '-1', 'j': 'k', 'k': '-j'},
        'j': {'1': 'j', 'i': '-k', 'j': '-1', 'k': 'i'},
        'k': {'1': 'k', 'i': 'j', 'j': '-i', 'k': '-1'},
    }

T = int(raw_input());

NEG, POS = 0, 1

for xyz in range(T):
    lx = raw_input().split();
    L, X = int(lx[0]), int(lx[1])
    s = raw_input()
    s = s*X

    I_IDX = []
    SIGN = POS
    CURR = '1'
    FOUND = False
    for i in range(len(s)-2):
        CURR = a[CURR][s[i]]
        if CURR[0] == '-':
            if SIGN == POS: SIGN = NEG
            else: SIGN = POS
            CURR = CURR[1]

        # I found
        if CURR == 'i' and SIGN == POS:
            I_IDX.append(i)

    K_IDX = set()
    SIGN = POS
    CURR = '1'
    if I_IDX:
        for i in range(len(s)-1, 1, -1):
            CURR = a[s[i]][CURR]
            if CURR[0] == '-':
                if SIGN == POS: SIGN = NEG
                else: SIGN = POS
                CURR = CURR[1]

            # K found
            if CURR == 'k' and SIGN == POS:
                K_IDX.add(i)

    for i in I_IDX:
        SIGN = POS
        CURR = '1'
        for j in range(i+1, len(s)-1):
            CURR = a[CURR][s[j]]
            if CURR[0] == '-':
                if SIGN == POS: SIGN = NEG
                else: SIGN = POS
                CURR = CURR[1]

            # J found
            if CURR == 'j' and SIGN == POS:
                if (j+1) in K_IDX:
                    FOUND = True
            if FOUND: break
        if FOUND: break
    
    if FOUND:
        print 'Case #%d: YES' % (xyz+1)
    else:
        print 'Case #%d: NO' % (xyz+1)
