#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cassert>
#include <climits>
#include <cfloat>
#include <ctime>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <utility>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <sstream>
#include <iostream>
#include <iomanip>
using namespace std;

typedef long long LL;

bool tab[500][15][128];

int main() {
	int L,D,N;
	cin>>L>>D>>N;
	vector<string> words(D);
	for (int i=0; i<D; ++i) {
		cin>>words[i];
	}
	memset(tab,0,sizeof tab);
	for (int i=0; i<N; ++i) {
		string pat;
		cin>>pat;
		for (int j=0, k=0; j<L; ++j, ++k) {
			if (pat[k]!='(') {
				tab[i][j][pat[k]]=1;
			}
			else {
				while (pat[++k]!=')') {
					tab[i][j][pat[k]]=1;
				}
			}
		}
	}
	vector<int> counts(N);
	for (int i=0; i<D; ++i) {
		for (int j=0; j<N; ++j) {
			++counts[j];
			for (int k=0; k<L; ++k) {
				if (!tab[j][k][words[i][k]]) {
					--counts[j];
					break;
				}
			}
		}
	}
	for (int i=0; i<N; ++i) {
		cout<<"Case #"<<(i+1)<<": "<<counts[i]<<endl;
	}
	return 0;
}
