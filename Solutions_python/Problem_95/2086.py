from sys import stdin
import itertools

dic2 = {}
dic = {'z' : 'q','a': 'y', 'c': 'f', 'b': 'n', 'e': 'c', 'd': 'i', 'g': 'l', 'f': 'w', 'i': 'k', 'h': 'b', 'k': 'o', 'j': 'u', 'm': 'x', 'l': 'm', 'o': 'e', 'n': 's', 'p': 'v', 's': 'd', 'r': 'p', 'u': 'j', 't': 'r', 'w': 't', 'v': 'g', 'y': 'a', 'x': 'h'}
for key in dic.keys():
	dic2[dic[key]] = key

indata = stdin.readlines()
bucket = []
for x in range(1, len(indata)):
	string = ""
	for y in range(0, len(indata[x])):
		if(indata[x][y] == " "):
			string += " "
		elif(indata[x][y] == "z"):
			string += "q"
		elif(indata[x][y] == "\n"):
			break
		else:
			string += dic2[indata[x][y]]
	bucket.append(string)

for x in range(0, len(bucket)):
	print "Case #" + str(x+1) + ": " + str(bucket[x])
