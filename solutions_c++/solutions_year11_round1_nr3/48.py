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

int C[100],S[100],T[100],V[100];

vector<int> A;

int main() {
	int i,j,m,n,k;
	FILE* fp = fopen("B.in","r");
	FILE* fp1 = fopen("B.out","w");
	int N,M;
	int t1,tt;
	fscanf(fp,"%d",&tt);
	FOR(t1,tt) {
		A.clear();
		fscanf(fp,"%d",&N);
		FOR(i,N) { fscanf(fp,"%d%d%d",&C[i],&S[i],&T[i]); if ((T[i] == 0) && (C[i] == 0)) A.pb(S[i]); }
		fscanf(fp,"%d",&M);
		FOR(i,M) fscanf(fp,"%d%d%d",&C[N+i],&S[N+i],&T[N+i]);
		M += N;
		memset(V,0,sizeof(V));
		int s = 0, t = 1;
		int ans = 0;
		int q;
		while (true) {
			FOR(i,N) if (V[i] == 0) if (T[i] > 0) {
				t += T[i]-1;
				V[i] = 1;
				s += S[i];
				if ((C[i] == 1) && (N != M)) {
					if ((T[N] == 0) && (C[N] == 0)) A.pb(S[N]);
					N++;
				}
			}
			sort(A.begin(),A.end());
			reverse(A.begin(),A.end());
			q = s;
			FOR(i,t) if (i < A.sz) q += A[i];
			ans = max(ans, q);
			if (t == 0) break; 
			int b = -1;
			FOR(i,N) if (V[i] == 0) if ((T[i] == 0) && (C[i] == 1)) {
				if (b == -1) b = i;
				if (S[b] < S[i]) b = i;
			}
			if (b == -1) break;
			s += S[b];
			V[b] = 1;
			t--;
			ans = max(ans,s);
			if (t == 0) break; 
			if (N != M) {
				if ((T[N] == 0) && (C[N] == 0)) A.pb(S[N]);
				N++;
			}
		}
		fprintf(fp1,"Case #%d: %d\n",t1+1,ans);
	}
	fclose(fp1);
	fclose(fp);
	return 0;
}