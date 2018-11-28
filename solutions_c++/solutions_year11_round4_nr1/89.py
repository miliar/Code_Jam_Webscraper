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

pair<int,int> C[1010];

int main() {
	int i,j,n,m;
	int X,S,R,N;
	FILE *fp = fopen("A-large.in","r");
	FILE *fp1 = fopen("A.out","w");
	int t,tt;
	fscanf(fp,"%d",&tt);
	FOR(t,tt) {
		fscanf(fp,"%d%d%d%d%d",&X,&S,&R,&j,&N);
		double T,t1,ans;
		double k;
		T = j;
		ans = 0;
		C[N].second = X;
		C[N].first = 0;
		FOR(i,N) { fscanf(fp,"%d%d%d",&j,&C[i].second,&C[i].first); C[i].second -= j; C[N].second -= C[i].second; }
		N++;
		sort(C,C+N);
		FOR(i,N) {
			t1 = C[i].second*1.0/(C[i].first + R);
			if (T >= t1) {
				T -= t1;
				ans += t1;
				continue;
			} else {
				ans += T;
				t1 -= T;
				T = 0;
				t1 = (C[i].first + R)*t1/(C[i].first + S);
				ans += t1; 
			}
		}
		fprintf(fp1,"Case #%d: %.10lf\n",t+1,ans);
	}
	fclose(fp);
	fclose(fp1);
	return 0;
}