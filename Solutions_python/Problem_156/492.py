#Written by Raynger
def solve(diners, time=0):
    if max(diners) == 1:
        return time + 1
    else:
        cur_max = max(diners)
        min_t = max(diners) + time
        for i in range(1, (cur_max//2)+1):
            new_diners = []
            counter = 0
            for j in diners:
                if j == cur_max:
                    new_diners.append(i)
                    new_diners.append(j-i)
                    counter += 1
                else:
                    new_diners.append(j)
            #print(new_diners)                        
            t = solve(new_diners, time+counter)
            if min_t > t:
                min_t = t
        return min_t
            
                    
                
ans_list =[]
cases = int(input())
for c in range(cases):
    D = int(input())
    diners = input().split()
    diners = list(map(int, diners))
    #print(diners)
    output = solve(diners)
    
    #print("Outcomes:", dp)
    print("Case #{}: {}".format(c+1, output))
    #print()
    #ans_list.append(min(dp))