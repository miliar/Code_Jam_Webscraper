
import sys
import re

inf = open(sys.argv[-1],"r")

(L,D,N) = inf.readline().split()

word_len = int(L)

lang = []
for i in range(int(D)):
	lang.append(inf.readline().strip())

tests = []
for i in range(int(N)):
	tests.append(inf.readline().strip())

def transform_to_regex(word):
	ts = ""
	in_paren = False
	for i in word:
		if i == "(":
			in_paren = True
			ts = ts + "("
			continue
		if i == ")":
			in_paren = False
			if ts.endswith("|"):
				ts = ts[0:-1]
			ts = ts + ")"
			continue
		ts=ts+i
		if in_paren:
			ts = ts +"|"
	return ts

def checkit(i, word, lang):
	# print "checking this word", word, lang
	tmp_regex = transform_to_regex(word)
	
	P = re.compile(tmp_regex)
	counter = 0
	for language_word in lang:
		if P.search(language_word):
			counter = counter + 1

	print "Case #%s: %s" % (i+1,counter)

for (i,v) in enumerate(tests):
	checkit(i,v,lang)

