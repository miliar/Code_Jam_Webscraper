#Bathroom Stalls - Problem C
#Google Code Jam - Qualification round 8/4/2017
#Theo Vickery

from queue import Queue
from math import *

def split(n):
    if n%2==0:
        return int(n/2), int(n/2-1)
    else:
        return int((n-1)/2), int((n-1)/2)
    
def main():
    t = int(input())
    case_list = []
    for i in range(t):
        line = input()
        n_temp = int(line.split()[0])
        k_temp = int(line.split()[1])
        case_list.append((n_temp, k_temp))

    for c in range(1, t+1):
        n, k = case_list[c-1]
        d = {n:1}
        i = 0
        q = Queue()
        
        while not i >= k:
            highest = max(d.keys())
            current = d.pop(highest)
            larger, smaller = split(highest)
            if larger > 0:
                d[larger] = d.get(larger, 0) + current
                q.put(larger)
            if smaller > 0:
                d[smaller] = d.get(smaller, 0) + current
                q.put(smaller)
            i+=current
            

        print("Case #{}: {} {}".format(c, larger, smaller))

main()
