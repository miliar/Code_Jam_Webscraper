import math
import heapq

FILE = 'A-large.in'

def solve(K, pancakes):
    for pancake in pancakes: pancake.append(pancake[0]*pancake[1]*2)
    select = heapq.nlargest(K-1, pancakes, key=lambda x: x[2])
    max_flat = max(select, key=lambda x: x[0], default=(0,))[0]**2
    for pancake in select: pancakes.remove(pancake)
    last_pancake_options = [pancake[2]+max((pancake[0]**2-max_flat,0)) for pancake in pancakes]
    return math.pi*(sum([pancake[2] for pancake in select])+max_flat+max(last_pancake_options))

def format_output(case, answer):
    return 'Case #{0}: {1}'.format(case,answer)

with open(FILE,'r') as infile:
    with open('output_'+FILE,'w') as outfile:
        for case_number in range(1,int(infile.readline().rstrip())+1):
            N, K = map(int,infile.readline().rstrip().split())
            pancakes=[]
            for line_number in range(N):
                pancakes.append(list(map(int,infile.readline().rstrip().split())))
            outfile.write(format_output(case_number,solve(K, pancakes))+'\n')
        
