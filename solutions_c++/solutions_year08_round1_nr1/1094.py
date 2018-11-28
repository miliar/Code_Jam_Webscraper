#include <stdio.h>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
#include <fstream>
using namespace std;

int main(int argc, char* argv[])
{
	  if (argc < 2) {cout<<"Usage: <task name> <input file>"<<endl; return -1;}

	char buf[2048];
	memset(buf, 0, sizeof(buf));

	vector<int> v1,v2,vr;

	 ifstream inFile;
  inFile.open(argv[1]);
  if (!inFile) {
    cerr << "Unable to open file datafile.txt";
    return 1;   // call system to stop
  }

	int num_of_test = 0;
	inFile>>num_of_test;
	for (int i=0; i<num_of_test; ++i) {
		int v=0;
		inFile>>v;
		int temp=0;
		for (int j=0; j<v; ++j) {
			inFile>>temp;
			v1.push_back(temp);
		}
		for (int j=0; j<v; ++j) {
			inFile>>temp;
			v2.push_back(temp);
		}
		sort(v1.begin(), v1.end());
		sort(v2.begin(), v2.end());
		int p = 0;
		vector<int>::const_iterator ci=v1.begin(); //ci!=v1.end(); ++ci)
                vector<int>::const_reverse_iterator cri=v2.rbegin(); //cri!=v2.rend(); ++cri)
		for (int s=0; s<v; ++s){
                
			p += (*ci) * (*cri);		
			++ci;
			++cri;
		}
		vr.push_back(p);
                v1.clear();
                v2.clear();
                
	}
        ofstream outfile ("output.dat");
	int i=1;
	for (vector<int>::const_iterator ci=vr.begin();ci!=vr.end();++ci, ++i)
          outfile<<"Case #"<<i<<": "<<*ci<<endl;

	return 0;
}

