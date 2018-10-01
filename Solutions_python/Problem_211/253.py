from decimal import *

N = 0
K = 0
t_unit = 0.0
data = []

def isPossible(pi):
    global N, K, t_unit, data
    total = Decimal(0.0)
    for i in range(N):
        if i != pi and data[i] < data[pi]:
            total += data[pi] - data[i]

    if total <= t_unit:
        return True
    else:
        return False

def fillUpTo(pi):
    global N, K, t_unit, data
    for i in range(N):
        if i != pi and data[i] < data[pi]:
            t_unit -= data[pi] - data[i]
            data[i] = data[pi]

def useRemaining(pi):
    global N, K, t_unit, data
    count = 0
    pivot_data = data[pi]
    for i in range(N):
        if data[i] == pivot_data:
            count += 1
            
    for i in range(N):
        if data[i] == pivot_data:
            data[i] += t_unit / count
            
def run():
    global N, K, t_unit, data
    data = sorted(data, reverse=True)

    for i in range(N):
        if isPossible(i):
            fillUpTo(i)
            useRemaining(i)
            break

    ret = 1
    for i in range(N):
        ret *= data[i]

    return ret    

fi = open("C-small-1-attempt0.in", "r")
fo = open("c_output.txt", "w")

getcontext().prec = 50

T = int(fi.readline())
for i in range(T):
    temp = fi.readline()
    N = int(temp.split()[0])
    K = int(temp.split()[1])
    temp = fi.readline()
    t_unit = Decimal(float(temp))
    data = []
    temp_list = fi.readline().split()
    for j in range(len(temp_list)):
        temp_list[j] = Decimal(temp_list[j])
        
    data = temp_list

    answer = run()

    fo.write("Case #" + str(i+1) + ": " + str(answer) + "\n")
    print i

fi.close()
fo.close()
