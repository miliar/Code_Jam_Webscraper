'''open file. 
read one first line, which is n
for i in the range of 0 to n, 
	read line, value is s
	for j in range of 0 to s, 
		read lines, put value in array of search engine names
	read line, value in q
	for j in range of 0 to q, 
		read lines, put value in array of queries
	while whole array of queries not traversed, 
		while (first instance of all search engines not found) and (not end of query array)
			traverse.
		x=max_first_instance
		count++
		reset first_instance_array
	output count to file
'''
f_in=open('a.in')
f_out=open('outputfile.out','w')
n=eval(f_in.readline())
count=0
for i in range(0,n):
	se_names=[]
	se_queries=[]
	se_first=[]
	count=-1
	s=eval(f_in.readline())
	for j in range(0,s):
		words=f_in.readline()
		words=''.join(words.split('\n'))
		se_first=se_first+[999]
		se_names=se_names+[words]
	q=eval(f_in.readline())
	if q==0:
		count=0
	for j in range(0,q):
		words=f_in.readline()
		words=words.split('\n')
		words=''.join(words)
		se_queries=se_queries+[words] #contains the queries
	start=0
	print se_names
	print se_queries
	while len(se_queries) > 0:
		start=0
		for j in range(0,s): #get first instance of each
			try:
				se_first[j]=se_queries.index(se_names[j])
			except ValueError:
				se_first[j]=999
		#print se_names
		#print se_first	
		start=max(se_first) #take term which is not used for the longest time
		se_queries=se_queries[start:]
		start=0
		#print se_names[se_first.index(start)]
		#print start
		count=count+1
		for j in range(0,s): #reset values
			se_first[j]=999
	f_out.write("Case #%d: %d\n" % (i+1,count))
	print count
	#print "**********************"
f_in.close()
f_out.close()


			
