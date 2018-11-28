// traintimetab.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

  typedef struct {
          int turnaroundTime;
          int numtripsA_B;
          int numtripsB_A;
          vector<int> depart_A,depart_B,arrival_A,arrival_B;
   } testcaseT;

	string itos(int i)	// convert int to string
	{
		stringstream s;
		s << i;
		return s.str();
	}

	int stoi(string str)	// convert int to string
	{
		stringstream s(str);
		int i=0;
		s >> i;
		return i;
	}

int main(int argc, char* argv[])
{
	cout<<"starting train time problem solution"<<endl;
    string inputFilename="e:\\goog\\B-large.in";

	int numTestCases=0;
    ifstream infile;
	infile.open("e:\\goog\\B-large.in", ios::in);
	if (!infile) 
	{     cerr << "Can't open input file " << inputFilename << endl;     
	return 0; 
	}

	infile>>numTestCases;
	if(numTestCases<=0)
	{     cerr << "Can't open input file " << inputFilename << endl;     
	return 0; 
	}

	vector<testcaseT> Testcases;

	for(;numTestCases>0;numTestCases--)
	{
		testcaseT test;
		infile>>test.turnaroundTime;
		//if(turnaroundT==60) turnaroundT=100; // normalise
		infile >> test.numtripsA_B >> test.numtripsB_A;

		// A to B
		for(int ii=0;ii<test.numtripsA_B;ii++)
		{
			string strTimeA , strTimeB;
			infile >>strTimeA >> strTimeB;
			strTimeA.erase(2,1); strTimeB.erase(2,1); // get rid of the ':'
			int numTimeA=0, numTimeB=0;
			numTimeA=stoi(strTimeA); 
			numTimeB=stoi(strTimeB);
			test.depart_A.push_back(numTimeA);


			int hours = (numTimeB/100)*100; // extract the hundredth part
			int balance = numTimeB-hours;
			balance = test.turnaroundTime+balance;
			int balHours = balance/60; balHours=balHours*100; // offset
			int balMins = balance%60;

			numTimeB = hours+balHours+balMins;   // recalculated to adjust to turnaronund time

			test.arrival_B.push_back(numTimeB);
		}

		// B to A
		for(int ii=0;ii<test.numtripsB_A;ii++)
		{
			string strTimeA , strTimeB;
			infile >>strTimeB >> strTimeA;
			strTimeA.erase(2,1); strTimeB.erase(2,1); // get rid of the ':'
		    int numTimeA=0, numTimeB=0;
			numTimeA=stoi(strTimeA); 
			numTimeB=stoi(strTimeB);
			test.depart_B.push_back(numTimeB);
			// we need to massage the numTimeA to account for the turnaround time			
			int hours = (numTimeA/100)*100; // extract the hundredth part
			int balance = numTimeA-hours;
			balance = test.turnaroundTime+balance;
			int balHours = balance/60; balHours=balHours*100; // offset
			int balMins = balance%60;

			numTimeA = hours+balHours+balMins;   // recalculated to adjust to turnaronund time

			test.arrival_A.push_back(numTimeA);
		}
	
		Testcases.push_back(test);
	}

	infile.close();

	// now for each test case get the tables etc

	ofstream outfile;
	outfile.open("e:\\goog\\b-large.out", ios::out);

	for(int jj=0; jj<Testcases.size(); jj++)
	{
		testcaseT test=Testcases[jj];
		string strcasenumber=itos(jj+1);
		string strout="Case #";
		strout+= strcasenumber;
		strout+= ": ";

		int numTrainsReqdA=0;
		sort(test.arrival_A.rbegin(),test.arrival_A.rend());
		for(int kk=0; kk<test.depart_A.size(); kk++)
		{
			bool bfound=false;
			for(int xx=0; xx<test.arrival_A.size(); xx++)
			{
                if(test.arrival_A[xx]==-1) continue; // invalid input
				bfound = ( test.depart_A[kk] - (test.arrival_A[xx]) ) >=0;
				if(bfound) 
				{
					test.arrival_A[xx]=-1;
					break;
				}
			}
			if(!bfound) numTrainsReqdA++;
		}

		/////////////////////

		int numTrainsReqdB=0;
		sort(test.arrival_B.rbegin(),test.arrival_B.rend());

		for(int kk=0; kk<test.depart_B.size(); kk++)
		{
			bool bfound=false;
			for(int xx=0; xx<test.arrival_B.size(); xx++)
			{

                if(test.arrival_B[xx]==-1) continue; // invalid input
				bfound = ( test.depart_B[kk] - (test.arrival_B[xx]) 

					) >=0;
				if(bfound) 
				{
					test.arrival_B[xx]=-1;
					break;
				}
			}
			if(!bfound) numTrainsReqdB++;
		}

		outfile << strout << numTrainsReqdA << " " << numTrainsReqdB<<endl;
	}

	outfile.close();

	return 0;
}
