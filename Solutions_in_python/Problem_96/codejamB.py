import math;

dp = [];
t = None;
i=1;

total = 0;

N=None;S=None;p=None;

fin = open('cjb.in','r');
fout = open('cjb.out','w');

t = int(fin.readline());
while i<=t:
    
    line = fin.readline();
    data = [int(s) for s in line.split()];
    #print(i);
    N = data[0];
    S = data[1];
    p = data[2];
    dp = [];
    el = [0,0,S];   
    dp.append(el);
    #print(len(dp));
    #print(p);
    ln = len(data)-3;
    for x in range(0,ln):
        nr = data[x+3];
        ddv = nr/3;
        rmv = nr%3;
        if rmv == 0:
            ddv = int(ddv);
            wos = [ddv] * 3;
            ws = [ddv-1,ddv,ddv+1];
            if nr == 0:
                wos = [0] * 3;
                ws = [0] * 3;
        if rmv == 1:          
            ddv = math.floor(ddv);
            wos = [ddv,ddv,ddv+1];
            ws = [ddv-1,ddv+1,ddv+1];
            if nr == 1:
                wos = [0,0,1];
                ws = [0,0,1];
        if rmv == 2:
            ddv = math.ceil(ddv);
            wos = [ddv,ddv,ddv-1];
            ws = [ddv+1,ddv-1,ddv-1];

        #print(wos);
        goS = True;
        for j in range(0,3):
            if p <= wos[j]:
                #print('no worry');
                #print(wos);
                el[0] = dp[x-1][0] + 1;
                el[1] = dp[x-1][1];
                el[2] = dp[x-1][2];
                goS = False;
                break;
                
        if goS == True:
            for j in range(0,3):
                if p <= ws[j]:
                    #print('worry: ' + str(nr));
                    #print(ws);
                    if S > 0:
                        el[0] = max(dp[x-1][0:2]) + 1;
                        S = S - 1;
                    else:
                        el[1] = dp[x-1][1];
                    el[2] = dp[x-1][2];
                    break;
        #print(el);
        dp.append(el);
    fout.write("Case #"+ str(i)+ ': ' + str(dp[ln][0]) + '\n');
    fout.write
    i = i +1 ;
    #print();
#print(dp[t]);
fin.close();
fout.close();
