# -*- coding: utf8 -*-
import os
import sys

if __name__ == "__main__":
	#input = open("sample.txt", "r")
	input = open("a-small.in", "r")
 	output = open("output-small.txt", "w")
	
	maxUnit = 4;
	
	caseMax = int(input.readline())
	
	for caseCounter in range(caseMax):
		strResult = "";
		incomplete = False;
		rows = [];
		for idx in range(maxUnit):
			row = input.readline();
			rows.append(row);
		
		
		for idx in range(maxUnit):
			#print("# : %d %s " % (idx, str(rows[0])[2]));
			#print("%d#: [%s]" % (idx, rows[idx]));
			shouldBe = 'T';
			continueCounter = 0;
			for loop in range(maxUnit):
				curMarker = rows[loop][idx];
				if "T" != curMarker and "O" != curMarker and "X" != curMarker:
					incomplete = True;
					continue;

				if shouldBe == curMarker or curMarker == "T":
					continueCounter = continueCounter + 1;
					continue;
				elif shouldBe == "T":
					shouldBe = curMarker;
					continueCounter = continueCounter + 1;
					continue;
				else:
					break;

			if maxUnit == continueCounter and shouldBe != "T":
				strResult = "%s won" % shouldBe;
			
			if strResult != "":
				break;
			
			#print("ContinueCounter : %d" % continueCounter);
		
		if strResult == "":
			for idx in range(maxUnit):
				#print("# : %d %s " % (idx, str(rows[0])[2]));
				#print("%d#: [%s]" % (idx, rows[idx]));
				shouldBe = 'T';
				continueCounter = 0;
				for loop in range(maxUnit):
					curMarker = rows[idx][loop];
					if "T" != curMarker and "O" != curMarker and "X" != curMarker:
						incomplete = True;
						continue;
					
					if shouldBe == curMarker or curMarker == "T":
						continueCounter = continueCounter + 1;
						continue;
					elif shouldBe == "T":
						shouldBe = curMarker;
						continueCounter = continueCounter + 1;
						continue;
					else:
						break;
					
				if maxUnit == continueCounter and shouldBe != "T":
					strResult = "%s won" % shouldBe;
				
				if strResult != "":
					break;
				
				#print("ContinueCounter : %d" % continueCounter);
			
		if strResult == "":
			for idx in range(maxUnit):
				#print("# : %d %s " % (idx, str(rows[0])[2]));
				#print("%d#: [%s]" % (idx, rows[idx]));
				shouldBe = 'T';
				continueCounter = 0;
				for loop in range(maxUnit):
					curMarker = rows[loop][loop];
					if "T" != curMarker and "O" != curMarker and "X" != curMarker:
						incomplete = True;
						continue;
					
					if shouldBe == curMarker or curMarker == "T":
						continueCounter = continueCounter + 1;
						continue;
					elif shouldBe == "T":
						shouldBe = curMarker;
						continueCounter = continueCounter + 1;
						continue;
					else:
						break;
					
				if maxUnit == continueCounter and shouldBe != "T":
					strResult = "%s won" % shouldBe;
				
				if strResult != "":
					break;
				
				#print("ContinueCounter : %d" % continueCounter);
			
		if strResult == "":
			for idx in range(maxUnit):
				#print("# : %d %s " % (idx, str(rows[0])[2]));
				#print("%d#: [%s]" % (idx, rows[idx]));
				shouldBe = 'T';
				continueCounter = 0;
				for loop in range(maxUnit):
					curMarker = rows[loop][maxUnit - 1 - loop];
					if "T" != curMarker and "O" != curMarker and "X" != curMarker:
						incomplete = True;
						continue;
					
					if shouldBe == curMarker or curMarker == "T":
						continueCounter = continueCounter + 1;
						continue;
					elif shouldBe == "T":
						shouldBe = curMarker;
						continueCounter = continueCounter + 1;
						continue;
					else:
						break;
					
				if maxUnit == continueCounter and shouldBe != "T":
					strResult = "%s won" % shouldBe;
				
				if strResult != "":
					break;
				
				#print("ContinueCounter : %d" % continueCounter);
			
			
		if "" == strResult:
			if True == incomplete:
				strResult = "Game has not completed";
			else:
				strResult = "Draw";
		
		strCase = "Case #%d: " % (caseCounter + 1);
		  
		print(strCase + strResult);
		output.write(strCase + strResult + "\r\n");
		input.readline();
   
	print("done")
