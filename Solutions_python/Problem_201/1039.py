t=int(input())
for i in range(1, t+1):
    stalls, people = input().split(' ')
    stalls = int(stalls)
    people = int(people)
    found = False
    level = 1
    l_cnt = 1
    u_cnt = 0
    cnt = 1
    lw = lambda x: 1 if x else 2
    hgh = lambda x: 1 if x else 0
    if people == 1:
        found = True
        val = stalls
    while not found:
        new_stalls = (stalls - 1) / 2
        l_un = not (new_stalls == int(new_stalls))
        new_stalls = int(new_stalls)
        u_new_stalls = (stalls) / 2
        u_un = not (u_new_stalls == int(u_new_stalls))
        n_l_cnt = (l_cnt * lw(l_un)) + (u_cnt * hgh(u_un))
        u_cnt = (l_cnt * hgh(l_un)) + (u_cnt * lw(u_un))
        l_cnt = n_l_cnt
        new_cnt = pow(2, level)
        assert new_cnt == u_cnt + l_cnt
        if cnt + new_cnt >= people:
            if cnt + u_cnt >= people:
                val = new_stalls + 1
            else:
                val = new_stalls
            break
        level += 1
        cnt += new_cnt
        stalls = new_stalls

    val = (val - 1) / 2
    if val == int(val):
        val = int(val)
        print("Case #{}: {} {}".format(i, val, val))
    else:
        val = int(val)
        print("Case #{}: {} {}".format(i, val+1, val))
        
