
with open('input.txt') as f:
    
    case_count = int(f.readline().strip())
    
    for index in range(case_count):
        args = f.readline().strip().split(' ')
        
        C = float(args[0])
        F = float(args[1])
        X = float(args[2])
        
        production = 2.0
        total_time = X / production
        factory_time_cost = C / production
        
        running_time = 0.0
        
        while True:
            running_time += factory_time_cost
            
            new_production = production + F
            new_time_cost = running_time + (X / new_production)
            
            if total_time < new_time_cost:
                break
                
            production = new_production
            total_time = new_time_cost
            factory_time_cost = C / production
            
        print 'Case #' + str(index + 1) + ': ' + str(total_time)