#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<string>
#include<algorithm>
#include<fstream>
#include<sstream>
#include<set>
#include<map>
#include<vector>
#include<queue>
#include<deque>
#include<complex>
#include<numeric>
using namespace std;

const int MaxN = 200;

char A[MaxN][MaxN],B[MaxN][MaxN];

int N, K, no;

int calc(char c) {
	for(int i=0;i<N;++i) {
		for(int j=0;j<N;++j)
			if(B[i][j] == c) {
				if(i+1>=K) {
					bool flag=true;
					for(int k=0;k<K;++k)
						if(B[i-k][j]!=c) {
							flag=false;
							break;
						}
					if(flag)return true;
				}
				if(j+1>=K) {
					bool flag=true;
					for(int k=0;k<K;++k)
						if(B[i][j-k]!=c) {
							flag=false;
							break;
						}
					if(flag)return true;
				}
				if(j+1>=K && i+1>=K) {
					bool flag=true;
					for(int k=0;k<K;++k)
						if(B[i-k][j-k]!=c) {
							flag=false;
							break;
						}
					if(flag)return true;
				}
				if(j+1>=K && i+K<=N) {
					bool flag=true;
					for(int k=0;k<K;++k)
						if(B[i+k][j-k]!=c) {
							flag=false;
							break;
						}
					if(flag)return true;
				}
			}
	}
	return false;
}

int run() {
	scanf("%d %d", &N, &K);
	for(int i=0;i<N;++i){
		scanf("%s",A[i]);
		for(int j=0;j<N;++j)
			B[j][N-1-i] = A[i][j];
	}
	for(int j=0;j<N;++j) {
		for(int i=N-1;i>=0;--i) {
			if(B[i][j] == '.') {
				int k = i;
				for(;k>=0;--k) if(B[k][j] != '.') break;
				swap(B[i][j],B[k][j]);
			}
		}
	}
	bool resA=calc('R'),resB=calc('B');
	printf("Case #%d: ",no);
	if(!resA&&!resB) printf("Neither");
	else
	if(resA&&resB) printf("Both");
	else
	if(resA) printf("Red");
	else
	printf("Blue");
	printf("\n");
}

int main() {
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	
	int test;
	scanf("%d", &test);
	for(no=1;no<=test;++no)run();
}
