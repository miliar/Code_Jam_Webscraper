class robot:
	def __init__(self,name,seq):
		self.glob_seq = seq
		self.name = name
		self.seq = self.create_sequence(name,seq)
		if self.name == seq[0][0]:
			self.can_push = 1
		else:
			self.can_push = 0
		self.pos = 1
		self.cur = 0
		if len(self.seq)>0:
			self.next = self.seq[0]
		else:
			self.next = self.pos
		
	def create_sequence(self,name,seq):
		ret = []
		for s in seq:
			if s[0] == name:
				ret.append(int(s[1]))
		return ret

global_walk = 1
N = 0
		
def next_second(o,b,global_walk,seq,N):
	if global_walk >= N:
		return 0
	
	print "-"*5
	
	'''
	print "global_walk is",global_walk
	print "o.pos =",o.pos
	print "o.cur =",o.cur
	print "o.next =",o.next
	print "b.pos =",b.pos
	print "b.cur =",b.cur
	print "b.next =",b.next
	'''
	
	if o.pos < o.next:
		o.pos += 1
		print "o moved +"
	elif o.pos > o.next:
		o.pos -= 1
		print "o moved -"
	elif not o.can_push:
		print "o stayed"
		pass
	else:
		o.cur +=1
		if o.cur < len(o.seq):
			o.next = o.seq[o.cur]
		else:
			pass
		global_walk +=1
		print "o pushed button"
	
	if b.pos < b.next:
		b.pos += 1
		print "b moved +"
	elif b.pos > b.next:
		b.pos -= 1
		print "b moved -"
	elif not b.can_push:
		print "b stayed"
		pass
	else:
		b.cur +=1
		if b.cur < len(b.seq):
			b.next = b.seq[b.cur]
		else: 
			pass
		global_walk +=1
		print "b pushed button"
		
	if global_walk < len(seq):
		#print "seq[",global_walk,"][0]=",seq[global_walk][0]
		if seq[global_walk][0] == 'O':
			o.can_push = 1
			b.can_push = 0
		else:
			o.can_push = 0
			b.can_push = 1
	
	return next_second(o,b,global_walk,seq,N)+1
		
def runs():	
	import sys
	sys.setrecursionlimit(1500)
	#filename = "A_input_small.txt"
	filename = "A-small-attempt1.in"
	#outfile = "A_output.txt"
	outfile = "A-small-attempt1.out"
	global_walk = 1
	N = 0
	f = open(filename,'r')
	g = open(outfile,'w')
	T = f.readline()
	print "T is: ",int(T),"\n"
	test = {}
	
	for i in range(1,int(T)+1):
	#for i in range(1,9):
		test[i] = f.readline()
		test[i] = test[i][0:-1]
		
		#N = test[i][0]
		seq = []
		global_walk = 0
		
		splits = test[i].split(" ")
		print splits
		N = splits[0]
		print "Line ",i,":'"+N+"'"
		
		for j in range(1,2*int(N)+1):
			if(j % 2 == 1):
				tuple = (splits[j],splits[j+1])
				seq.append(tuple)
		
		print seq
		
		o = robot('O',seq)
		b = robot('B',seq)
		#print o.seq
		#print b.seq
		
		c = next_second(o,b,global_walk,seq,int(N))
		if i <=  int(T):
			g.write("Case #"+str(i)+": "+str(c)+"\n")
		else :
			g.write("Case #"+str(i)+": "+str(c))
	
	




