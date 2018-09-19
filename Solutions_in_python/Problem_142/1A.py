from collections import OrderedDict

def unique_list(l):
	ulist = []
	ulist.append(l[0]) 
	for ix in xrange(len(l)):
		if	l[ix] != ulist[-1]:
			ulist.append(l[ix]) 
	return ulist
	
ntest = int(raw_input())
for itc in xrange(ntest):
	print 'Case #%d:' % (itc+1),
	nwords = int(raw_input())
	words = [] 
	short_words = [] 
	for iword in xrange(nwords):
		word = raw_input()
		words.append(word)
		short_words.append("".join(unique_list(word)))
	
	numbers_words = [] 
	if (all(short_words[0] == item for item in short_words)):
		for iword in xrange(nwords):
			count = 1
			char = words[iword][0]
			numbers_words.append([])
			for ichar in xrange(len(words[iword])-1):
				newChar = words[iword][ichar + 1]
				if (char == newChar):
					count += 1
				else:
					char = newChar
					numbers_words[iword].append(count)
					count = 1
			numbers_words[iword].append(count)
		
		charnumber = len(numbers_words[0])

		moves = 0

		for nchar in xrange (charnumber):
			sum = 0
			for nvalue in xrange (len(numbers_words)):
				sum += numbers_words[nvalue][nchar]
		 	average = int(round(float(sum)/len(numbers_words)))
			for nvalue in xrange (len(numbers_words)):
				moves += abs(numbers_words[nvalue][nchar] - average)
		print moves
	else:
		print "Fegla Won"
	

