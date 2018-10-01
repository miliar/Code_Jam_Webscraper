#!/usr/bin/python2.5

def permute(s, d):
    global first_time
    global next_number
    for i in range(s,length):
        d[i],d[s] = d[s],d[i]
        permute(s+1, d)
        d[i],d[s] = d[s],d[i]
    if (s+1 == length): 
        new_number = int("".join(map(str, d)))
        if (first_time and new_number > current_number):
            first_time = False
            next_number = new_number
        if (new_number > current_number and new_number < next_number):
            next_number = new_number

def compute_next_number(data):
    return permute(0, data)

T = input()
for case in range(T):
    n = input()
    current_number = n
    nstr = str(n)
    data = map(int, nstr)
    data.insert(0, 0)
    data.sort()
    first_time = True
    length = len(data)
    next_number = 0
    compute_next_number(data)
    print('Case #%d: %d') % (case+1, next_number)
