# -*- coding: utf-8 -*-

# R: R times in a day
# k: hold k people at once

filename = "C-small-attempt3.in"

def convert2int_tuple(str_list):
    result = []
    for s in str_list:
        result.append(int(s))
    return tuple(result)

def read_T():
    f = open(filename, "r")
    T = int(f.readline().strip())
    f.close()
    return T

def read_question3():

    f = open(filename, "r")
    T = f.readline().strip()

    RkNSet = []

    for i in range(50):
        RkN = convert2int_tuple(f.readline().strip().split(" "))
        Ns = convert2int_tuple(f.readline().strip().split(" "))
        RkNSet.append((RkN, Ns))

    f.close()

    return RkNSet

def get_as_que(l, index):
    if len(l) <= index:
        return l[index%len(l)]
    else:
        return l[index]

RkNSet = read_question3()

total_sum_list = []
T = read_T()
for i in range(T):
    print i
    set1 = RkNSet[i]
    R = set1[0][0]
    k = set1[0][1]
    max = set1[0][2]
    ns = set1[1]
    #print R, k, ns
    start = 0
    total_sum = 0
    for j in range(R):
        sum = 0
        count = 0
        while True:
            candidate = get_as_que(ns, start)
            #print candidate
            tmp = sum+candidate
            if tmp <= k and count<max:
                #print tmp, k
                count+=1
                sum+=candidate
                start+=1
            else:
                #print "sum", sum
                count=0
                break
        total_sum += sum
    total_sum_list.append(total_sum)

f = open("Output.txt", "w")
for i in range(len(total_sum_list)):
    f.write("Case #" + str(i+1) + ": " + str(total_sum_list[i]) + "\n")
f.close()