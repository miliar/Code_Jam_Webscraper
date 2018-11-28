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

int main()
{
	int tn;
	cin>>tn;

	while (tn--) {
		int n;
		cin>>n;
		string seq;
		queue<int> qo,qb;
		REP(i,n) {
			char a;
			int v;
			scanf(" %c %d",&a,&v);
			if (a=='O')
				qo.push(v);
			else
				qb.push(v);
			seq+=a;
		}
		qo.push(1);
		qb.push(1);

		int o,b,t,s;
		o=b=1;
		t=s=0;

		while (s<SZ(seq)) {
			bool pp=false;
			if (seq[s]=='O' && o==qo.front()) {
				pp=true;
				qo.pop();
			}
			else {
				if (o<qo.front())
					o++;
				else if (o>qo.front())
					o--;
			}

			if (seq[s]=='B' && b==qb.front()) {
				pp=true;
				qb.pop();
			}
			else {
				if (b<qb.front())
					b++;
				else if (b>qb.front())
					b--;
			}

			if (pp)
				s++;

			t++;
		}
		static int qq=1;
		printf("Case #%d: %d\n",qq++,t);
	}
	return 0;
}
