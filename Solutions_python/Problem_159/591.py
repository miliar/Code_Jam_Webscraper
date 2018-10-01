#!/usr/bin/env python 

def read_input(filename):
    lines = []
    with open(filename) as f:
        for line in f:
            lines.append([int(x) for x in line.rstrip().split()])
                 
    n_cases = lines[0][0]
    cases = []
    for i,line in enumerate(lines[1:]):
        if i % 2 == 0:
            continue
        else:
            cases.append(line)
            
            
    return cases
    
def first_method(time_steps):
    
    n_eaten = 0
    for i,n_mush in enumerate(time_steps):
        if i == 0:
            # starting configuration
            pass
        elif n_mush >= time_steps[i-1]:
            # no mushrooms were added
            pass
        else:
            n_eaten += time_steps[i-1] - n_mush
            
    return n_eaten
    
def second_method(time_steps):
    
    n_eaten = 0
    
    difference = [(x-y) for x,y in zip(time_steps[:-1],time_steps[1:])]
    min_rate = max(difference) 
    
    for i,n_mush in enumerate(time_steps[:-1]):
        if n_mush < min_rate:
            n_eaten += n_mush
        else:   
            n_eaten += min_rate
                
    return n_eaten      
    
def main():

    input_cases = read_input("A-large.in")
    output = open('output_Alarge.dat','w')
    
    for i,case in enumerate(input_cases):
        n_first = first_method(case)
        n_second = second_method(case)

        output.write('Case #%d: %d %d\n' % (i+1,n_first,n_second))
        
    output.close()
    
if __name__ == "__main__":
    main()
            
