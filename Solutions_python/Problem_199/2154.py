#!/usr/bin/env python3
import sys

T = int(sys.stdin.readline())

def main():
	for x in range(1, T+1):
		print("Case #{}: ".format(x), end="")
		global flips, row, i, K
		flips = 0
		string = sys.stdin.readline()
		pieces = string.split(" ")
		row = list(pieces[0]) # use list instead of string so it can be modified
		K = int(pieces[1])
		length = len(row)
		for i in range(0, length-K+1):
			if (row[i] == "-"):
				flip()

		#check
		if ("".join(row[-K:]) == "+"*K): #last K pancakes are +
			print(flips)
		else:
			print("IMPOSSIBLE")

def flip():
    global flips, row, i, K
    flips += 1
    for y in range(i, i+K):
        if (row[y] == "-"):
            row[y] = "+"
        else:
            row[y] = "-"

if __name__ == "__main__":
    main()