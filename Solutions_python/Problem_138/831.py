#!/usr/bin/env python
import sys

def print_result(tc_number, res):
    print "Case #{0}:".format(tc_number), res

def deceitful_war():
    pass

# def min_eq(num, lst):
#     res = []
#     for i in lst:
#         if num > i:
#             res.append(i)
#     if len(res) == 0:
#         return 0
#     return min(res)

def war(Naomis, Kens):
    result = 0
    naomis = sorted(Naomis, reverse=True)
    kens = sorted(Kens)
    for i in kens:
        for j in naomis:
            if i > j:
                result += 1
                naomis.remove(j)
                break
    return result

def deceitful_war(Naomis, Kens):
    result = 0
    naomis = sorted(Naomis)
    kens = sorted(Kens, reverse=True)
    for i in naomis:
        for j in kens:
            if i > j:
                result += 1
                kens.remove(j)
                break
    return result





def main():
    data = sys.stdin
    T = int(data.readline())
    
    test_case = 1       
    while test_case <= T:
        N = int(data.readline())
        Naomis, Kens = [], []
        y = 0 #score if she plays Deceitful War optimally 
        z = 0 #score if she plays War optimally

        Naomis = map(float, data.readline().split())
        Kens = map(float, data.readline().split())
        
        if N == 1:
            if Naomis[0] > Kens[0]:
                # print Naomis, Kens
                y, z = 1, 1
        else:
            y = deceitful_war(Naomis, Kens)
            z = N - war(Naomis, Kens)
            

        print_result(test_case, ' '.join(map(str, (y, z))))        
        
        test_case += 1    

    
if __name__ == '__main__':
    main()