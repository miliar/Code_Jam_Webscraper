def mini_l_p(l):
    if l == []:
        return None
    else:
        mini = l[0]
        for i,el_i in l:
            if mini[1] > el_i:
                mini = (i,el_i)
        return mini


def maxi_l_p(l):
    if l == []:
        return None
    else:
        maxi = l[0]
        for i,el_i in l:
            if maxi[1] < el_i:
                maxi = (i,el_i)
        return maxi



t = int(input())
for case in range(1,t+1):
    n = int(input())
    naomi_l = map(float,raw_input().split(' '))
    ken_l = map(float,raw_input().split(' '))

    result_war = 0
    naomi_war = [(i,naomi_l[i]) for i in range(len(naomi_l))]
    ken_war = [(i,ken_l[i]) for i in range(len(ken_l))]
    for i, el_i in naomi_war:
        more_el = [(i,el) for i,el in ken_war if el > el_i]
        chosen = mini_l_p(more_el)
        if chosen == None:
            chosen = mini_l_p(ken_war)
            result_war += 1
        ken_war = [(i,el_i) for i,el_i in ken_war if i!=chosen[0]]

    result_deic = 0
    naomi_deic = [(i,naomi_l[i]) for i in range(len(naomi_l))]
    ken_deic = [(i,ken_l[i]) for i in range(len(ken_l))]
    while ken_deic != []:
        if maxi_l_p(naomi_deic)[1] > maxi_l_p(ken_deic)[1]:
            chosen_ken = mini_l_p(ken_deic)
            more_el = [(i,el) for i,el in naomi_deic if el > chosen_ken[1]]
            chosen = mini_l_p(more_el)
            result_deic += 1
        else:
            chosen = mini_l_p(naomi_deic)
            chosen_ken = maxi_l_p(ken_deic)
        naomi_deic = [(i,el_i) for i,el_i in naomi_deic if i!=chosen[0]]
        ken_deic = [(i,el_i) for i,el_i in ken_deic if i!=chosen_ken[0]]

    print("Case #"+str(case)+": "+str(result_deic)+" "+str(result_war))



