'''
Created on May 26, 2012

@author: Lior
'''

def keyfunc(vine):
    i,d,l = vine

def solve(D, vines, current_place, current_vine, mem=None):   
    if mem is None:
        mem = {}
    key = (current_place, current_vine)
    if key in mem:
        return mem[key]
    i, current_d, current_l = vines[current_vine]
    reach = current_d-current_place
    if current_place + 2*reach >= D:
        mem[key] = True
        return True
    available_vines = [(i, d,l) for (i, d,l) in vines[current_vine+1:] 
                       if (d >= current_place and d <= current_place + 2*reach)]
    
    for vine_index, next_d, next_l in available_vines:
        result = solve(D, vines, 
                       current_place=max(current_d, next_d-next_l), 
                       current_vine=vine_index,
                       mem=mem)
        if result:
            mem[key] = True
            return True
    mem[key] = False
    return False
    
             
def process_files(in_file, out_file):
    num_of_test_cases = int(in_file.next().strip())
    for test_number in xrange(num_of_test_cases):
        N = int(in_file.next().strip())
        vines = []
        for i in xrange(N):
            d, l = (int(i) for i in in_file.next().strip().split())
            vines.append((i, d, l))
        D = int(in_file.next().strip())
        result = 'YES' if solve(D, vines, 0, 0) else 'NO'
        out_file.write('Case #%d: %s\n' % (test_number+1, result))

if __name__ == '__main__':
    with open('small1.in', 'rb') as in_file:
        with open('small1.out', 'wb') as out_file:
            process_files(in_file, out_file)
        