import sys

def slowest(horses, end):
    max_score = 0
    for pos, speed in horses:
        score = (end - pos)/speed
        if score > max_score:
            max_score = score
    return end / max_score

def solve(in_file, out_file):
    num_cases = int(in_file.readline().strip())
    for case in range(1, num_cases + 1):
        #Read in data
        end, num_horses = (int(val) for val in in_file.readline().strip().split())
        horses = []
        for _ in range(num_horses):
            pos, speed = (int(val) for val in in_file.readline().strip().split())
            horses.append((pos, speed))
        sol = slowest(horses, end)
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
        
        
