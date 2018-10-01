#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Google Code Jam: Qualification Round 2010
# Problem C: Theme Park

T = int(input()) # number of test cases

for t in range(1,T+1):
	print('Case #{0}: '.format(t), end='')
	R,k,N = [ int(x) for x in input().split(' ') ]
	G = [ int(x) for x in input().split(' ') ]

	# precalculo cuántos grupos hay que saltarse si
	# estamos el grupo i es el que está el primero
	# dst[i] indica qué grupo se quedará el primero
	# en ese viaje
	dst = [0]*N
	euros = [0]*N
	for i in range(N):
		acum = G[i]
		next = (i+1)%N
		while acum+G[next] <= k:
			if next == i:
				next = (N+i-1)%N
				break
			acum += G[next]
			next = (next+1)%N
		dst[i] = next
		euros[i] = acum

	acum = 0
	current = 0
	visited = [False]*N
	cont = [0]*N
	runs = [0]*N
	x = 0
	while x < R:
		if visited[current]: # ciclo encontrado!
			dif_p = acum - cont[current]
			dif_r = x - runs[current]

			loops = (R-x-1)//dif_r
			rem = (R-x-1)%dif_r
			acum += loops*dif_p
			x += loops*dif_r

		visited[current] = True
		cont[current] = acum
		runs[current] = x

		acum += euros[current]
		current = dst[current]

		x += 1

	print(acum)
