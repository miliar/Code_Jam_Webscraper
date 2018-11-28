#include <vector>
#include <map>
#include <set>
#include <stack>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <cctype>
#include <cstring>
#include <queue>
#include <cassert>

using namespace std;

typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;

#define MP make_pair
#define ST first
#define ND second
#define PB push_back
#define FOR(i,a,b) for( int i=(a); i<(b); ++i)
#define FORD(i,a,b) for( int i=(a); i>(b); --i)
#define REP(i,n) for(int i=0; i<(n); ++i)
#define ALL(X) (X).begin(),(X).end()
#define SZ(X) (int)(X).size()
#define FORE(it,X) for(__typeof((X).begin()) it=(X).begin(); it!=(X).end();++it)

int n,pd,pg;

int main()
{
	int tn;
	cin>>tn;

	while (tn--) {
		cin>>n>>pd>>pg;
		bool pos=true;
		if (pg==100) {
			if (pd<100)
				pos=false;
		}
		if (pg==0) {
			if (pd>0)
				pos=false;
		}

		int w=-1;
		FOR(d,1,min(101,n+1)) {
			if (pd*d%100==0) {
				w=pd*d/100;
				break;
			}
		}

		if (w==-1) pos=false;

		static int qq=0;
		printf("Case #%d: ",++qq);
		if (pos) cout<<"Possible"<<endl;
		else cout<<"Broken"<<endl;
	}
	return 0;
}
