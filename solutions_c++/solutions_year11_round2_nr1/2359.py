#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <functional>
#include <cmath>
#include <sstream>
#include <memory.h>
     
#define forn(i,n) for (int i = 0; i < (int)(n); i++)
#define forv(i, a) for(int i=0; i<(int)a.size(); i++)
#define mset(a, val) memset(a, val, sizeof(a))
#define all(a) a.begin(),a.end()
#define mp make_pair
#define pb push_back
#define sz size()
#define VI vector< int >
#define VS vector< string >
#define PII pair< int,int >
#define PDD pair< double,double >
#define PIS pair< int, string >
#define sqr(a) ((a)*(a))
#define cube(a) ((a)*(a)*(a))
#define pi 3.1415926535897932384626433832795
const int inf=1000*1000*1000;
#define eps 1e-6
#define ll long long
using namespace std;

#define name "A-small"
//#define testing

char a[105][105];
PII wp[105];
PII owp[105];
int n;

int gcd(int a, int b){
	if(b==0) return a;
	else return gcd(b, a%b);
}

void clear(){
	forn(i, n) {
		wp[i].first=wp[i].second=0;
		owp[i].first=0;owp[i].second=1;
	}

}

int main(){
#ifdef testing
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#else
	freopen(name".in", "r", stdin);
    freopen(name".out", "w", stdout);
#endif

	int T;
	scanf("%d", &T);

	forn(q, T){
		printf("Case #%d: \n", q+1);

		scanf("%d", &n);
		clear();

		forn(i, n) scanf("%s", a[i]);

		//wp
		forn(i, n) forn(j, n)
		{
			if(a[i][j]!='.') wp[i].second++;
			if(a[i][j]=='1') wp[i].first++;
		}

		

		//owp
		forn(i, n){
			int t=0;

			forn(j, n){
				if(j==i || a[i][j]=='.')continue;
				PII temp=wp[j];
				t++;

				
				temp.second--;
				if(a[i][j]=='0') temp.first--;

				if(temp.second!=0) {
					owp[i]=mp(owp[i].first*temp.second+owp[i].second*temp.first, owp[i].second*temp.second);
					int g=gcd(owp[i].first, owp[i].second);
					owp[i].first/=g; owp[i].second/=g;
				}
			}

			owp[i].second*=t;
			int g=gcd(owp[i].first, owp[i].second);
			owp[i].first/=g; owp[i].second/=g;
		}

		forn(i, n){
			double ans=0.25*wp[i].first/wp[i].second + 0.50 * owp[i].first/owp[i].second;
			double av=0;
			int t=0;

			forn(j, n) if(j!=i && a[i][j]!='.') {
				av+=1.0*owp[j].first/owp[j].second;
				t++;
			}
			//printf("av %d\n", av);
			av/=t;
			ans+=0.25*av;

			printf("%.10f\n", ans);
		}
		
	}

	

	return 0;
}