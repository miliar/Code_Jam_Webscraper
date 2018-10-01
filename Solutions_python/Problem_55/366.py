from collections import deque

ifile = open("C-large.in")
inp = ifile.read().split("\n")
ifile.close()

T = int(inp[0])

for i in range(1,len(inp)-1,2):
    #input set
    R = int(inp[i].split(" ")[0])
    k = int(inp[i].split(" ")[1])
    N = int(inp[i].split(" ")[2])
    Gtemp = inp[i+1].split(" ")
    G = deque([])
    for g in Gtemp:
        G.append(int(g))
    
    #roller
    dic = dict()
    money = 0
    m = 1
    is_caled = False
    while m <= R:
        if not is_caled:
            if str(G) in dic:
                money_r = money - dic[str(G)][0]
                m_r = m - dic[str(G)][1]
                times = (R-m)/m_r
                #jump
                money += times*money_r
                m = R - ((R-m)%m_r)
                is_caled = True
            else:
                dic[str(G)] = (money,m)
        
        k_temp = 0
        people_cnt = 1
        while (k_temp+G[0]<=k) and (people_cnt<=len(G)):
            k_temp += G[0]
            money += G[0]
            G.append(G.popleft())
            people_cnt+=1

        m += 1
    
    ofile = open("theme_out.txt","a")
    ofile.write("Case #"+str(i/2+1)+": "+str(money)+"\n")
    ofile.close()