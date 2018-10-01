import os
import numpy as np

INPUT = os.environ.get("INPUT",'q2_input.txt')
input1 = open(INPUT,'r')
output1 = open('B_output.txt', 'w')
q = input1.read().split('\n')

def f(n):
    reverse_arr = np.array([int(i) for i in n])[::-1]
    for i, c in enumerate(reverse_arr[:-1]):
        if c < reverse_arr[i+1]:
            reverse_arr[i+1] = reverse_arr[i+1]-1
            reverse_arr[:i+1] = np.zeros_like(reverse_arr[:i+1])+9
    return int(''.join(reverse_arr[::-1].astype('U8')))

for i in range(1,int(q[0])+1):
    output1.write('Case #%s: %d\n'%(i, f(q[i])))
input1.close()
output1.close()