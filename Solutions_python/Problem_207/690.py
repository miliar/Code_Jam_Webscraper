N = int(input())

for i in range(N):
    inp = list(map(int,input().split()))
    H_N = inp[0]
    hs = inp[1:len(inp)]

    ret = ''
    m_i = -1
    first_m_i = hs.index(max(hs))
    while(max(hs)>0):
        #print(hs)
        hs_cp = hs[:]
        if m_i>=0:
            hs_cp[m_i] = 0
            hs_cp[m_i-1] = 0
            hs_cp[(m_i+1)%len(hs_cp)] = 0
        if max(hs_cp)==0:
            #print(ret)
            ret = 'IMPOSSIBLE'
            break

        if m_i>=0:
            m_i = (m_i+3)%len(hs_cp)
            if hs_cp[m_i]==0:
                if m_i+1==first_m_i and hs_cp[m_i+1]>0:
                    m_i = m_i+1
                elif m_i-1==first_m_i and hs_cp[m_i-1]>0:
                    m_i = m_i-1
                else:
                    m_i = hs_cp.index(max(hs_cp))
        else:
            m_i = hs_cp.index(max(hs_cp))
        if m_i ==0:
            ret += 'R'
        elif m_i==1:
            ret += 'O'
        elif m_i==2:
            ret += 'Y'
        elif m_i==3:
            ret += 'G'
        elif m_i==4:
            ret += 'B'
        elif m_i==5:
            ret += 'V'
        hs[m_i] -= 1
    if ret[0]==ret[len(ret)-1]:
        #print(ret)
        ret = 'IMPOSSIBLE'
    print('Case #'+str(i+1)+': '+ret)
