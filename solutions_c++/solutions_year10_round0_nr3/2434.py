#include<iostream>
#include<string>
#include<sstream>
#include<fstream>
#include<vector>
#include<math.h>

using namespace std;

int main()
{
	ifstream infile("C.in");

	if (!infile) {
		cerr << "error: unable to open input file: "
			<< infile << endl;
		return -1;
	}

	string line("");
	size_t T(0);

	getline(infile, line);
	
	stringstream ssTrans;
	ssTrans << line;
	ssTrans >> T;
	ssTrans.clear();
	
	size_t stR[50], stk[50], stN[50], stg[50][1000];
	for (size_t i = 0; i < 50; ++i)  {
		stR[i] = 0;
		stk[i] = 0;
		stN[i] = 0;
		for (size_t j = 0; j < 1000; ++j)  
			stg[i][j] = 0;
	}

	string sTrans("");
	size_t stTrans(0);

	for (size_t i = 0; i < T; ++i)  {

		infile >> sTrans;
		ssTrans << sTrans;
		ssTrans >> stTrans;
		stR[i] = stTrans;
		ssTrans.clear();
		stTrans = 0;

		infile >> sTrans;
		ssTrans << sTrans;
		ssTrans >> stTrans;
		stk[i] = stTrans;
		ssTrans.clear();
		stTrans = 0;

		infile >> sTrans;
		ssTrans << sTrans;
		ssTrans >> stTrans;
		stN[i] = stTrans;
		ssTrans.clear();
		stTrans = 0;

		for (size_t j = 0; j < stN[i]; ++j)  {
			infile >> sTrans;
			ssTrans << sTrans;
			ssTrans >> stTrans;
			stg[i][j] = stTrans;
			ssTrans.clear();
			stTrans = 0;
		}
	}

	infile.close();

////////////////////////////////

	size_t stInGroupNum(0), stTotalEarning[50];
	for (size_t i = 0; i < 50; ++i)
		stTotalEarning[i] = 0;


	for (size_t i = 0; i < T; ++i)  {

		size_t stNext(0), stLeftSeats(0);
		bool bGroupIsIn[1000];
		for (size_t j = 0; j < 1000; ++j)
			bGroupIsIn[j] = false;


		for (size_t j = 0; j < stR[i]; ++j)  {

			stLeftSeats = stk[i];
			for (size_t j = 0; j < stN[i]; ++j)
				bGroupIsIn[j] = false;

			while(stLeftSeats >= stg[i][stNext] && bGroupIsIn[stNext] == false)  {

				stLeftSeats -= stg[i][stNext];
				bGroupIsIn[stNext] = true;
				stTotalEarning[i] += stg[i][stNext];

				cout << stg[i][stNext] << " ";

				stNext++;
				stNext = stNext % stN[i];
			}
			cout << endl;
		}
	}




////////////////////////////////

	cout << T << endl << endl;

	ofstream outfile("C.out", ofstream::trunc);
	if (!outfile) {
		cerr << "error: unable to open input file: "
			<< outfile << endl;
		return -1;
	}

	for (size_t i = 0; i < T; ++i)  {

		cout << stR[i] << "," << stk[i] << "," << stN[i] << endl;

		size_t j(0);

		for (j = 0; j < stN[i] - 1; ++j)  {

			cout << stg[i][j] << ","; 
		}

		cout << endl << "Earing in this time: " << stTotalEarning[i] << endl;

		outfile << "Case #"<< i + 1 << ": " << stTotalEarning[i] << endl;

		cout << stg[i][j] << endl << endl;
	}

	outfile.close();

	return 0;
}
