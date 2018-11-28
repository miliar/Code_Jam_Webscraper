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

char C[400][400];
bool R[500][500];
char S[1000],A[1000];
int n;

int cnt[1000];

string run() {
	memset(C,0,sizeof(C)); memset(R,0,sizeof(R));
	int N, M;
	scanf("%d", &N);
	for(int i=0;i<N;++i){
		char S[100];
		scanf("%s",S);
		C[S[0]][S[1]]=C[S[1]][S[0]]=S[2];
	}
	scanf("%d", &M);
	for(int i=0;i<M;++i){
		scanf("%s",S);
		R[S[0]][S[1]]=R[S[1]][S[0]]=true;
	}
	scanf("%d", &N);
	scanf("%s", S);
	n=0;
	memset(A,0,sizeof(A));
	for(int i=0;i<N;++i) {
		A[n ++] = S[i];
		while(n > 1) {
			if(C[A[n-1]][A[n-2]]) {
				A[n-2]=C[A[n-1]][A[n-2]];
				A[--n]=0;
			} else {
				bool flag=false;
				for(int i=0;i<n-1;++i)
					if(R[A[i]][A[n-1]]) {
						flag = true;
					}
				if(flag){
					fill(A,A+n,0);
					n=0;
				} else break;
			}
		}
	}
	string ret;
	ret.push_back('[');
	for(int i=0;i<n;++i){
		if(i) {
			ret.push_back(',');
			ret.push_back(' ');
		}
		ret.push_back(A[i]);
	}
	ret.push_back(']');
	return ret;
}

int main() {
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	
	int test;
	scanf("%d", &test);
	for(int no=1;no<=test;++no){
		printf("Case #%d: %s\n",no,run().c_str());
	}
}
