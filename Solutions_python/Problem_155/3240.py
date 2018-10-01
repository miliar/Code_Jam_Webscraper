

def solve(case_num, input):
    parts = input.split(" ")
    max_shyness_level = int(parts[0])

    count_per_level = list(parts[1])
    
    # print(max_shyness_level)
    # print(count_per_level)
    
    current_level = 1
    num_of_currently_activated = int(count_per_level[0])
    num_of_friends_to_add = 0
      
    if max_shyness_level == 0: 
        print "Case #" + str(case_num) + ": 0"
    else:    
        while current_level != max_shyness_level+1:
            if int(count_per_level[current_level]) != 0:
                delta = current_level - num_of_currently_activated
                #print "current_level: " + str(current_level)
                #print "delta:" + str(delta)
                
                if delta > 0:
                    num_of_friends_to_add += delta
                    num_of_currently_activated += delta
            
            num_of_currently_activated += int(count_per_level[current_level]) 
            #print "num_of_currently_activated:" + str(num_of_currently_activated)
            current_level += 1
            
        print "Case #" + str(case_num) + ": "  + str(num_of_friends_to_add)
        


with open("input.in", "r") as ins:
    a = False
    i = 0
    for line in ins:
        if a:
            solve(i, line)
        a = True
        i += 1

# solve(0, "4 11111")