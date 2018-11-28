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

typedef long long ll;

ifstream fin("c.in");
ofstream fout("c.out");

int times;
ll k;
int n;
ll a[5000];
ll sum[5000];

ll num(int i, int p) {
	if(i==0) {
		return sum[p-1];
	}
	else {
		int maxx = min(p,n-i);
		ll ret = sum[i+maxx-1]-sum[i-1];
		if(p>maxx) ret += num(0,p-maxx);
		return ret;
	}
}

int main() {
	int T;
	fin>>T;
	int testnum;
	int i;
	for(testnum = 1; testnum<=T; ++testnum) {
		fin>>times>>k>>n;
		for(i=0;i<n;++i) {
			fin>>a[i];
			if(i==0)sum[i] = a[i];
			else sum[i] = a[i] + sum[i-1];
		}
		int curr = 0;
		ll ret = 0,tmp;
		int L,R,Q;
		while(times--) {
			L = 1;R = n+1;
			while(R-L>1) {
				Q = (L+R)/2;
				tmp = num(curr,Q);
				if(tmp<=k) {
					L = Q;
				}
				else {
					R = Q;
				}
			}
			ret += num(curr,L);
			//cout<<curr<<" "<<L<<endl;
			//cin.ignore();
			curr += L;
			curr %= n;
		}
		fout<<"Case #"<<testnum<<": "<<ret<<endl;
	}
	return 0;
}
