class Input:
	def str(self):
		return raw_input()
	def int(self):
		return int(self.str())
	def strList(self):
		return self.str().split()
	def intList(self):
		return [int(i) for i in self.strList()]
	def _anyLines(self,count,call):
		r=[]
		for i in range(count):
			r.append(call())
		return r
	def strLines(self,count):
		return self._anyLines(count,self.str)
	def intLines(self,count):
		return self._anyLines(count,self.int)
	
get=Input()

def result(iCase,result):
	case="Case #"+str(iCase+1)+":"
	if type(result) == list:
		print case," ".join(list)
	else:
		print case, result

