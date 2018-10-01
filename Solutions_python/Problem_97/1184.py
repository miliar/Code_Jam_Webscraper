'''
Created on 14-04-2012

@author: Marta
'''

def starts_with_zero(string_number):
    return string_number[0] == '0'

def shift_string(string_number):
    return string_number[1:] + string_number[0]

def in_bounds(A, B, n_string, m_string):
    return A <= int(n_string) and int(n_string) < int(m_string) and int(m_string) <= B

def get_possible_count(A, B, n_string):
    next = n_string
    possibs = {}
    for i in range(len(n_string)-1):
        next = shift_string(next)
        if (not starts_with_zero(next)) and in_bounds(A, B, n_string, next):
            possibs[next] = 1
    return len(possibs.keys())
            
def get_count(A, B):
    count = 0
    for i in range(A, B+1):
        count += get_possible_count(A,B, str(i))
    return count
        
def process_input(in_filename, out_filename):
    file = open(in_filename, 'r')
    output = open(out_filename, 'w+')
    # dont care abount number of cases
    file.readline()  
    i = 0  
    for line in file.readlines():
        i+=1
        numbers = line.split()
        A = int(numbers[0]) # number of suprising tripets
        B = int(numbers[1]) # score_linit
        result = get_count(A, B)
        heading = "Case #%d: %d\n" %(i, result)
        output.write(heading)
        
if __name__ == '__main__':
    process_input('../input/C-small-attempt1.in', '../output/output')