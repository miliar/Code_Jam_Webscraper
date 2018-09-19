

			README
			------
			

This is built using Python. Version details below:

Python 2.6.5 (r265:79359, Mar 24 2010, 01:32:55) 
[GCC 4.0.1 (Apple Inc. build 5493)] on darwin



Input and output files must be formatted correctly and present in designated path.


Source Files:
There are two python modules:
	1. myFileIO.py
		This file contains routines to read from and write to file.
		
	2. snapperchain.py
		This files contains solution to the actual problem.
		
Notes on Solution:
	After solving on paper for N lamps where N = 1, 2, 3 ,4, it was clear that snaps done K times 
	followed the pattern of a boolean chart.
	e.g. for N = 4, light will be on when states are ON,ON,ON,ON, equivalent to 2^4-1 = 31 snaps.
	Similar logic was extended to general N.

		
Submitted on: May 8, 2010
