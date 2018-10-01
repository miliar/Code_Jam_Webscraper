fout = open('DeceitfulAns.txt', 'w')
fin = open('D-large.in','r')
T = int(fin.readline())
for i in range(T):
    count = int(fin.readline());
    naomi = map(float, fin.readline().split());
    ken = map(float, fin.readline().split());
    naomi.sort();
    ken.sort();
    naomicurrent = 0;
    kencurrent = 0;
    while(kencurrent < len(ken)):
        while(kencurrent < len(ken) and ken[kencurrent] < naomi[naomicurrent]):
            kencurrent += 1;
        if(kencurrent >= len(ken)):
            break;
        naomicurrent += 1;
        kencurrent += 1;
    naomiWarBalls = count - naomicurrent;
    naomicurrent = 0;
    kencurrent = 0;
    while(naomicurrent < len(naomi)):
        while(naomicurrent < len(naomi) and naomi[naomicurrent] < ken[kencurrent]):
            naomicurrent += 1;
        if(naomicurrent >= len(naomi)):
            break;        
        naomicurrent += 1;
        kencurrent += 1;
    naomiDeceitfulWarBalls = kencurrent;    
    fout.write('Case #' + str(i + 1) + ': '   + str(naomiDeceitfulWarBalls)+ ' ' + str(naomiWarBalls) + '\n');


fin.close()
fout.close()
        
