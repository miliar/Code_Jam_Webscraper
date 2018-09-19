# -*- coding: utf-8 -*-

import sys
import os.path
import os, time, itertools
import math



class Sample:
	def solve(self,a,n,motes):
		motes.sort()
		if a>motes[n-1]:
			return 0
		elif a==1:
			return n
		self.motes=motes
		ans=n
		for i in range(n+1):
			#上位からi件消す
			ope=i
			if i>0:
				self.motes.pop()
			tmp_ans=self.calc(ope,a,0)
			if tmp_ans<ans:
				ans=tmp_ans
		return min(ans,n)
		
	def calc(self,ope_num,sum,target_idx):
		#print "ope_num:",ope_num,"sum:",sum,"target_idx:",target_idx
		while(target_idx<len(self.motes)):
			if self.motes[target_idx]<sum:
				sum+=self.motes[target_idx]
				target_idx+=1
			else:
				break
		if target_idx==len(self.motes):
			return ope_num
		else:
			tmp=sum
			for i in range(30):
				#print "tmp:",tmp
				ope_num+=1
				tmp=tmp*2-1
				if tmp>self.motes[target_idx]:
					break
			sum=tmp+self.motes[target_idx]
			target_idx+=1
			return self.calc(ope_num,sum,target_idx)

def read_nums():
	return map(int, in_fh.readline().split())
def read_str():
	return in_fh.readline().rstrip('\r\n')

def read_testcase():
	#print board
	#print "-----"
	a,n = read_nums()
	motes = read_nums()
	return {'a':a,'n':n,'motes':motes}

def read_testcases(test_num):
	for i in range(test_num):
		case_num=i+1
		print "case:",case_num
		yield read_testcase()

def wrapper_of_solve(q):
	sample=Sample()
	return sample.solve(**q)

if __name__ == '__main__':

	input_name = sys.argv[1]
	root, ext = os.path.splitext(input_name)
	in_fh=open(input_name)

	test_num=int(in_fh.readline())

	output_name = root + ".out"
	out_fhs=[open(output_name,'w')]

	testcases = read_testcases(test_num)

	mul_iter = itertools.imap(wrapper_of_solve, testcases)

	for (i, r) in enumerate(mul_iter, start=1):
	    for f in out_fhs:
	        print >> f, "Case #%d: %s" % (i, str(r))
