##libraries function
from math import *
import numpy as np

##custom file name
file_n = 'C-large-1'

##template
input = open(file_n + '.in', 'r')
output = open(file_n + '.out', 'w')

n_case = int(input.readline())

def palindrome(n):
	return str(n) == str(n)[::-1]

fs = set()
for k in range(1, trunc(sqrt(10 ** 14))+1):
	if palindrome(k) and palindrome(k**2):
		fs.add(k ** 2)

for z in range(1, n_case+1):

	[n,m] = map(int, input.readline().split(' '))

	result = len([i for i in fs if i >= n and i <= m])

	output.write('Case #' + str(z) + ': ' + str(result) + '\n')

output.close()
