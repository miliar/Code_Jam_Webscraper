#include<iostream>
#include<string>
#include<algorithm>
#include<fstream>
#include<cstdio>
#include<vector>
#include<list>
#include<sstream>
#include<map>
#include<queue>
#include<deque>
#include<set>
#include<cmath>
#include<functional>
#include<memory>
#include<stack>

//check http://www.ttmath.org for more info
#include <ttmath/ttmath.h>


using namespace std;



#define FOR(i,a,b) for(int i = a; i<b;++i)
#define RFOR(i,a,b) for(int i = (b-1); i>=a; --i)
#define REP(i,a) FOR(i,0,a)
#define RREP(i,a) RFOR(i,0,a)


#define ALL(a) a.begin(),a.end()
#define FILL(a,val) memset(a,val,sizeof(a))
#define pb(a) push_back(a)
#define sz(a) a.size()

#define mp make_pair

typedef long long Int;
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<VI > VII;

const int INF = (1<<30);

typedef ttmath::Int<10> Long;

Long GCD(Long x, Long y)
{
	while(x!=0 && y!=0)
		if(x>y)
			x%=y;
		else
			y %=x;
	return (x+y);
}


int main()
{
	int T,n;
	cin>>T;
	Long a,res,prev,t;
	REP(i,T)
	{
		t = prev = 0;
		cin>>n;
		REP(j,n)
		{
			cin>>a;
			if(prev != 0)
			{
				if(a>prev)
					t = GCD(t,a-prev);
				else
					t = GCD(t,prev-a);
			}
			prev = a;
		}
		res =t-a%t;
		if(res == t)
			res = 0;
		cout<<"Case #"<<i+1<<": "<<res<<endl;
	}
	return 0;
}