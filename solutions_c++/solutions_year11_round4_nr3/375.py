#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <set>
using namespace std;
#define forn(i,n) for(int i=0; i<(n); i++)
const int N = 1000000+10;
bool P[N];
void init() {
	memset(P,true,sizeof(P));
	P[0]=P[1]=false;
	for(int i=2;i<N;i++) {
		if(P[i]==false) continue;
		for(int d=2;d*i<N;d++)P[d*i]=false;
	}
}

int main() {

  freopen("C-large.in", "r", stdin);
   freopen("out.txt", "w", stdout);
   int ncase; cin >> ncase;
   init();
   forn(icase, ncase) {
		long long n; cin >> n;
		int a = 0, b = 0;
		if(n==1) { printf("Case #%d: %d\n",icase+1,0); continue;}
		if(n==2) { printf("Case #%d: %d\n",icase+1,1); continue;}
		int res = 1;
		for(long long i=2;i*i<=n;i++) if(P[i]) {
			long long k = i*i;
			while(k<=n) {
				res++;
				k*=i;
			}
		}

		printf("Case #%d: %d\n", icase+1, res);
   }
}
	