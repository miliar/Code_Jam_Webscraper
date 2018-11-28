#include <list>
#include <deque>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <utility>
#include <string>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <sstream>

using namespace std;

typedef unsigned long long int u64;
typedef long long int i64;


int plac[510][510];

bool cmass(int r,int c,int K,int D) {
	u64 cx=0,cy=0,mt=0;
	for(int i=r;i<r+K;i++) {
		for(int j=c;j<c+K;j++) {
			if(i==r && j==c)
				continue;
			if(i==r && j==c+K-1)
				continue;
			if(i==r+K-1 && j==c)
				continue;
			if(i==r+K-1 && j==c+K-1)
				continue;
			cx+=j*(D+plac[i][j]);
			cy+=i*(D+plac[i][j]);
			mt+=D+plac[i][j];
		}
	}

	if(cx==mt*((2*c+K-1)/2.0) && cy==mt*((2*r+K-1)/2.0))
		return true;
	else
		return false;
}

int main() {
	int NC;

	cin >> NC;
	
	for(int cs=1;cs<=NC;cs++) {
		int R,C,D;
		cin >> R >> C >> D;
		for(int i=0;i<R;i++) {
			for(int j=0;j<C;j++) {
				char aux;
				cin >> aux;
				plac[i][j]=aux-'0';
				}
		}
		int K;
		for(K=min(R,C);K>=3;K--) {
			for(int i=0;i<=R-K;i++) {
				for(int j=0;j<=C-K;j++) {
					if(cmass(i,j,K,D))
						goto ans;
				}
			}
		}
		
		
		ans:
		if(K==2)
			cout << "Case #" << cs << ": " << "IMPOSSIBLE" << endl;
		else 
			cout << "Case #" << cs << ": " << K   << endl;
	}
	
	return 0;
}
