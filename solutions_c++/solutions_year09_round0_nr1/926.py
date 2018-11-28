#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

ifstream fin("a.in");
ofstream fout("a.out");

bool a[501][16][27];
int L,D,N;
int ret[501];

int main() {
	fin>>L>>D>>N;
	vector<string> words(D);
	int i,j,k;
	for(i=0;i<D;++i) {
		fin>>words[i];
	}
	for(i=0;i<N;++i) {
		ret[i] = 0;
		for(j=0;j<L;++j) for(k=0;k<26;++k)a[i][j][k]=false;
	}
	for(j=0;j<N;++j) {
		string tmp;
		fin>>tmp;
		i = 0;
		int ind = 0;
		while(i < tmp.size()) {
			if(tmp[i]!='(') {
				a[j][ind++][tmp[i++]-'a'] = true;
			}
			else {
				k = i+1;
				while(k<tmp.size() && tmp[k]!=')') {
					a[j][ind][tmp[k]-'a'] = true;
					++k;
				}
				++ind;
				i = k+1;
			}
		}
	}
	for(i=0;i<D;++i) {
		for(j=0;j<N;++j) {
			bool ok = true;
			for(k=0;k<L;++k) {
				if(a[j][k][words[i][k]-'a']==false){ok=false;break;}
			}
			if(ok){ret[j]++;}
		}
	}
	for(i=0;i<N;++i) {
		fout<<"Case #"<<(i+1)<<": "<<ret[i]<<endl;
	}
	return 0;
}