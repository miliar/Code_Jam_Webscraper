import sys


#def method(t):
#     n = t[0]
#     d = t[1]
#     g = t[2]
# #    tmp = 100 - d
# #    tmp = (d*n)/100
#     if (d==g):
#         return "Possible"
#     else:
#         if ((g != 0) and (((d*n) / g) > n) or ((g!=0 and n ==0))):
#             return "Possible"
#         else:
#             return "Broken"
    
    

if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        fin = open(sys.argv[1], "r")
        
    cases = int(fin.readline().strip())

    for i in range(cases):
        print "Case #%s:" %str(i+1)
        
        n = int(fin.readline().strip())
        teams = []
        wp = {}
        owp = {}
        oowp = {}
        rpi = {}
        play_list = {}
        pcount_list = {}
        win_list = {}
        comps = '10'
        for j in range(n):
            test = fin.readline().strip()
            teams.append(test)
            pcount = 0
            win = 0
            play_list[j] = []
            for k in range(n):
                if test[k] in comps:
                    pcount += 1
                    play_list[j].append(k)
                if test[k] == '1':
                    win += 1
            pcount_list[j] = pcount
            win_list[j] = win
            wp[j] = float(win)/float(pcount)
#        print "Teams : %s" %str(teams)
        for j in range(n):
            tmp_list = []
#            print "play_list: %s" %str(play_list[j])
            for k in play_list[j]:
                if teams[j][k] == '1':
                    twin = win_list[k] 
                    tpcount = pcount_list[k] -1
                else:
                    twin = win_list[k] -1
                    tpcount = pcount_list[k] -1
                tmp = float(twin)/float(tpcount)
                tmp_list.append(tmp)
#            print "TMP_LIST :%s" %str(tmp_list)
            owp[j] = sum(tmp_list)/float(len(play_list[j]))
        for j in range(n):
            tmp = 0.0
            for k in play_list[j]:
                tmp += owp[k]
            oowp[j] = tmp/float(len(play_list[j]))
            rpi[j] = (0.25 * wp[j]) + (0.50 * owp[j]) + (0.25 * oowp[j])
#            print "WP: %s  owp: %s  oowp: %s" %(str(wp[j]), owp[j], oowp[j])
            print rpi[j]
#            t = method(test)
#            print "Case #%s: %s" %(str(i+1), t) 
    fin.close()
