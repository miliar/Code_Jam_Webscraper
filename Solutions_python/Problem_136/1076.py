T = int(input())
for m in range(0,T):
    C, F, X = [float(x) for x in input().split(' ')]
    noOfFarms = 0
    min_time = X / 2.0
    freq = 2.0
    farmTime = 0.0
    while(1):
        noOfFarms += 1 
        farmTime += C / freq 
        freq += F
        current_time = X/freq + farmTime
        if current_time > min_time:
            break
        else:
            min_time = current_time
    print( 'Case #' + str(m+1) + ': ' + str(round(min_time,7)) )  
             

