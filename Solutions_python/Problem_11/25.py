
import sys, os
import math as m

try:
	import psyco
	psyco.full()
except:
	pass

if len(sys.argv)>1:
  fi=open(sys.argv[1])
else:
  fi=sys.stdin

ncases=int(fi.readline())

def addsigns(s,n):
	r=0
	nu=[0,1]
	sum=[]
	for p in range(len(s)-1):
		if n%3==0:
			nu[-1]+=1
		elif n%3==1:
			sum.append(True)
			nu.append(nu[-1]+1)
		elif n%3==2:
			sum.append(False)
			nu.append(nu[-1]+1)
		n/=3
			
	r=int(s[nu[0]:nu[1]])
	for p in range(len(sum)):
		if sum[p]:
			r+=int(s[nu[p+1]:nu[p+2]])
		else:
			r-=int(s[nu[p+1]:nu[p+2]])
	return r

#def addsigns(s,n):
	#r=0
	#sub=int(s[0])
	#subs=False
	#for l in s[1:]:
		#if n%3==0:
			#sub*=10
		#else:
			#if subs: r-=sub
			#else: r+=sub
			#subs=n%3==1
			#sub=0
		#sub+=int(l)
		#n/=3
	#return r+sub

#def addsigns(s,n):
	#r=s[0]
	#a='','.0+','.0-'
	#for l in s[1:]:
		#r+=a[n%3]+l
		#n/=3
	#return r+'.0'
	
#def addsigns(s,n):
	#r='int("'+s[0]
	#a='','")+int("','")-int("'
	#for l in s[1:]:
		#r+=a[n%3]+l
		#n/=3
	#return int(eval(r+'")'))
	
#for case in xrange(ncases):
	s=fi.readline().strip('\n')
	u=0
	for i in xrange(3**(len(s)-1)):
		#n=abs(int(eval(addsigns(s,i))))
		n=abs(addsigns(s,i))
		if not (n%2 and n%3 and n%5 and n%7):
			u+=1
	
	print "Case #%i:"%(case+1),u
	
