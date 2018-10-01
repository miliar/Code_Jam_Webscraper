infile = r'D:\pratik\code jam\Real Code jam\\level2\ward.in'
ofile = r'D:\pratik\code jam\Real Code jam\\level2\wardo.in'

ifp = open(infile, 'r')
t = int(ifp.readline().strip())
##print t

answer = ''
for i in range(t):
    print i,
    n = int(ifp.readline().strip())
    ##print n
    naomi = map(float, ifp.readline().strip().split(' '))
    ken = map(float, ifp.readline().strip().split(' '))
    ##print naomi, ken
    naomi.sort()
    ken.sort(reverse=True)
    naomi2 = list(naomi)
    ken2 = list(ken)
    war, dec_war = 0, 0


    #optimal WAR
    #naomi plays least card first
    #print naomi
    #print ken
    n_dash = n
    for u in range(n):
        chosen_naomi = naomi[u]
        loc_ken_bigger = sum(u>chosen_naomi for u in ken)
        if loc_ken_bigger:
            loc = loc_ken_bigger-1
        else:
            war+=1
            #ken choses lowest card
            loc = n_dash-1
        chosen_ken = ken.pop(loc)
        n_dash-=1
        #print loc_ken_bigger, chosen_naomi, chosen_ken, ken
    print ' war ',

    #optimal DECITFUL WAR
    #ken play to lose!
    naomi2.sort(reverse=True)
    #print ken2
    #print naomi2
    n_dash = n
    #print n_dash
    for u in range(n):
        chosen_ken = ken2[u]
        loc_naomi_bigger = sum(u>chosen_ken for u in naomi2)
        if loc_naomi_bigger:
            #naomi choses higher card
            dec_war+=1
            loc = loc_naomi_bigger-1
        else:
            loc = n_dash-1
        chosen_naomi = naomi2.pop(loc)
        n_dash-=1
        #print loc_naomi_bigger, chosen_ken, chosen_naomi, naomi2, loc


    #print 'Case #%d: %d %d\n' %(i+1, dec_war, war)
    answer+='Case #%d: %d %d\n' %(i+1, dec_war, war)
    if dec_war<war:
        #print 'Fail'
        break
    print 'dec-war'
	
ofp = open(ofile, 'w')
ofp.write(answer)
ofp.close()
ifp.close()


