# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 11:20:06 2017

@author: Emad Yehya
"""

fi = file('B-large.in', 'r')
fo = file('out.txt', 'w')

T = int(fi.readline()[:-1])

def solve_for_str(N):
    breakat = -1
    for i in range(1, len(N)):
        if(N[i] < N[i-1]):
            breakat = i
            break
    if(breakat == -1):
        return N
    init_base = str(int(N[0:breakat]) - 1)
    other_len = len(N) - breakat
    ans = "9"*other_len
    if(init_base != "0"):
        ans = solve_for_str(init_base) + ans
    return ans
    

    
    
for t in range(1, T+1):
    N = str(fi.readline())[:-1]
    #find first break, if any
    fo.write("Case #" + str(t) + ": " + solve_for_str(N) + "\n")
    print N, solve_for_str(N)
    
fi.close()
fo.close()