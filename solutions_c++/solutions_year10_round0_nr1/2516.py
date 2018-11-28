#include<iostream>
#include<string>
#include<sstream>
#include<fstream>
#include<vector>
#include<math.h>

using namespace std;

int main()
{
	ifstream infile("A.in");

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

	vector<size_t> Ks, Ns;
	string sK(""), sN("");
	size_t uiTrans(0);

	while (infile.good())  {

		infile >> sN;
		ssTrans << sN;
		ssTrans >> uiTrans;
		Ns.push_back(uiTrans);
		ssTrans.clear();
		uiTrans = 0;

		infile >> sK;
		ssTrans << sK;
		ssTrans >> uiTrans;
		Ks.push_back(uiTrans);
		ssTrans.clear();
		uiTrans = 0;
	}

	infile.close();

	//cout << T << endl;

	ofstream outfile("A.out", ofstream::trunc);
	if (!outfile) {
		cerr << "error: unable to open input file: "
			<< outfile << endl;
		return -1;
	}

	for (size_t n = 0; n < T; ++n) {
		size_t OnNum(size_t(pow(float(2), int(Ns[n]))));
		//cout << Ns[n] << "," << Ks[n] << endl;
		//cout << OnNum << endl;

		//cout << endl;

		//cout << "Case #" << n+1 << ": ";
		outfile << "Case #" << n+1 << ": ";

		if ((Ks[n] + 1) % (OnNum) == 0)  {
			//cout << "ON";
			outfile << "ON";
		}
		else  {
			//cout << "OFF";
			outfile << "OFF";
		}

		//cout << endl;
		outfile << endl;
	}

	outfile.close();

	return 0;
}
