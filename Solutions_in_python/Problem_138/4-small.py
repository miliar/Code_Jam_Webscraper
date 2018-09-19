# Deceitful War - Short

import math
import time

def Greater(X,Y,n):

    sum_greater = 0

    for i,j in zip(X,Y):

        if i > j:

            sum_greater += 1

    if sum_greater == n:

        return True

    else:

        return False

time_start = time.time()

file_input = open('D-large.in')
file_out = open('output_4_large.txt','w')
file_out.write('')
file_out.close()

Test_Cases = [int(a) for a in file_input.readline().split(' ')][0]

N = 1

while N <= Test_Cases:

    n = [int(a) for a in file_input.readline().split(' ')][0]

    n_d = n

    Naomi = sorted([float(a) for a in file_input.readline().split(' ')])

    Naomi_2 = Naomi[:]
    
    Ken = sorted([float(a) for a in file_input.readline().split(' ')])

    Ken_2 = Ken[:]

    Naomi_score = 0

    #### Playing War ####

    while n > 0:

        Naomi_block = Naomi[0]

        Ken_greater = [i for i in Ken if i > Naomi_block]

        if len(Ken_greater) > 0:

            Ken.remove(Ken_greater[0])

            Naomi.remove(Naomi_block)

        else:

            Ken.remove(Ken[0])

            Naomi.remove(Naomi_block)

            Naomi_score += 1

        n-=1

    #### Playing Deceitful War ####

    Naomi_score_d = 0

    while n_d > 0:

        if Greater(Naomi_2,Ken_2,n_d):

            Naomi_score_d = len(Naomi_2)

            n_d = 0

        else:

            Naomi_2.remove(Naomi_2[0])
            Ken_2.remove(Ken_2[-1])

            n_d -=1
        
            
    file_out = open('output_4_large.txt','a')
    file_out.write('Case #'+str(N)+': '+str(Naomi_score_d)+' '+str(Naomi_score)+'\n')
    file_out.close()
    print('Case #'+str(N)+': '+str(Naomi_score_d)+' '+str(Naomi_score))

    N+=1

time_end = time.time()

print('Time taken: '+str(time_end-time_start)+' sec')

