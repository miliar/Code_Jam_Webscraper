import copy
import math

def parse_input(inp_file):
    cases = []
    with open(inp_file) as f:
        num_cases = int(f.readline()[:-1])
        for i in range(num_cases):
            D =int( f.readline()[:-1])
            entries = map(int, (f.readline()[:-1]).split(" "))
            cases.append([D, entries])
    return cases


def inf_pancakes(cases):
    with open('data.out', 'w') as f:
        for i,case in enumerate(cases):
            #f.write("-------------------------\n")
            #f.write("%s  %s \n"%(case[0] , case [1]))
            ret =  exec_case(case)
            f.write("Case #%d: %d\n" %(i+1,ret))
            #f.write("-------------------------\n")
            #print("Case #%d: %d\n" %(i+1,ret))
            #print "===================================="
    f.close()


def exec_case(case):
    D, entries =  case
    #print D, entries
    change = 1
    tot_change = 0
    max_inds, highest = argmaxx(entries)
    min_val = highest
    for i in range(1,highest):
        tot = i
        for j in range(D):
            if entries[j] > i:
                if entries[j]%i == 0:
                    tot = tot + (entries[j]/i) - 1
                else:
                    tot = tot + (entries[j]/i)
        min_val = min(min_val, tot)
    return min_val
                
    
    
def argmaxx(lst):
    max_num = 0
    max_inds = []
    for i in range(len(lst)):
        if lst[i] > max_num:
            max_num = lst[i]
            max_inds = [i]
        elif lst[i] == max_num:
            max_inds.append(i)
    return max_inds, max_num


if __name__ == '__main__':
    cases = parse_input('data.in')
    inf_pancakes(cases)
    
    #print apply_special([11,11,11,11])
    #print "Result : ", int(exec_case([0,[7,1,8]]))
