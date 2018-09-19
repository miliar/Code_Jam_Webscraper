#!/usr/bin/env python3
from collections import Counter


rounds = int(input())
for i in range(rounds):
	A, B, K =input().split()
	A=int(A)
	B=int(B)
	K=int(K)
	
	times = sum( ( 1 for i in range(A) for j in range(B) if i&j < K )  )
	print("Case #{}: {}".format(i+1,times))
 
