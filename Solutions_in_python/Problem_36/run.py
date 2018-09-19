import sys

def printResult( f, tc, res ):
	print 'Case #',tc,':%04d'%res
	if res>10000:
		f.write( 'Case #'+str(tc)+': %04d\n'%(res%10000) ) #last 4 digits
	else:
		f.write( 'Case #'+str(tc)+': %04d\n'%res )
	
if __name__=="__main__":
	if len(sys.argv)>1:
		inp = sys.argv[1]
	else:
		print "append an input file param"
		sys.exit()

	f = open( inp, 'rt' )
	nTC = int( f.readline() )
	print 'the number of tc :', nTC

	output_file = inp.split('.')[0]+"_output.txt"
	fout = open( output_file, 'wt')

	ans = "welcome to code jam"
	
	for testcase in range(0, nTC):
		tc = f.readline().strip()
		print testcase+1, tc
		
		seq = {}
		for ai, a in enumerate(ans):
			for ti, t in enumerate(tc):
				if a==t:
					try:
						seq[ai].append(ti)
					except:
						seq[ai]=[ti]
						
		#sort
		#for s in seq.keys():
		#	seq[s].sort()
			
		#prune
		while 1:
			cnt = 0
			for s in seq.keys():
				if s==0: 
					continue
				#print seq[s-1][-1]
				rm_list = []
				rm_list2 = []
				try:
					for prev in seq[s-1]:
						try:
							if prev > seq[s][-1]: 
								rm_list.append( prev )
						except:
							pass
				except:
					pass
				for cur in seq[s]:
					try:
						if cur < seq[s-1][0]:
							rm_list2.append( cur )
					except:
						pass
						
				for rm in rm_list:
					cnt+=1
					seq[s-1].remove(rm)
				for rm in rm_list2:
					cnt+=1
					seq[s].remove(rm)
			if cnt==0: break
		
		#check if 0?
		nCount = 0
		for s in seq.keys():
			if len(seq[s])<1:
				continue
			else:
				nCount+=1
		if nCount!=len(ans): 
			printResult( fout, testcase+1, 0 )
			continue
		
		#merge
		res = 1.
		#print
		prev_values = {}
		for s in seq.keys():
			#pass the last one
			#if s >= len(seq)-1: continue
			if s==0: #first one
				#multiply.append( len(seq[s]) )
				if len(seq[s])>0:
					#res *= len(seq[s])
					for i in range(0, len(seq[s])):
						prev_values[i]=1
					#print ans[0]+':%d,'%res,
				continue
				
			branch = 0		
			try:
				"""
				for prev in seq[s-1]:
					for cur in seq[s]:
						if prev < cur:
							branch +=1
				if branch>len(seq[s-1]):
					#multiply.append( branch/len(seq[s-1] ))
					res *= float(branch)/float(len(seq[s-1] ))
					print ans[s]+':%d'%branch+'/%d'%len(seq[s-1] )+',',
				"""
				cur_values={}
				for i, prev in enumerate(seq[s-1]):
					for j, cur in enumerate(seq[s]):
						if prev < cur:
							try:
								cur_values[j]+=prev_values[i]
							except:
								cur_values[j]=prev_values[i]
				prev_values = cur_values
				print ans[s]+';',
				for v in prev_values.keys():
					print prev_values[v],
				
				
			except:
				pass
			
		res=0
		for v in prev_values.keys():
			res+=prev_values[v]
		#print multiply	
		printResult( fout, testcase+1, res )
		if testcase+1==71:
			for s in seq.keys():
				print ans[s],':',
				for v in seq[s]:
					print v,
				print 
			
	f.close()
	fout.close()