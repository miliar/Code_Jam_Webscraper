import sys

infile = open(sys.argv[1])

try:
    outfile = open(sys.argv[2], 'w')
    
except IndexError:
    outfile = sys.stdout
    
base_elements = 'QWERASDF'
    
for index, line in enumerate(infile.readlines()):
    
    if index == 0:
        continue
    
    terms = line.split()
    
    num_combos = int(terms[0])
    combos = terms[1:num_combos + 1]
    
    num_cancels = int(terms[num_combos + 1])
    cancels = terms[num_combos + 2:num_combos + num_cancels + 2]
        
    combo_dict = {}
    cancel_dict = {}
    extra_cancels = []
    
    for combo in combos:
        
        combo_dict[combo[:-1]] = combo[-1]
        combo_dict[combo[:-1][::-1]] = combo[-1]
    
    combos = combo_dict
    
    for cancel in cancels:
        extra_cancels.append(cancel[::-1])
        
    cancels += extra_cancels
    
    for cancel in cancels:
        
        cancel_dict[cancel[0]] = cancel[1]
        cancel_dict[cancel[1]] = cancel[0]
        
    invocations = terms[-1]
    
    elements = []
    
    for eindex, element in enumerate(invocations):
        
        elements.append(element)
        
        last_two = ''.join(elements[-2:])
            
        if last_two in combos:
            elements = elements[:-2] + [combos[last_two]]
            
        elif element in cancel_dict:
            
            if cancel_dict[element] in elements:
                elements = []
                
    print >> outfile, 'Case #%d: [%s]' % (index, ', '.join(elements))