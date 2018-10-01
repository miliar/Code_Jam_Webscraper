
# coding: utf-8

# In[1]:

def read_problem(filename):
    with open(filename,'rt') as file:
        problem = file.read()
    return problem


# In[2]:

def process_problem(problem):
    problem = problem.splitlines()
    return (int(problem[0]),[int(x) for x in problem[1:]])


# In[3]:

def format_results(filename,results):
    with open(filename,'wt') as file:
        file.write('\n'.join(['Case #{0}: {1}'.format(index+1,val) for index,val in enumerate(results)]))


# In[33]:

def solve (N, tidy):
    if N > 0:
        ordered_section = str(N)
        len_N = len(ordered_section)
        
        # Esta toda la seccion ordenada? Add the rest as zeros
        while re.fullmatch(tidy,ordered_section) is None:
            # No esta ordenada? Entonces dividir or diez y restar 1 y volver a comprobar
            ordered_section = str((int(ordered_section)//10)-1)
        
        num_nines = len_N - len(ordered_section)
        temp = int(ordered_section + '9'*num_nines)
        if temp > N: temp = temp //10
        
        return(temp)


# In[34]:

def solve_brute (N, tidy):
    if N > 0:
        ordered_section = str(N)
        
        # Esta toda la seccion ordenada? Add the rest as zeros
        while re.fullmatch(tidy,ordered_section) is None:
            # No esta ordenada? Entonces dividir or diez y restar 1 y volver a comprobar
            ordered_section = str(int(ordered_section)-1)
        return(int(ordered_section))


# In[40]:

size_problem = 'large'
T,Ns = process_problem(read_problem('B-'+size_problem+'.in'))


# In[41]:

import re
tidy = re.compile('[0]*[1]*[2]*[3]*[4]*[5]*[6]*[7]*[8]*[9]*')
results = list()
results_brute = list()
for cur_N in Ns:
    results.append(solve(cur_N,tidy))
    #results_brute.append(solve_brute(cur_N,tidy))
    format_results('output_'+size_problem+'.out',results)


# In[37]:

#for index in range(len(results)):
    #print(Ns[index], results[index], results_brute[index], results[index] == results_brute[index])

