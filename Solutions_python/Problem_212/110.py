import sys
import math

def max_fresh(tours, pack_size):
    num_left = [0] * pack_size
    for tour in tours:
        num_left[tour % pack_size] += 1
    
    ret = num_left[0]
    
    if pack_size == 2:
        ret += math.ceil(num_left[1] / 2)
    elif pack_size == 3:
        while num_left[1] > 0 and num_left[2] > 0:
            ret += 1
            num_left[1] -= 1
            num_left[2] -= 1
        ret += math.ceil(sum(num_left[1:3])/3)
    elif pack_size == 4:
        #match the odds till one runs out
        while num_left[1] > 0 and num_left[3] > 0:
            ret += 1
            num_left[1] -= 1
            num_left[3] -= 1
        
        #match the evens till run out
        while num_left[2] > 1:
            ret += 1
            num_left[2] -= 2
            
        #find which of the odds still has left
        odds = 1
        if num_left[3] > num_left[1]:
            odds = 3
        
        #pair of 3
        if num_left[odds] > 1 and num_left[2] > 0:
            num_left[odds] -= 2
            num_left[2] -= 1
            ret += 1
        
        #kill left over odds
        while num_left[odds] > 3:
            num_left[odds] -= 4
            ret += 1
        
        #either remainder gets fresh pack
        if num_left[odds] > 0 or num_left[2] > 0:
            ret += 1
        
    return ret

def solve(in_file, out_file):
    num_cases = int(in_file.readline().strip())
    for case in range(1, num_cases + 1):
        #Read in data
        num_tours, pack_size = (int(val) for val in in_file.readline().strip().split())
        tours = [int(val) for val in in_file.readline().strip().split()]
        
        sol = max_fresh(tours, pack_size)
        #Call func for solution
        out_file.write("Case #{}: {}\n".format(case, sol))

if __name__ == '__main__':
    from_file = True
    alt_out = False
    
    if from_file:
        path = 'Data\\'
        #name = 'A-sample'
        #name = 'A-small-attempt0'
        name = 'A-large'
        file_input = open(path + name + '.in', 'r')
        out_full_name = path + name +'.out'
        if alt_out:
            out_full_name = path + name + "naive" +'.out'            
        file_output = open(out_full_name,'w')
        solve(file_input, file_output)
        file_input.close()
        file_output.close()
    else:
        solve(sys.stdin, sys.stdout)
        
        
