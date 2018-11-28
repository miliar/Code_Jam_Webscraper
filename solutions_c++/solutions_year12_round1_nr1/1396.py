#include "Handler.h"
#include <sstream>

using namespace std;

struct probA
{
	probA() {};
	~probA() {};
	
	int solve()
	{
		Handler myFiles;
		string lineIn;
		int numCases = 0;
		
		myFiles.openIn("probAIn.txt");
		myFiles.openOut("probAOut.txt");
		
		
		myFiles.fileIn >> numCases;
		
		int iCharTyped, iLength;
		//int iCharLeft;
		double iCharLeft;
		vector<double> prob;
		vector<double> expVal;
		double dExpected, dBest;
		
		double dVal;
		
		for(int i=0; i<numCases; i++)
		{
			myFiles.debugOut << "case " << (i+1) << "\r\n";
			iCharTyped = iLength = 0;
			dVal = 0.0;
			dExpected = 1.0;
			iCharLeft = 0.0;
			prob.clear();
			expVal.clear();
			
			myFiles.fileIn >> iCharTyped;
			myFiles.fileIn >> iLength;
			
			dBest = iLength * 2.0;
			
			for(int j=0; j<iCharTyped; j++)
			{
				myFiles.fileIn >> dVal;
				//prob.push_back(dVal);
				dExpected = dExpected * (dVal);
				prob.push_back(dExpected);
			}
			
			iCharLeft =(double)(iLength - iCharTyped);
			
			myFiles.debugOut << "iCharTyped: " << iCharTyped; // << "\r\n";
			myFiles.debugOut << "  iLength: " << iLength << "\r\n";
			
			dVal = 0.0;
			// forge ahead
			dVal = (dExpected * (iCharLeft + 1.0));
			dVal = dVal + ((1.0 - dExpected) * ((double)(iCharLeft + (double)iLength) + 2.0));
			//dVal = dVal + 2.0;
			expVal.push_back(dVal);
			if(dBest > dVal)
				dBest = dVal;
			
			// start over
			dVal = (double)iLength + 2.0;
			expVal.push_back(dVal);
			
			if(dBest > dVal)
				dBest = dVal;
			
			for(int j=0; j<iCharTyped; j++)
			{
				dExpected = prob.at(iCharTyped - j - 1);
				myFiles.debugOut << "dExpected: " << dExpected << "; ";
				//iCharLeft = iLength - (iCharTyped + j);
				
				dVal = (dExpected * (iCharLeft + (double)(2*j) + 1.0));
				dVal = dVal + ((1.0 - dExpected) * ((double)(2*j) + iCharLeft + (double)iLength + 2.0));
				//dVal = dVal + 2.0;// + j;
				expVal.push_back(dVal);
				if(dBest > dVal)
					dBest = dVal;
			}
			char buff[1024];
			sprintf(buff, "%.6f", dBest);
			std::string myStr(buff);
			
			myFiles.debugOut << "\r\nCase #" << (i + 1) << ": ";
			myFiles.debugOut << myStr;
			myFiles.debugOut << "\r\n";
			
			myFiles.fileOut << "Case #" << (i + 1) << ": ";
			myFiles.fileOut << myStr;
			myFiles.fileOut << "\r\n";
			
			myFiles.debugOut << "\r\n";
		}
		
		myFiles.fileOut << "\r\n";
		
		myFiles.close();
		
		return 0;
	};
	

};
