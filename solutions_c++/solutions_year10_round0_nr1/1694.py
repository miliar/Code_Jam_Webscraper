#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <fstream>
using namespace std;

ifstream fin("a.in");
ofstream fout("a.out");

typedef long long ll;

int main() {
	int T;
	fin>>T;
	int testNum;
	int n,k;
	for(testNum=1;testNum<=T;++testNum) {
		string ret = "OFF";
		fin>>n>>k;
		if( k % (1<<n) == (1<<n) - 1 )ret = "ON";
		fout<<"Case #"<<testNum<<": "<<ret<<endl;
	}
	return 0;
}
