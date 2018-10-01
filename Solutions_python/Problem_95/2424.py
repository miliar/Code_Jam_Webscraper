#!/usr/bin/python/

f1 = "A-small-attempt2.in"
f2 = "output_SiT.dat"
fin = open(f1,'r')
fout = open(f2,'w')

test_string = 'ynficwlbkuomxsevzpdrjgthaq '
match_string = 'abcdefghijklmnopqrstuvwxyz '

n = int(fin.readline())

for i in range(n):
	G = fin.readline()
	output = 'Case #'+str(i+1)+': '
	for j in range(len(G)-1):
		x = test_string.index(G[j])
		output+=match_string[x]
	print>>fout,output

