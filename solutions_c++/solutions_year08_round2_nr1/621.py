#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#include <map>
#include <vector>
#include <iostream>
#include <string>

using namespace std;

#define MAX 100000
#define PI 3.141592653589793238

vector<int> vi;
vector<string> vs;
vector<long> vl;
map<string, int> lut;

int main(int argc, char **argv) {

long long N, n, A, B, C, D, x0, y0, M;
long long X[MAX],Y[MAX];
vector<long> vx, vy;
long i,j,k,p,q;

scanf("%lld", &N);

for(i=1;i<=N;i++) {

	scanf("%lld %lld %lld %lld %lld %lld %lld %lld", &n, &A, &B, &C, &D, &x0, &y0, &M); 
	
	vx.clear(), vy.clear();
	X[0]=x0; Y[0]=y0;
//	printf("X=%d, Y=%d\n",X,Y);
	for(k=1;k<n;k++) {
		X[k] = (A*X[k-1] + B) % M;
		Y[k] = (C*Y[k-1] + D) % M;
		for(p=0;p<k;p++) {
			if(X[p]==X[k] && Y[p]==Y[k])
				printf("HIT!\n");
		}
//		printf("X=%d, Y=%d\n",X,Y);
	}
	long ans=0;
	for(k=0;k<n-2;k++) {
		for(p=k+1;p<n-1;p++) {
			for(q=p+1;q<n;q++) {
				if(X[k]==X[p] && Y[k]==Y[p]) continue;
				if(X[p]==X[q] && Y[p]==Y[q]) continue;
				if(X[q]==X[k] && Y[q]==Y[k]) continue;
				if(((X[k]+X[p]+X[q])%3 == 0) && ((Y[k]+Y[p]+Y[q])%3 == 0)) {
					ans++;
					//printf("%ld %ld, %ld %ld, %ld %ld\n", X[k], Y[k], X[p], Y[p], X[q], Y[q]);
				}
			}
		}
	}

	printf("Case #%d: %d\n",i, ans);


} //for

} //main
