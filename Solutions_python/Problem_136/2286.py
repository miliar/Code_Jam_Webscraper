t = int(raw_input())
for case in range(t):
    c, f, x = raw_input().split()
    c = float(c)
    f = float(f)
    x = float(x)
    k = 2
    time = 0
    max_t = x / k
    t_farm = c / k
    points = 0
#    while((max_t - t_farm) < x / (k + f)):
#        k += f
#        time += t_farm
    
    while(points <= x):
        max_t = x / k
        t_farm = c / k
        time += t_farm
        if(((max_t - t_farm) > x / (k + f))):
            k += f
            points = 0
        else:
            time += (x - c) / k 
            break
    print 'Case #%i:'%(case + 1), time        
            
        
