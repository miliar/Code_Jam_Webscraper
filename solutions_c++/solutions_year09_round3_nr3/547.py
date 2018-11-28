#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <map>
using namespace std;
#define FOR(i,n) for(i=0;i<n;i++)
#define VI vector<int>
#define FORR(i,a,b) for(i=a;i<b;i++)
#define pb(a) push_back(a)
ifstream fin("CCC.in.txt");
ofstream fout("CCC.txt");

int main() {
	int i,j,k,l,n,m,p,r,t;
	fin >> r;
	bool c[1000];
	FORR(t,1,r+1) {
		fin >> m >> n;
		VI a;
		FOR(i, n) {fin >> k;a.pb(k);}
			l = 0;
		p = -1;
		do {
			l=0;
		memset(c,0,sizeof(c));
		FOR(i, a.size()) {
				c[a[i]] = 1;
				k = a[i];
				while(++k <=m && c[k]==0) {l++;};
				
				k = a[i];
				while(--k>=1 && c[k]==0) {l++;};
			}
			if (l < p || p==-1) p = l;
		} while (next_permutation(a.begin(),a.end()));
		fout << "Case #"<<t << ": " << p << endl;
	}
	return 0;
}