import sys

#reads input from stdin, example usage:
#cat input.txt | speakingintounges.py > output.txt

#creates a dictionary using character mapping by taking a string and its translated version.
#takes an optional existing dictionary to add to.
#may be a bit redundant but python's dict should sort it out.
def makeDict(G, S, d = dict()):
	if len(G) != len(S):
		print "strings are different length"
		return
	for i in range(len(G)):
		if G[i] != ' ':
			d[G[i]] = S[i];
	return d;

#translates a given string G using dictionary d.
#fills unknown characters with spaces.
def translate(G, d):
    S = "";
    for c in G:
        if c in d:
            S = S + d[c];
        else:
            S = S + ' ';
    return S;


#prepare dictionary by using hard coded hints from sample test case:

D = makeDict("y qeez", "a zooq"); #z->q mapping added by manual inspection of resulting dictionary.
D = makeDict("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand", D);
D = makeDict("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities", D);
D = makeDict("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up", D);

#parse input
inputlines = sys.stdin.readlines();
T = int(inputlines[0])

for i in range(1, T+1):
    print "Case #%d: %s" % (i, translate(inputlines[i], D));


