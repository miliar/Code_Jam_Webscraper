import math
import numpy as numpy


inp=open('C-small-1-attempt0.in', 'r')
out=open("C-small-1.out", 'w')

T=int(inp.readline())
for index in range(T):
	N, K=[int(x) for x in (inp.readline()).split()]
	inter=[N]
	for k in range(K-1):
		temp=inter.pop();
		if temp!=1:
			if (temp % 2)==0:
				inter.append(temp/2);
				inter.append(temp/2-1);
			else:
				inter.append((temp-1)/2);
				inter.append((temp-1)/2);
		inter=sorted(inter);
	temp=inter.pop();
	if (temp % 2)==0:
		result=(temp/2, temp/2-1);
	else:
		result=(temp/2, temp/2);

	out.write('Case #{}: {} {}\n'.format(index+1, result[0], result[1]))




inp.close()
out.close()
