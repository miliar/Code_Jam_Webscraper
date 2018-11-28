#include <string>
#include <list>
#include <fstream>
#include <iostream>

#include "stdio.h"
#include <stdlib.h>
#include "math.h"

using namespace std;

double const sqr5 = 5.2360679774997896964091736687313;
string sqr_5 = "5.2360679774997896964091736687313";

string results[32];

void main()
{
	ifstream inFile("c:\\C-small.in");
	ofstream outFile("c:\\out");

	// results by hand from windows calculator

	results[0] = "001";
	results[1] = "005";
	results[2] = "027";
	results[3] = "143";
	results[4] = "751";
	results[5] = "935";
	results[6] = "607";

	results[7] = "903";
	results[8] = "991";
	results[9] = "335";
	results[10] = "047";
	results[11] = "943";

	results[12] = "471";
	results[13] = "055";
	results[14] = "447";
	results[15] = "463";

	results[16] = "991";
	results[17] = "095";
	results[18] = "607";
	results[19] = "263";
	results[20] = "151";
	results[21] = "855";

	results[22] = "527";
	results[23] = "743";
	results[24] = "351";
	results[25] = "135";
	results[26] = "407";

	results[27] = "903";
	results[28] = "791";
	results[29] = "135";
	results[30] = "647";


	int numberOfCases = 0;	
	int n;

	inFile >> numberOfCases ;

	for(int caseNumber = 1; caseNumber <= numberOfCases ; caseNumber++)
	{
		inFile >> n ;
		
		outFile << "Case #" << caseNumber << ":" << " " << results[n] << endl;
	}
}