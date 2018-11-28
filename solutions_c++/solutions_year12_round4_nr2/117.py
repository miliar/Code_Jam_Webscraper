#include <iostream>
#include <algorithm>
#include <cstring>
#include <climits>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <cmath>
using namespace std;
int A[1005], R[1005], X[1005], Y[1005], posx[3005], posy[3005], xi, yi;
int main() {
	int T;
	srand(42);
	scanf("%d",&T);
	for(int cn=1;cn<=T;++cn) {
		int N,W,L;
		xi = yi = 0;
		scanf("%d%d%d",&N,&W,&L);
		for(int i=0;i<N;++i) scanf("%d",&R[i]);
		for(int i=0;i<N;++i) A[i] = i;
		bool noans = 1;
		for(;;) {
			random_shuffle(A,A+N);
			X[A[0]] = Y[A[0]] = 0;
			posx[xi++] = posy[yi++] = 0;
			posx[xi++] = posy[yi++] = R[A[0]];
			bool can = 1;
			for(int i=1;i<N;++i) {
				int x,y;
				for(;;) {
					for(int j=-1;j<1;++j) {
						if(j < 0) x = 0;
						else x = posx[rand()%xi] + R[A[i]];
						if(x > W) continue;
						for(int k=-1;k<1;++k) {
							if(k < 0) y = 0;
							else y = posy[rand()%yi] + R[A[i]];
							if(y > L) continue;
							bool fail = 0;
							for(int l=0;l<i;++l) {
								long long dx = (X[A[l]]-x);
								long long dy = (Y[A[l]]-y);
								long long dr = (R[A[l]]+R[A[i]]);
								if(dx*dx + dy*dy < dr*dr) {
									fail = 1;
									break;
								}
							}
							if(!fail) goto end;
						}
					}
				}
				can = 0;
				break;
				end:;
				X[A[i]] = x;
				Y[A[i]] = y;
				posx[xi++] = x + R[A[i]];
				posy[yi++] = y + R[A[i]];
			}
			if(can) {
				printf("Case #%d:",cn);
				for(int i=0;i<N;++i) {
					assert(X[i] <= W && Y[i] <= L);
					for(int j=0;j<i;++j) {
						long long dx = (X[i]-X[j]);
						long long dy = (Y[i]-Y[j]);
						long long dr = (R[i]+R[j]);
						assert(dx*dx + dy*dy >= dr*dr);
					}
				}
				for(int i=0;i<N;++i) printf(" %d %d",X[i],Y[i]);
				printf("\n");
				break;
			}
		}
	}
}
