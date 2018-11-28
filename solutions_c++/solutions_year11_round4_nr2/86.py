#include <stdio.h>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <utility>
#include <math.h>

using namespace std;

#define lint long long

#define sz size()
#define pb push_back
#define mp make_pair

#define FOR(i,n) SFOR(i,0,n)
#define SFOR(i,m,n) for(i=m;i<n;i++)
#define FORD(i,n) for(i=n-1;i>=0;i--)

int A[510][510];
int X[510][510];
int Y[510][510];
int V[510][510];

int i,j,k,p;
int n,m,K;
int S;
int SX, SY;

bool Check() {
	memset(V,0,sizeof(V));
	FOR(i,m) {
		S = 0;
		FOR(k,K) S += A[i][k];
		FOR(j,n-K+1) {
			X[i][j] = S;
			S += A[i][j+K]-A[i][j];
		}
	}
	FOR(j,n-K+1) {
		S = 0;
		FOR(k,K) S += (2*k-K+1)*X[k][j];
		SX = 0;
		FOR(k,K) SX += X[k][j];
		FOR(i,m-K+1) {
			if (S == (K-1)*(A[i+K-1][j]+A[i+K-1][j+K-1]-A[i][j]-A[i][j+K-1])) V[i][j] = 1;
			S += (K+1)*X[i+K][j] + (K-1)*X[i][j];
			SX += X[i+K][j] - X[i][j];
			S -= 2*SX;
		}
	}
	FOR(j,n) {
		S = 0;
		FOR(k,K) S += A[k][j];
		FOR(i,m-K+1) {
			Y[i][j] = S;
			S += A[i+K][j]-A[i][j];
		}
	}
	FOR(i,m-K+1) {
		S = 0;
		FOR(k,K) S += (2*k-K+1)*Y[i][k];
		SY = 0;
		FOR(k,K) SY += Y[i][k];
		FOR(j,n-K+1) {
			if (S == (K-1)*(A[i][j+K-1]+A[i+K-1][j+K-1]-A[i][j]-A[i+K-1][j])) if (V[i][j] == 1) return true;
			S += (K+1)*Y[i][j+K] + (K-1)*Y[i][j];
			SY += Y[i][j+K] - Y[i][j];
			S -= 2*SY;
		}
	}
	return false;
}

int main() {
	char ch;
	FILE *fp = fopen("B.in","r");
	FILE *fp1 = fopen("B.out","w");
	int t,tt;
	fscanf(fp,"%d",&tt);
	FOR(t,tt) {
		fscanf(fp,"%d%d%d",&m,&n,&i);
		memset(A,0,sizeof(A));
		FOR(i,m) FOR(j,n) {
			do { fscanf(fp,"%c",&ch); } while ((ch < '0') || (ch > '9'));
			A[i][j] = ch-'0';
		}
		fprintf(fp1,"Case #%d: ",t+1);
		for(K=min(m,n);K>=3;K--) {
			if (Check()) { fprintf(fp1,"%d\n",K); break; }
		}
		if (K == 2) fprintf(fp1,"IMPOSSIBLE\n");
	}
	fclose(fp);
	fclose(fp1);
	return 0;
}