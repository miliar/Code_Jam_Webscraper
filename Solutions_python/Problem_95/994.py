import sys, string

f = open("A-small-attempt0.in")
n = int(f.readline())
for i in range(n):
	l = f.readline()
	j = l.translate(string.maketrans("abcdefghijklmnopqrstuvwxyz","yhesocvxduiglbkrztnwjpfmaq"))
	print ("Case #" + str(i+1) + ": " + j[:-1])


