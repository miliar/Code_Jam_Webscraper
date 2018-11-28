// Sample.cpp : Defines the entry point for the console application.
//
#include <fstream>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <numeric>
#include <cmath>
using namespace std;

struct testcase {
	int n, A, B, C, D, x0, y0, M;
};

fstream f1;

void readTestcase(fstream& fp, testcase& tcase) {
	fp>>tcase.n>>tcase.A>>tcase.B>>tcase.C>>tcase.D>>tcase.x0>>tcase.y0>>tcase.M;
}

vector<testcase> readInput(char *fileName) {
	vector<testcase>testCases;
	fstream fp;
	int nCases = 0;
	fp.open(fileName, ios::in);
	fp>>nCases;

	for (int i=0; i<nCases; i++) {
		testcase newCase;
		readTestcase(fp, newCase);
		testCases.push_back(newCase);
	}
	return testCases;
}

vector<pair<double,double>> generateCoods(testcase& t) {
	vector<pair<double,double>> coods;
	pair<double, double> vert;
	long long int X = t.x0, Y = t.y0;
	vert.first = X;
	vert.second = Y;
	coods.push_back(vert);
	for (int i = 1 ; i<t.n; i++) {
		X = (t.A * X + t.B) % t.M;
		Y = (t.C * Y + t.D) % t.M;
		pair<double, double> vert(X,Y);
		coods.push_back(vert);
	}
	return coods;
}

int processTestCase(testcase& t) {
	vector<pair<double,double>> coods = generateCoods(t);

	int myVerts=0;

	int n = coods.size();
	for(int i=0; i<n; i++)
		for (int j=0; j<n; j++)
			for(int k=0; k<n; k++){
				if (i>=j || j>=k ) continue;
				double x = (coods[i].first + coods[j].first + coods[k].first)/3.0;
				double y = (coods[i].second + coods[j].second + coods[k].second)/3.0;
				long xr = (long)(x+0.5);
				long yr = (long)(y+0.5);

				if (abs(x-xr) < 1E-10&& abs(y-yr) <1E-10) {
					myVerts++;
					//f1<<x<<y<<endl;
				}
			}
		return myVerts;
}

int main(int argc, char* argv[])
{
	vector<testcase> myTestCases = readInput("C:\\A-small.in");
	fstream fout;
	fout.open("c:\\A-small.out", ios::out);
	f1.open("c:\\test.out", ios::out);
	for(unsigned int i=0; i < myTestCases.size();  i++) {		
		int x = processTestCase(myTestCases[i]);
		cout<< "Case #"<<i+1<<": "<< x <<endl;
		fout<< "Case #"<<i+1<<": "<<x <<endl;
	}
	fout.close();
	f1.close();
	return 0;
}
