#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>
#include <algorithm>
using namespace std;

ifstream fin;
ofstream out;

vector<int> list;
vector<int> dst;

double process(int num) {
	list.clear();
	dst.clear();
	int tmp;
	for(int i = 0; i < num; i++) {
		fin >> tmp;
		list.push_back(tmp);
		dst.push_back(tmp);
	}
	sort(dst.begin(),dst.end());

	double rt = 0.0;

	for(int i = 0; i < num; i++){
		if(list[i] != dst[i]) {
			rt += 1.00;
		}
	}
	return rt;
}




int main(int argc,char** argv) {
	fin.open(argv[1]);
	out.open(argv[2]);

	int cnum = 0;
	fin >> cnum;

	for(int i = 0; i < cnum; i++) {
		int tmp;
		fin >> tmp;
		out << "Case #" << i + 1 << ": " << process(tmp) << endl;
	}


	fin.close();
	out.close();
}
