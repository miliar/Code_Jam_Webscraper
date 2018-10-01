import sys
sys.stdin = open('i.txt')
sys.stdout = open('o.txt','wb')
imap = lambda x: map(int,x.strip().split())

def getinput(callback=lambda x: x):
	return callback(raw_input())
def simulate(caseNumber):	
	def magicicanAnswer(possibility):
		if len(possibility) == 0: return 'Volunteer cheated!'		
		if len(possibility) == 1: return "%i" % possibility[0]
		return 'Bad magician!'
	ans0 = getinput(int) - 1 
	arrange0 = [getinput(imap) for i in xrange(4)][ans0]
	ans1 = getinput(int) - 1
	arrange1 = [getinput(imap) for i in xrange(4)][ans1]
	answer = [e for e in arrange0 if e in arrange1]		
	print 'Case #%i: %s' % (caseNumber+1,magicicanAnswer(answer))
def main():
	
	tc = getinput(int);
	for caseNumber in xrange(tc):
		simulate(caseNumber)
main()