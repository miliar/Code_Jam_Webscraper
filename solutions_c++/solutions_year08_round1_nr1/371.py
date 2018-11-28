#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	ifstream ifs=ifstream("in1.txt");
	ofstream ofs=ofstream("out1.txt");
	int T;

	ifs>>T;

	for (int i=0; i<T; i++) {
		int n;
		ofs<< "Case #" << i+1 << ": ";
		ifs>> n;
		vector<long long> v1, v2;
		for (int j=0; j<n; j++) {
			int temp;
			ifs>> temp;
			v1.push_back(temp);
		}
		for (int j=0; j<n; j++) {
			int temp;
			ifs>> temp;
			v2.push_back(temp);
		}
		sort(v1.begin(), v1.end());
		sort(v2.begin(), v2.end());
		long long sp=0;
		for (int j=0; j<n; j++)
			sp+=v1[j]*v2[n-j-1];
		ofs<< sp <<endl;
	}

	ifs.close();
	ofs.close();
	return 0;
}