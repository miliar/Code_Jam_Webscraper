#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>
#include <ctime>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <map>
#include <set>
#include <queue>
using namespace std;

ifstream fin("a.in");
ofstream fout("a.out");

int main() {
	int T,t;
	fin>>T;
	int n;
	int i,j,last;
	string str;
	vector<int> vec;
	int ret;
	for(t=1;t<=T;++t) {
		fin>>n;
		vec.resize(n);
		ret = 0;
		for(i=0;i<n;++i) {
			fin>>str;
			last = -1;
			for(j=0;j<n;++j) {
				if(str[j]=='1')last=j;
			}
			vec[i] = last;
		}
		for(i=0;i<n;++i) {
			for(j=i;j<n;++j) if(vec[j]<=i) {
				break;
			}
			while(j>i) {
				++ret;
				swap(vec[j],vec[j-1]);
				--j;
			}
		}
		fout<<"Case #"<<t<<": "<<ret<<endl;
	}
	return 0;
}
