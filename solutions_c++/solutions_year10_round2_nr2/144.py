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
using namespace std;

ifstream fin("b.in");
ofstream fout("b.out");

typedef long long ll;

ll x[100];
ll v[100];

int main() {
	int tests;
	fin>>tests;
	int testNum;
	int n,k;
	ll B,T;
	int i;
	for(testNum=1;testNum<=tests;++testNum) {
		fin>>n>>k>>B>>T;
		for(i=0;i<n;++i)fin>>x[i];
		for(i=0;i<n;++i)fin>>v[i];
		int ret = 0;
		int failed = 0;
		int done=0;
		for(i=n-1;i>=0;--i) {
			if(done>=k)break;
			if(x[i]+T*v[i]>=B) {
				ret += failed;
				++done;
			}
			else {
				++failed;
			}
		}
		if(done>=k) {
			fout<<"Case #"<<testNum<<": "<<ret<<endl;
		}
		else {
			fout<<"Case #"<<testNum<<": IMPOSSIBLE"<<endl;
		}
	}
	return 0;
}
