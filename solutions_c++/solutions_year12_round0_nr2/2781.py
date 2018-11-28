

#include<cstdio>
#include<iostream>
#include<algorithm>
#include<set>
#include<map>
#include<stack>
#include<list>
#include<queue>
#include<deque>
#include<cctype>
#include<string>
#include<vector>
#include<sstream>
#include<iterator>
#include<numeric>
#include<cmath>
#include<cstring>
#include<complex>
#include<cstdlib>
#include<climits>
#include<bitset>
using namespace std;
#define RFOR(i,a,b) for(int i=a; i > b; i--)
#define FOR(i,a,b) for(int i=a; i < b;i++)
#define PB push_back
#define BN begin()
#define ED end()
#define RN rbegin()
#define RD rend()
#define PF push_front
#define BP pop_back
#define FP pop_front
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define IT(X) __typeof((X).BN) 
#define RIT(X) __typeof((X).RN) 
#define REF(X) __typeof(__typeof(X)::reference) 
#define FORIT(it, X) for(IT(X) it = (X).BN; it != (X).ED; ++it) 
#define FORITR(it, X) for(RIT(X) it = (X).RN; it != (X).RD; ++it)
#define VV(X) vector< vector< X > > 
#define PIB(X) pair<IT(X),bool>
#define SQ ((x)*(x))
#define El() cout<<endl;

typedef long long LL;
typedef unsigned long long ULL;
typedef istringstream ISS;
typedef stringstream SS;
typedef vector<int> VI;
typedef pair <int,int> PII;
typedef vector< PII > VPII;

using namespace std;
int main()
{
        int cas,n=1,m,s,p,k;
	cin >> cas;
	while(n <= cas)
	{cin >> m>>s>>p;
	VI v;
	FOR(i,0,m)
	{cin >> k;
	v.PB(k);
	}
	int maxg=0,a,b,c,maxt;
	FOR(i,0,m)
	{if(v[i]%3 == 2)
	{if(s>0)
	{a=v[i]/3;
	b=v[i]/3+v[i]%3;s--;
	if((b>10)||(b<p)) {b=v[i]/3 + 1;s++;}
	c=v[i]-(a+b);
	}
	else
	{a=v[i]/3;
	//if(v[i]%3 == 2)
	b=v[i]/3 + 1;
	c=v[i]/3 + 1;
	}}
	else if(v[i]%3==0)
	{if(s>0) {a=v[i]/3;
		   b=v[i]/3+1;s--;//cout <<"m";
		  if((b<p)||(b>p)) { b=v[i]/3;s++;}
		   c=v[i]-(a+b);
		}
	else {a=v[i]/3;
		b=v[i]/3;
		c=v[i]-(a+b);
	}
	}
	else{a=v[i]/3;
		b=v[i]/3+v[i]%3;
		c=v[i]-(a+b);
		}
	maxt=max(a,b);
	if(max(maxt,c) >= p) maxg++;
	}
	cout<<"Case #"<<n<<": "<<maxg;
	cout<<endl;
	n++;			
	}
	return 0;
}
