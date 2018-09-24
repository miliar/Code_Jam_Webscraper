def OptFor(engines,queries):
	"Just the greedy algorithm (which is optimal)"
	max_seq=len(engines)
	optval=0
	seen_so_far=0
	for q in queries:
		print q+','+repr(seen_so_far)
		if engines[q]==0:
			seen_so_far+=1
			engines[q]=1
			if seen_so_far==max_seq:
				print 'switching...'
				optval+=1
				engines=dict([(x,0) for x in engines.keys()])
				engines[q]=1
				seen_so_far=1
	return optval			

f=open('/home/anat/code/inputfile', 'r')
fout=open('/home/anat/code/outputfile','w')
N=int(f.readline())
print N
for i in xrange(1,N+1):
	num_engines=int(f.readline())
	engines={}
	# Scan engine names
	for j in xrange(1,num_engines+1):
		name=f.readline()
		# just in case...
		name=(name.split('\n'))[0]
		engines[name]=0
	# Scan query sequence
	num_queries=int(f.readline())
	queries=[]
	for j in xrange(1,num_queries+1):
		query=f.readline()
		query=query.split('\n')[0]
		queries.append(query)	
	result = OptFor(engines,queries)	
	fout.write('Case #'+repr(i)+': '+repr(result)+'\n')
f.close()
fout.close()
