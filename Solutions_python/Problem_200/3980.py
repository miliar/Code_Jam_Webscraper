T = input()

for i in range(T):
    N = input()
    N_lst = [int(n) for n in str(N)]

    for j in range(len(N_lst) - 2, -1, -1):
        if N_lst[j] > N_lst[j + 1]:
            N_lst[j] -= 1
            
            for k in range(j + 1, len(N_lst)):
                N_lst[k] = 9

    result = int(''.join([str(n) for n in N_lst]))

    print "Case #%d: %s" % (i + 1, result)