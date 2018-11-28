#include <map>     
#include <set>     
#include <cmath>    
#include <cstdio>   
#include <vector>     
#include <string>     
#include <sstream>    
#include <iostream>    
#include <algorithm>     
using namespace std;     
#define FOR(i,a,b) for(int i=(a); i<(b); ++i)     
#define FORE(it,x) for(typeof(x.begin()) it=x.begin(); it!=x.end(); ++it)     
#define SET(x, v) memset(x, v, sizeof (x))     
#define sz size()     
#define cs c_str()     
#define pb push_back     
#define mp make_pair    
typedef pair<int, int> IP;

typedef long long i64;     

const int c = 8192 * 2;

int dat[c][3];
int idx[32768];
//int idx[10001][32768];

int comp(const void *a, const void *b) {
	int* A = (int *) a;
	int* B = (int *) b;
	return A[0] - B[0];
}
int comp2(const void *a, const void *b) {
	int* A = (int *) a;
	int* B = (int *) b;
	return A[1] - B[1];
}
void add(int C) {
	int st = C + c;
	while(st>0) {
		idx[st]++;
		st>>=1;
	}
}
int lteq(int C) {
	//less than or equal
	int l = 0 + c, r = c + C;
	int ret= 0;
	while(l<=r && l>0) {
		if(l&1) {
			ret+= idx[l];
			l++;
		}
		if((r&1)==0) {
			ret+= idx[r];
			r--;
		}
		l>>=1;
		r>>=1;
	}
	return ret;
}
int main() {

	freopen("A.in","r",stdin);
	int n, T, e=0;
	scanf("%d",&T);
	while(T--) {
		scanf("%d",&n);
		FOR(i,0,n)
			scanf("%d%d%d",&dat[i][0],&dat[i][1],&dat[i][2]);
		qsort(dat, n, sizeof(dat[0]), comp);
		int ans=0;
		FOR(i,0,n) {
			int A = dat[i][0];
			int BC = 10000 - A;
			qsort(dat, (i+1), sizeof(dat[0]), comp2);
			SET(idx, 0);
			/*
			FOR(k,0,n) {
				printf("%5d %5d %5d\n",dat[k][0],dat[k][1],dat[k][2]);
				if(k==i)
					printf("------------------------\n");
			}
			printf("\n");
			*/
			FOR(j,0,i+1) {
				int B = dat[j][1];
				int C = BC - B;
				add(dat[j][2]);
				if(C>=0) {
					int cnt = lteq(C);
				//printf("j:%d cnt:%d A(%d) B(%d) C(%d) BC(%d)\n",j,cnt,A,B,C,BC);
					ans=max(ans, cnt);
				}
			}			
		}
		printf("Case #%d: %d\n",++e, ans);
	}

	return 0;
}

