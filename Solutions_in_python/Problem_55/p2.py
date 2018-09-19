fin = open("C-small.in")
fout = open("output.txt", "w")
num_cases = int(fin.readline())
#print num_cases

for i in range(num_cases):
	[num_run, rc_size, num_ppl] = map(int, fin.readline().replace("\n","").split(" "))
	#print num_run, rc_size, num_ppl
	ppl_queue = map(int, fin.readline().replace("\n","").split(" "))
	#print ppl_queue
	euro=0
	for run in range(num_run):
		filled_queue=0
		for q_index in range(len(ppl_queue)):
			if filled_queue + ppl_queue[q_index] > rc_size:
				break
			else:
				euro = euro + ppl_queue[q_index]
				filled_queue = filled_queue+ppl_queue[q_index]
				q_index = q_index+1
		ppl_queue = ppl_queue[q_index:]+ppl_queue[:q_index]
		#print ppl_queue
	
	fout.write("Case #"+str(i+1)+": "+str(euro)+"\n")

fin.close()
fout.close()

