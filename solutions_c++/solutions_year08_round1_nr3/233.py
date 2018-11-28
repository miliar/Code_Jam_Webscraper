#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	ifstream ifs=ifstream("in3.txt");
	ofstream ofs=ofstream("out3.txt");
	vector<string> vs;
	vs.push_back("000");
	vs.push_back("000");
	vs.push_back("027");
	vs.push_back("143");
	vs.push_back("751");
	vs.push_back("935");
	vs.push_back("607");
	vs.push_back("903");
	vs.push_back("991");
	vs.push_back("335");
	vs.push_back("047");
	vs.push_back("943");
	vs.push_back("471");
	vs.push_back("055");
	vs.push_back("447");
	vs.push_back("463");
	vs.push_back("991");
	vs.push_back("095");
	vs.push_back("607");
	vs.push_back("263");
	vs.push_back("151");
	vs.push_back("855");
	vs.push_back("527");
	vs.push_back("743");
	vs.push_back("351");
	vs.push_back("135");
	vs.push_back("407");
	vs.push_back("903");
	vs.push_back("791");
	vs.push_back("135");
	vs.push_back("647");

	int T,n;

	ifs>>T;

	for (int i=0; i<T; i++) {
		ofs<< "Case #" << i+1 << ": ";
		ifs>> n;
		ofs<< vs[n] <<endl;
	}

	ifs.close();
	ofs.close();
	return 0;
}