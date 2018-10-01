
def read_ints():
    return map(int, raw_input().split(" "))




def calc_wp(n, sch):
    wp = []
    for i in range(n):
        win_cnt = len(filter(lambda x: x == 1, sch[i]))
        tot_cnt = len(filter(lambda x: x != -1, sch[i]))
        wp += [float(win_cnt) / float(tot_cnt)]   
    #print wp
    return wp

def calc_owp(n, sch):
    owp = []
    for i in range(n):
        wp = []
        for j in range(n):
            if j == i:
                wp += [0.0]
                continue
            win_cnt = 0
            tot_cnt = 0
            for k in range(n):
                if k == i:
                    continue
                if (sch[j][k] != -1):
                    tot_cnt += 1
                if (sch[j][k] == 1):
                    win_cnt += 1
            wp += [float(win_cnt) / float(tot_cnt)]   
        ave = 0.0
        cnt = 0
        for j in range(n):
            if sch[i][j] != -1:
                cnt += 1
                ave += wp[j]
                #print "  -- %d, %f, %d" % (i, ave, cnt)
        owp += [ave / float(cnt)]
    return owp

def solve(n, sch):
    wp = calc_wp(n, sch)
    owp = calc_owp(n, sch) 
    #print owp
    oowp = []
    for i in range(n):
        ave = 0.0
        cnt = 0
        for j in range(n):
            if sch[i][j] != -1:
                cnt += 1
                ave += owp[j]
        oowp += [ave / float(cnt)]
        #print oowp
    ans = []
    for i in range(n):
        ans += [0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]]
    return ans



def main():
    T, = read_ints()
    for cas in xrange(T):
        N, = read_ints()
        sch = []
        for i in range(N):
            s = raw_input()
            tmp = []
            for x in s:
                if x == '.':
                    tmp += [-1]
                elif x == '1':
                    tmp += [1]
                else:
                    tmp += [0]
            sch += [tmp]
            #print tmp
        ans = solve(N, sch)
        print "Case #%d:" % (cas+1)
        for a in ans:
            print a

if __name__ == '__main__':
    main()
