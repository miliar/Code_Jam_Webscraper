#include<cstdio>
#include<algorithm>
#include<cmath>
#include<vector>

#define FOR(i,a,b) for(int i=(a); i<(int)(b); ++i)
#define FORD(i,a,b) for(int i=(a)-1; i>=(int)(b); --i)
#define FORE(i,C) for(__typeof(C.begin()) i=C.begin(); i!=C.end(); ++i)
#define MP make_pair
#define FI first
#define SE second
#define PB push_back

using namespace std;

typedef long long LL;

int num[3][3];

void testcase(int tNum) {
	int n,A,B,C,D,X,Y,M;
	scanf("%d %d %d %d %d %d %d %d",&n,&A,&B,&C,&D,&X,&Y,&M);
	FOR(i,0,3) FOR(j,0,3) num[i][j] = 0;
	FOR(i,0,n) {
		num[X%3][Y%3]++;
		X = (A*1LL*X + B)%M;
		Y = (C*1LL*Y + D)%M;
	}
	LL res = 0;
	FOR(i,0,9) if(num[i/3][i%3]>0) {
		int ix=i/3, iy=i%3;
		int a = num[ix][iy]--;
		FOR(j,i,9) if(num[j/3][j%3]>0) {
			int jx=j/3, jy=j%3;
			int b = num[jx][jy]--;
			FOR(k,j,9) if(num[k/3][k%3]>0) {
				int kx=k/3, ky=k%3;
				if((ix+jx+kx)%3==0 && (iy+jy+ky)%3==0) {
					LL toAdd = a*1LL*b*1LL*num[kx][ky];
					int numEq = 0;
					if(i==j) numEq++;
					if(j==k) numEq++;
					if(numEq==1) toAdd /= 2;
					if(numEq==2) toAdd /= 6;
					res += toAdd;
				}
			}
			num[jx][jy]++;
		}
		num[ix][iy]++;
	}
	printf("Case #%d: %lld\n",tNum,res);
}

int main() {

	int t;
	scanf("%d",&t);
	FOR(i,0,t) testcase(i+1);
	
	return 0;
}
