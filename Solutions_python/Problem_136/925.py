import sys

def print_answer(answer):
    print "Case #"+str(ii+1)+": "+str(answer)
    fout.write("Case #"+str(ii+1)+": "+str(answer)+"\n")

def solve_case(rate, overall_time):
    while X/rate > (C/rate + X/(rate+F)):
        overall_time += C/rate
        rate = rate+F
    overall_time += X/rate
    print_answer('%.7f' % overall_time)

f = open("B-large.in")
fout = open("output.txt", "w")
T = int(f.readline().rstrip())

for ii in range(T):
    line_list = f.readline().rstrip().split(" ")
    C = float(line_list[0])
    F = float(line_list[1])
    X = float(line_list[2])
    
    
    solve_case(2.0,0.0)

fout.close()
