import math
import numpy as numpy


def flip(S, K, idx):
	for k in range(K):
		if S[idx+k]=='+':
			S[idx+k]='-';
		else:
			S[idx+k]='+';

def isOk(S, target):
	i=0;
	while i<len(S):
		if(S[i]!=target):
			return False
		i+=1;
	return True

def apply(S, K, target):
	compteur=0;
	for i in range(len(S)-K+1):
		if S[i]!=target:
			flip(S, K, i);
			compteur+=1;
	if isOk(S, target):
		return compteur;
	else:
		return 100000000;

def reverse(S):
	S2=[]
	for i in range(len(S)):
		S2.append(S[i])
	return S2



inp=open('A-large.in', 'r')
out=open("A-large.out", 'w')

T=int(inp.readline())
for index in range(T):
	S, K=[x for x in (inp.readline()).split()] 
	K=int(K); S=list(S);
	print K;
	print S;
	cp=apply(list(S), K, '+'); 
	result=cp;
	if result>10000000:
		result="IMPOSSIBLE";
	print result
	out.write('Case #{}: {}\n'.format(index+1, result))




inp.close()
out.close()
