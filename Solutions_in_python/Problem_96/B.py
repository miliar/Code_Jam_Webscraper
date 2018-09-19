inputTxt = open('binput.txt', 'r').readlines()

for i, line in enumerate(inputTxt[1:]):
    answer = 0
    N, S, p, *Ti = map(int, line.split())
    #print('(N, S, p, Ti)', N, S, p, Ti)

    for totals in Ti:
        s1 = round(totals / 3)
        s2 = round(totals / 3)
        s3 = totals - s1 - s2

        if max((s1, s2, s3)) >= p:
            answer += 1
        elif S>0 and any(map(lambda x: x==p-1, (s1, s2, s3))) and max((s1, s2, s3)) > 0:
            answer += 1
            S -= 1
            #print('     sr')
        #print('     (s1, s2, s3)', s1, s2, s3)

    print("Case #{}: {}".format(i+1, answer))
