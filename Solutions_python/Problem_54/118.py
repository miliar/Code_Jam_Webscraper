
def gcd (a,b):
    "gcd (a, b)  -  claculate greatest common divisor of a and b"
    if a==0:
        return b
    if b==0:
        return a
    while b != 0:
        a,b = b, a %b
    return a

def gcd_list (l):
    "gcd_list (l)  -  claculate greatest common divisor of all numbers in list l"
    g = l[0]
    for i in l[1:]:
        g = gcd(g,i)
    return g



f_in = open('c:/temp/codejam/qualification/B-large.in')
f_out = open('c:/temp/codejam/qualification/B-large.out','w')

C = int(f_in.readline())
print (C)
for case in range(C):
    line = f_in.readline()
    list_of_event_times = [int(x) for x in line.split()][1:]
    max_time= max(list_of_event_times)
    time_differences = [max_time - x for x in list_of_event_times]
    g = gcd_list (time_differences)
    #print (list_of_event_times, time_differences, g)
    t_i = list_of_event_times[-1]
    if t_i % g == 0:
        res = 0
    else:
        res = (t_i// g +1)*g - t_i

    f_out.write('Case #' + str(case+1) + ': ' + str(res) + '\n')


f_in.close()
f_out.close()

