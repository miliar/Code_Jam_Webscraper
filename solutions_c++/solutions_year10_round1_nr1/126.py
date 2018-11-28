// A.cpp

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

char b[64][64];
int N,K;

char res[][10]={"Neither","Red","Blue","Both"};

void solve(int cas){
	int i,j,k,t;
	scanf("%d %d",&N,&K);
	for (i=0;i<N;i++) scanf("%s",b[i]);
	for (i=0;i<N;i++){
		t = N-1;
		for (j=N-1;j>=0;j--){
			if (b[i][j]!='.'){
				b[i][t]=b[i][j]; t--;
			}
		}
		while (t>=0){
			b[i][t]='.'; t--;
		}
	}
	int ok=0;
	for (i=0;i<N;i++) for (j=0;j<N;j++){
		if (b[i][j]=='.') continue;
		// ->r
		if (j+K<=N){
			for (k=0;k<K;k++){
				if (b[i][j]!=b[i][j+k]) break;
			}
			if (k==K){
				if (b[i][j]=='R') ok|=1;
				if (b[i][j]=='B') ok|=2;
			}
		}
		// ->d
		if (i+K<=N){
			for (k=0;k<K;k++){
				if (b[i][j]!=b[i+k][j]) break;
			}
			if (k==K){
				if (b[i][j]=='R') ok|=1;
				if (b[i][j]=='B') ok|=2;
			}
		}
		// ->dr
		if (i+K<=N && j+K<=N){
			for (k=0;k<K;k++){
				if (b[i][j]!=b[i+k][j+k]) break;
			}
			if (k==K){
				if (b[i][j]=='R') ok|=1;
				if (b[i][j]=='B') ok|=2;
			}
		}
		// ->dl
		if (i+K<=N && j>=K-1){
			for (k=0;k<K;k++){
				if (b[i][j]!=b[i+k][j-k]) break;
			}
			if (k==K){
				if (b[i][j]=='R') ok|=1;
				if (b[i][j]=='B') ok|=2;
			}
		}
	}
	printf("Case #%d: %s\n",cas,res[ok]);
}

int main(){
	int T;
	int c = 0;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	while (T--)
		solve(++c);
	return 0;
}
