import sys

def seat_proirity(tiks):
    ret = list(range(len(tiks)))
    sort_key = lambda index: (-1 * min(tiks[index]), index)
    ret.sort(key = sort_key)
    return ret
    
def try_remove(tiks, cust, ex_seat, seat_order):
    for seat in seat_order:
        if seat == ex_seat:
            continue
        if tiks[seat][cust] > 0:
            tiks[seat][cust] -= 1
            return True
    return False

def try_promote(tiks, cust, seat):
    
    if tiks[seat][cust] > 0 and seat > 0:
        tiks[seat][cust] -= 1
        return True
    return False

def min_rides(tiks):
    pro = 0
    ret = 0
    
    while tiks[0][0] > 0:
        order = seat_proirity(tiks)
        try_remove(tiks, 1, 0, order)
        tiks[0][0] -= 1
        ret += 1
    
    for seat in range(1, len(tiks)):
        order = seat_proirity(tiks)        
        while tiks[seat][0] > 0 and try_remove(tiks, 1, seat, order):
            order = seat_proirity(tiks)
            tiks[seat][0] -= 1
            ret += 1
    
    for seat in range(1, len(tiks)):   
        while tiks[seat][0] > 0:     
            if try_promote(tiks, 1, seat):
                pro += 1
            tiks[seat][0] -= 1
            ret += 1
    
    for seat in range(0, len(tiks)):   
        ret += tiks[seat][1]
    
    return ret, pro
            
    
        
        
    
def solve(in_file, out_file):
    num_cases = int(in_file.readline().strip())
    for case in range(1, num_cases + 1):
        num_seat, num_cust, num_tik = (int(val) for val in in_file.readline().strip().split())
        
        tiks = [[0, 0] for _ in range(num_seat)]
        
        for _ in range(num_tik):
            seat, cust = (int(val) for val in in_file.readline().strip().split())
            tiks[seat - 1][cust - 1] += 1
        
        sol = min_rides(tiks)
        
        out_file.write("Case #{}: {} {}\n".format(case, *sol))

if __name__ == '__main__':
    from_file = True
    alt_out = False
    
    if from_file:
        path = 'Data\\'
        #name = 'B-sample'
        name = 'B-small-attempt0'
        #name = 'B-large'
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
        
        
