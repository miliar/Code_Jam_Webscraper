'''
Created on Apr 12, 2014

@author: Federico
'''
lst_number = [line.strip() for line in open('B-large.in', "r")][::-1]
file_solution = open('result.txt', 'w')
number_test = int(lst_number.pop())

for index in range(1, number_test + 1):
    C, F, X = map(float, lst_number.pop().strip().split())
    production = 2.0
    upper_bound = X / 2.0
    t0 = C / production
    t1 = X / production
    total = 0 
    if t1 < t0:
        file_solution.write("Case #{}: {:.7f}\n".format(index, t1))
    else:
        while (C* 1.0 / (production) + (X * 1.0 / (production + F)))  < (X * 1.0 / (production)):
            t0 = C * 1.0 / production
            t1 = X * 1.0 / production
            total += t0
            production += F
        t1 = X * 1.0 / (production)           
        total += t1

        

        file_solution.write("Case #{}: {:.7f}\n".format(index, total))
file_solution.close()
