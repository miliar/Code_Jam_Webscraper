#!/usr/bin/python
from itertools import groupby
import numpy as np

out=open('B-small-attempt0.out','w')
with open('B-small-attempt0.in') as fi:
    T = int(fi.readline())
    for t in range(1,T+1):
        A,B,K = [int(x) for x in fi.readline().split()]
        sum=0
        for a in range(A):
            for b in range(B):
                if ((a&b)<K) and ((a&b)>=0):
                    sum+=1
        
        out.write('Case #' + str(t) + ': ' + str(int(sum)) + '\n')


#out=open('A-large.out','w')
#with open('A-large.in') as fi:
#    T = int(fi.readline())
#    for t in range(1,T+1):
#        N = int(fi.readline())
#        strings=[]
#        strings.append(["".join(grp) for num, grp in groupby(fi.readline().rstrip('\n'))])
#        fund=[x[0] for x in strings[0]]
#        nchars=len(fund)
#        factors=np.ones((N,nchars))
#        factors[0,:]=[len(x) for x in strings[0]]
#        possible=True
#        for n in range(1,N):
#            if possible:
#                strings.append(["".join(grp) for num, grp in groupby(fi.readline().rstrip('\n'))])
#                fund2=[x[0] for x in strings[n]]
#                if fund2==fund:
#                    factors[n,:]=[len(x) for x in strings[n]]
#                else:
#                    possible=False
#
#        if possible:
#            changes=0
#            for n in range(nchars):
#                median=min(factors[:,n], key=lambda x:abs(x-sum(factors[:,n])/len(factors[:,n])))
#                changes+=sum(abs(factors[:,n]-median))
#
#            out.write('Case #' + str(t) + ': ' + str(int(changes)) + '\n')
#        else:
#            out.write('Case #' + str(t) + ': Fegla Won\n')





#from operator import add
#
#def flip(switch, circuit, L):
#    return [(2**switch+x)%(2**L) for x in circuit]
#
#def flipSeveral(coeff, circuit, L):
#    s=len(coeff)
#    out=[coeff[s-0-1]*((2**0+x)%(2**L))+x for x in circuit]
#    for l in range(1,s):
#        out=map(add, out, [coeff[s-l-1]**((2**l+x)%(2**L)) for x in circuit])
#
#    return out
#
#out=open('test.out','w')
#with open('test.in') as fi:
#    n = [int(x) for x in fi.readline().split()]
#    for y in range(1,n[0]+1):
#        N,L = [int(x) for x in fi.readline().split()]
#        inn = [int(str(x),2) for x in fi.readline().split()]
#        outt = [int(str(x),2) for x in fi.readline().split()]
#        minimum=L+1
#        for l in range(2**L):
#            coeff = [int(x) for x in list(format(l,'b'))]
#            if sum(coeff)<minimum:
#                innn = flipSeveral(coeff,inn,L)
#                print innn
#                if set(innn)==set(outt):
#                    minimum=sum(coeff)
#
#        if minimum == L+1:
#            out.write('Case #' + str(y) + ': NOT POSSIBLE\n')
#        else:
#            out.write('Case #' + str(y) + ': ' + str(minimum) + '\n')
#







#iteration=100
#out=open('B-large.out','w')
#with open('B-large.in') as fi:
#    n = [int(x) for x in fi.readline().split()]
#    for y in range(1,n[0]+1):
#    	C,F,X = [float(x) for x in fi.readline().split()]
#    	cookies=0.0
#    	f=2.0
#    	t=0.0
#    	done=False
#    	while not done:
#    		done=True
#    		t=t+X/f
#    		tB=t-X/f+C/f+X/(f+F);
#   		if tB<t:
#   			done=False
#   			t=t+C/f-X/f
#   			f=f+F
#    	out.write('Case #' + str(int(y)) + ': ' + str(float(t)) + '\n')
    	#while cookies<X:
    	#	t=t+1.0
    	#	cookies=cookies+f
    	#	if cookies >= C and (X-cookies+C)/(f+F)>(X-cookies)/(f):
    	#		cookies = cookies - C
    	#		f = f + F
    	#excess=cookies-X
    	#t=t-excess/f
    	






#out=open('A-small-attempt3.out','w')
#with open('A-small-attempt3.in') as f:
#    n = [int(x) for x in f.readline().split()]
#    for y in range(1,n[0]+1):
#    		r1 = [int(x) for x in f.readline().split()]
#    		array1 = [[int(x) for x in f.readline().split()] for line in range(0,4)]
#    		r2 = [int(x) for x in f.readline().split()]
#    		array2 = [[int(x) for x in f.readline().split()] for line in range(0,4)]
#    		a=set(array1[r1[0]-1])
#    		b=set(array2[r2[0]-1])
#    		c=len(set.intersection(a,b))
#    		if c == 0:
#    			out.write('Case #' + str(y) + ': Volunteer cheated!\n')
#    		if c == 1:
#    			out.write('Case #' + str(y) + ': ' + str(set.intersection(a,b).pop()) + '\n')
#    		if c > 1:
#    			out.write('Case #' + str(y) + ': Bad magician!\n')
