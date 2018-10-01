ina = raw_input()
for l in range(0,int(ina)):
        inb = raw_input()
        [S,w] = inb.split()
        S = str(S)
        w = int(w)
        # print S,w
        c = 0
        i = 0
        j = -1
        while i < len(S):
                if S[i] == '-':
                        if j == -1:
                                j = i
                if j != -1:
                        # if (i - j) == w-1:
                        #         print 'a',i
                        #         c += 1
                        #         for k in range(j,i+1):
                        #                 # print k,S[k]
                        #                 # S[k] = '+'
                        #                 if S[k] == '-':
                        #                         S = S[:k] + '+' + S[k+1:]
                        #                 else:
                        #                         S = S[:k] + '-' + S[k+1:]
                        #         j = -1
                        if S[i] == '-' and (i <= len(S)-w):
                                # print 'b',i
                                c += 1
                                for k in range(i, i+w):
                                        if S[k] == '-':
                                                S = S[:k] + '+' + S[k+1:]
                                                # S[k] == '+'
                                        else:
                                                S = S[:k] + '-' + S[k+1:]
                                                # S[k] == '-'
                        # elif S[i] == '-' and (i <= len(S) -w):
                i = i + 1
        for z in range(0,len(S)):
                if S[z] == '-':
                        c = 'IMPOSSIBLE'
        case = l + 1
        # print S
        name = 'Case #' + str(case) + ':'
        print name,str(c)
