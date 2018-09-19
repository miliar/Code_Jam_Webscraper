# -*- coding: utf8 -*-
import os
import sys

if __name__ == "__main__":
	#input = open("A-sample.txt", "r")
	input = open("A-small-attempt.in", "r");
	#input = open("A-large.in", "r")
	output = open("A-output-small.txt", "w")
	google_set = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"];
	english_set = ["y", "h", "e", "s", "o", "c", "v", "x", "d", "u", "i", "g", "l", "b", "k", "r", "z", "t", "n", "w", "j", "p", "f", "m", "a", "q"];
	
	caseMax = int(input.readline())
	
	for caseCounter in range(caseMax):
		orgText = input.readline();
		strResult = "";
		for idx in range(len(orgText)):
			ascii = ord(orgText[idx]);
			if(97 <= ascii and 122 >= ascii):
				strResult = strResult + english_set[ascii - 97];
			else:
				strResult = strResult + orgText[idx];
		
		
		strCase = "Case #%d: " % (caseCounter + 1);
		
		print(strCase + strResult);
		output.write(strCase + strResult);
		
	print("done")