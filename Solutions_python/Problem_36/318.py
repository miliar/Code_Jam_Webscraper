#!/usr/bin/python

filename = "C-small-attempt0"
input_filename = filename + ".in"
output_filename = filename + ".out"
message = "welcome to code jam"

def find(str):
	pass

def work(str, msg):
	count = 0
	l = len(str)
	if len(msg) == 1:
		for i in range(l):
			if str[i] == msg[0]:
				count += 1
				count %= 10000
		return count

	for i in range(l-len(msg)):
		if str[i] == msg[0]:
			count += work(str[i+1:],msg[1:])
			count %= 10000
	return count

def main():
	fi = open(input_filename,"r")
	fo = open(output_filename,"w")
	N = int(fi.readline())
	for i in range(N):
		input = fi.readline()
		input.replace('\n','')
		count = work(input, message)
		fo.write("Case #" + str(i+1) + ": " + str(count).rjust(4).replace(' ','0') + "\n");

if __name__ == "__main__":
	main()
