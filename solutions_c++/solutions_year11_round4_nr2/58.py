#pragma comment(linker, "/STACK:65777216")

#include <algorithm>
#include <iostream>
#include <string>
#include<sstream>
#include<string.h>
#include <cstdio>
#include <vector>
#include <bitset>
#include <cmath>
#include <queue>
#include<stack>
#include <set>
#include <map>
#include<ctime>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef pair<double,double> pdd;
typedef unsigned long long ull;

#define FOR(i,a,b) for (int i(a); i < (b); i++) 
#define REP(i,n) FOR(i,0,n) 
#define SORT(v) sort((v).begin(),(v).end())
#define UN(v) sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())
#define CL(a,b) memset(a,b,sizeof(a))
#define pb push_back

char s[555][555];
ll   a[555][555];
ll   b[555][555];
ll   x[555][555];
ll   y[555][555];

int main(){ 
#ifdef LocalHost
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
#endif

	int tc;
	cin>>tc;
	REP(TC,tc){
		int best = 0;
		printf("Case #%d: ",TC+1);

		int n,m,d;
		cin>>n>>m>>d;
		REP(i,n) scanf(" %s",s[i]);
		REP(i,n){
			REP(j,m){
				a[i][j] = d + (s[i][j]-'0');
				b[i][j] = a[i][j];
				if(i) b[i][j] += b[i-1][j];
				if(j) b[i][j] += b[i][j-1];
				if(i&&j) b[i][j] -= b[i-1][j-1];

				x[i][j] = i * a[i][j];
				if(i) x[i][j] += x[i-1][j];
				if(j) x[i][j] += x[i][j-1];
				if(i&&j) x[i][j] -= x[i-1][j-1];

				y[i][j] = j * a[i][j];
				if(i) y[i][j] += y[i-1][j];
				if(j) y[i][j] += y[i][j-1];
				if(i&&j) y[i][j] -= y[i-1][j-1];
			}
		}
		int k = min(n,m);
		for(;k>=3;k--){
			REP(i,n-k+1)REP(j,m-k+1){
				int ex = i + k - 1;
				int ey = j + k - 1;

				ll sum = x[ex][ey];
				if(ex-k>=0) sum -= x[ex-k][ey];
				if(ey-k>=0) sum -= x[ex][ey-k];
				if(ex-k>=0 && ey-k>=0) sum += x[ex-k][ey-k];

				ll w = b[ex][ey];
				if(ex-k>=0) w -= b[ex-k][ey];
				if(ey-k>=0) w -= b[ex][ey-k];
				if(ex-k>=0 && ey-k>=0) w += b[ex-k][ey-k];

				sum -= w * i;

				sum -= a[ex][j] * (k-1);
				sum -= a[ex][ey] * (k-1);

				w -= a[ex][j];
				w -= a[ex][ey];
				w -= a[i][j];
				w -= a[i][ey];

				if(sum * 2 != (k-1) * w) continue;

				sum = y[ex][ey];
				if(ex-k>=0) sum -= y[ex-k][ey];
				if(ey-k>=0) sum -= y[ex][ey-k];
				if(ex-k>=0 && ey-k>=0) sum += y[ex-k][ey-k];

				w = b[ex][ey];
				if(ex-k>=0) w -= b[ex-k][ey];
				if(ey-k>=0) w -= b[ex][ey-k];
				if(ex-k>=0 && ey-k>=0) w += b[ex-k][ey-k];

				sum -= w * j;

				sum -= a[i][ey] * (k-1);
				sum -= a[ex][ey] * (k-1);

				w -= a[ex][j];
				w -= a[ex][ey];
				w -= a[i][j];
				w -= a[i][ey];

				if(sum * 2 != (k-1) * w) continue;




				best = k;
				goto here;

				

			}
		}

	here:
		if(best == 0) puts("IMPOSSIBLE");
		else cout<<best<<endl;
	}


/*#ifdef LocalHost
	cout<<endl<<endl<<clock()<<endl;
#endif*/
	return 0;
}