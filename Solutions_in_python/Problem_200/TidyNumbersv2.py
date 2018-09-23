
fout = open('TidyNumbers-largegcj.out', 'w')

def lp(s, n):
    return (n-len(s))*'0'+s

def doprint(s):
    print(s)
    fout.write(s+'\n')

def close():
    fout.close()

T = int(input())
for tc in range(1,T+1):
    ns = input()
    lns = [int(d) for d in ns]

    di = -1 # dropind

    '''for i in range(len(lns)-2, -1, -1):
        if lns[i] > lns[i+1]:
            di = int(i)
            break'''

    # once we hit the decrease from going forward, there can only be up to one before that final number.
    # eg. 24468883573101
    #         *  ^
    #     2446799999999


    # forward phase
    i = 1
    while i < len(lns) and lns[i-1] <= lns[i]: # could rewrite with i-1, i
        i += 1

    if i < len(lns):# or len(lns) >= 2 and lns[-2] > lns[-1]:
        while i-2 >= 0 and lns[i-1] == lns[i-2]:
            i -= 1

    if i < len(lns):
        # make answer
        lns[i-1] -= 1
        for digi in range(i, len(lns)):
            lns[digi] = 9

    ansS = "".join(str(e) for e in lns)
    ans = int(ansS)
    doprint("Case #"+str(tc)+": "+str(ans) )   

    

close()


'''
9
3100
31003100
1234
159
106
810
24468883573101
42
461
'''


'''
4
132
1000
7
111111111111111110
'''

'''
4
1324
780011
79900
2111000888999
'''
