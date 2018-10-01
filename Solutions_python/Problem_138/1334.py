'''
Created on Apr 12, 2014

@author: Andrew
'''

def solve_case(Na_list, Ke_list):
    N_list = Na_list
    K_list = Ke_list
    points = 0
    for block in N_list:
        larger_list = []
        for b in K_list:
            if b > block:
                larger_list.append(b)
        if larger_list == []:
            points += 1
            K_list.remove(K_list[0])
        else:
            K_list.remove(larger_list[0])
            
    return points

def solve_case_flip(Na_list, Ke_list):
    N_list = Na_list
    K_list = Ke_list
    points = 0
    for block in K_list:
        larger_list = []
        for b in N_list:
            if b > block:
                larger_list.append(b)
        if larger_list == []:
            points += 1
            N_list.remove(N_list[0])
        else:
            N_list.remove(larger_list[0])
            
    return len(K_list)-points


def solve():        
    text = open("google.in", "r")
    test_cases = int(text.readline())
    total_cases = [[] for x in range(0,test_cases)]
    
    for x in range(0, test_cases):
        text.readline()
        total_cases[x].append([float(i) for i in text.readline().split()])
        total_cases[x].append([float(i) for i in text.readline().split()])
        
    text.close()
    
    solution = open("solution.txt", "w")
    number = 1
    for case in total_cases:
        a = sorted(case[0])
        b = sorted(case[1])
        answer1 = solve_case_flip(a,b)
        case[0].sort()
        case[1].sort()
        answer2 = solve_case(case[0],case[1])
        solution.write("Case #" + str(number) + ": " + str(answer1) + " " + str(answer2) + "\n")
        number += 1
    solution.close()
    
solve()
