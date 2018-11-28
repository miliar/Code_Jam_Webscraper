#include <vector>
#include <string>
#include <set>
#include <algorithm>
#include <map>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
using namespace std;

set<pair<__int64,__int64> > P[3][3];
__int64 SZ[3][3];

int main() {
	freopen("Al.in","r",stdin);
	freopen("Al.out","w",stdout);
	int i,j,k,l, N, n, T;
	__int64 A, B, C, D, x0, y0, M, X, Y,cnt;
	scanf("%d",&N);
	for(n=1;n<=N;n++) {
		cnt = 0;
		scanf("%d %I64d %I64d %I64d %I64d %I64d %I64d %I64d",&T, &A, &B, &C, &D, &x0, &y0, &M);
		X = x0; 
		Y = y0;
		for(i=0;i<3;i++) {
			for(j=0;j<3;j++) {
				P[i][j].clear();
			}
		}
		P[X%3][Y%3].insert(make_pair(X,Y));
		for(i = 1;i<T;i++) {
			X = (A * X + B) % M;
			Y = (C * Y + D) % M;
			P[X%3][Y%3].insert(make_pair(X,Y));
		}
		for(i=0;i<3;i++) {
			for(j=0;j<3;j++) {
				SZ[i][j] = P[i][j].size();
				cnt += SZ[i][j]*(SZ[i][j]-1)*(SZ[i][j]-2) / 6;
			}
		}
		for(i=0;i<3;i++) {
			cnt += SZ[i][0]*SZ[i][1]*SZ[i][2];
			cnt += SZ[0][i]*SZ[1][i]*SZ[2][i];
		}
		for(i=0;i<3;i++) {
			cnt += SZ[i][0]*SZ[(i+1)%3][1]*SZ[(i+2)%3][2];
			cnt += SZ[2][i]*SZ[1][(i+1)%3]*SZ[0][(i+2)%3];
		}
		printf("Case #%d: %I64d\n",n,cnt);
	}
	return 0;
}