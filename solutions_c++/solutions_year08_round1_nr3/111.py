#include<set>
#include<map>
#include<cmath>
#include<cstdio>
#include<vector>
#include<string>
#include<iostream>
#include<sstream>
#include<algorithm>
using namespace std;
#define FOR(i,a,b) for(int i=(a); i<(b); ++i)
#define FORE(i,a) for(typeof(a.begin()) i = a.begin(); i!= a.end(); ++i)
#define SET(x,v) memset(x,v,sizeof(x))
#define cs c_str()
#define sz size()
#define mp make_pair
#define pb push_back
double ans[32];
int comb[32][32];
int main() {
    freopen("cc.in","r",stdin);
	 int T,e=0;
	 scanf("%d",&T);
	 int n;
	 SET(comb, 0);
	 comb[0][0]= 1;
	 FOR(i,1,31) {
		 comb[i][0] = comb[i][i] = 1;
		 FOR(j,1,i) {
			 comb[i][j]=comb[i-1][j-1]+comb[i-1][j];
			 comb[i][j]%= 1000;
		 }
	 }
	 FOR(i,1,31) {
		 ans[i] = 0.0;
		 double a = 1.0, b = 1.0;
		 if (i%2)
			 b = sqrt(5.0);
		 FOR(k,0,i/2) {
			 b*= 5.0;
		 }
		 FOR(j,0,i+1) {
			 ans[i] += comb[i][j] * a * b;
			b/= sqrt(5.0);
			a*= 3.0;
		 }
		 printf("%d: %lf\n",i,ans[i]);
	 }
	 while(T--) {
		scanf("%d",&n);
		printf("Case #%d: %Lf\n",++e, ans[n]);
	 }
    return 0;
}


