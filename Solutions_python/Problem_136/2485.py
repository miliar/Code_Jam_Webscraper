def remaining_time(win_cookie, cookie_earned, farm_earned, farm_extras):
    return (win_cookie - cookie_earned) / (farm_earned * farm_extras + 2) 
    
def farm_good(cookie_earned, farm_earned, farm_cost, farm_extras, win_cookie): 
    Tb = remaining_time(win_cookie, cookie_earned - farm_cost, farm_earned + 1, farm_extras)
    Tc = remaining_time(win_cookie, cookie_earned, farm_earned, farm_extras)
    return Tb < Tc
    
def calculate_time(C, F, X):
    import pdb
    #pdb.set_trace()
    T = 0
    cookies = 0
    farms = 0
    while cookies < X:
        if cookies >= C:
            if farm_good(cookies, farms, C, F, X):
                farms += 1
                cookies -= C
                
            else:
                T += (X - cookies) / (farms*F + 2)
                break
                    
        T1 = (X - cookies) / (farms*F + 2)
        T2 = (C - cookies) / (farms*F + 2)
        
        if (T1 < T2):
            cookies = X
            T += T1
        else:
            T += T2
            cookies  = C
            
    return T
              
foo = input() 

for i in range(0, foo):
    UI = raw_input()
    UIF = map(float, UI.split())
    
    print "Case #%d: %.7f" % (i + 1, calculate_time(UIF[0], UIF[1], UIF[2]))
