import sys

class InputReader:
	def __init__(self,filePath):
		try:
			f = open(filePath)
			contents = f.readlines()
			f.close()
			N = contents.pop(0)
			with open('output.out','w') as fout:
				count = 1
				while len(contents) > 0:
					print '\n**************\n'
					print len(contents)
					[C,F,X] = [float(i) for i in contents.pop(0).split(' ')]
					pr = Problem(C,F,X)
					print pr.toString()
					res = pr.solve()
					fout.write('Case #'+str(count)+': '+str(res)+'\n')
					count += 1

			fout.close()

		except ValueError as e:
			print e
		except IOError as e:
			print e
		except:
			print "Unexpected error:", sys.exc_info()[0]

class Problem:
	def __init__(self,C,F,X):
		self.C = C
		self.F = F
		self.X = X

	def solve(self):
		try:
			i = 0
			found = False
			t1=1E10
			while found == False:
				best = t1
				t1 = self.X/(2+i*self.F)
				for j in range(i):
					t2 = self.C/(2+j*self.F)
					t1 += t2
				i += 1
				if t1 > best:
					found = True
			t = 0
			for c in range(i-1):
				t = self.X/(2+c*self.F)
				for j in range(c):
					t2 = self.C/(2+j*self.F)
					t += t2

			# t2 = (self.X/(2+self.F))+self.C/2
			# t3 = (self.X/(2+2*self.F))+self.C/(2+self.F)+self.C/2
			# t4 = (self.X/(2+3*self.F))+self.C/(2+2*self.F)+self.C/(2+self.F)+self.C/2
			# t5 = (self.X/(2+4*self.F))+self.C/(2+3*self.F)+self.C/(2+2*self.F)+self.C/(2+self.F)+self.C/2
			print t,i
			return t
		except NameError as e:
			print e
		except:
			print "Unexpected error:", sys.exc_info()[0]

	def toString(self):
		print 'C: '+str(self.C)+'\n'+'F: '+str(self.F)+ '\n' + 'X: '+str(self.X)


if __name__ == '__main__':
	#ir = InputReader('sample.in')
	ir = InputReader('/Users/david/Downloads/B-small-attempt0.in')








