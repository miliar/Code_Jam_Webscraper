import math
import numpy as numpy


inp=open('B-small-attempt0.in', 'r')
out=open("B-smallout", 'w')

def isSorted(blah):
	n=len(blah); idx=0;
	while idx<n-1:
		if int(blah[idx])> int(blah[idx+1]):
			return False;
		idx=idx+1;
	return True;

def treatAnnoying(blah):
	n=len(blah); idx=0;
	temp=str(int(blah[n-2])-1);
	while (idx<n-1 and blah[n-1-idx]==blah[n-2-idx]):
		idx=idx+1;
	if idx!=n-1:
		result = str(int(blah[0: n-1-idx]));
		for i in range(idx+1):
			result=result+temp;
		result=result+'9';
		return result;
	else:
		result=str(int(blah[0])-1)
	for i in range(idx+1):
		result=result+'9';
	return result; 


T=int(inp.readline())
for index in range(T):
	N=str(int(inp.readline()));
	temp=len(N);
	print temp
	if len(N)<4:
		result=N;
		while (not isSorted(result)):
			result=str(int(result)-1);
	else:
		for n in range(len(N)):
			result=N[0:n];
			if N[n-1]>N[n]:
				result=treatAnnoying(result);
				idx=n+1;
				while (idx<len(N)):
					result=result+"9";
					idx=idx+1;
				result=str(int(result));
				break;
	out.write('Case #{}: {}\n'.format(index+1, result))




inp.close()
out.close()
