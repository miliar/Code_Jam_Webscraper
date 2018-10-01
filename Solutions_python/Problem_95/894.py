import string, sys

global G
G = {}

G['y'] = 'a'
G['e'] = 'o'
G['q'] = 'z'

string = 'ejp mysljylc kd kxveddknmc re jsicpdrysi'
truestring = 'our language is impossible to understand'
for char in range(len(string)):
	G[string[char]] = truestring[char]

string = 'de kr kd eoya kw aej tysr re ujdr lkgc jv'
truestring = 'so it is okay if you want to just give up'
for char in range(len(string)):
	G[string[char]] = truestring[char]

string = 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
truestring = 'there are twenty six factorial possibilities'
for char in range(len(string)):
	G[string[char]] = truestring[char]	


G['z'] = 'q'

#print len(G)

def solver(stra):
	solution = ""
	for i in stra:
		solution += G[i]
	return solution
	
fil = open(sys.argv[1]).readlines()

fout = open('g.txt', 'w')

for i in range(1, len(fil)):
	fout.write("Case #" + str(i) + ": " + solver(fil[i].strip('\n')) + '\n')