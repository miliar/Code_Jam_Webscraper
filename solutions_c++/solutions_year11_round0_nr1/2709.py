#include <cstdio>
#include <numeric>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <sstream>
#include <cmath>
#include <iomanip>

using namespace std;

typedef vector <int> VI;
typedef vector <string> VS;
typedef long long LL;
typedef stringstream SS;

#define ALL(x) x.begin(),x.end()
#define REP(i,n) for(int i=0; i<(n); i++)
#define FOR(i,a,b) for(int i=(a); i<(b); i++)
#define FORE(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define PB push_back
#define sz size()
#define MP make_pair
#define two(x) (1<<(x))


/////////////////////////////////////////////////////////////////////////////////

int F(vector<pair<int,int> >& v)
{
	int p1=1, p2=1;
	int t1=0, t2=0;
	int l1=0, l2=0;
	REP(i, v.sz)
	{
		int which=v[i].first;
		int nextp=v[i].second;
		if(which==0)
		{
			int nextt1=max(t1+abs(nextp-p1), t2);
			l1=0;
			l2+=nextt1-t1+1;
			t1=nextt1+1;
			p1=nextp;
		}
		else
		{
			int nextt2=max(t2+abs(nextp-p2), t1);
			l2=0;
			l1+=nextt2-t2+1;
			t2=nextt2+1;
			p2=nextp;
		}
	}
	return max(t1, t2);
}


int main()
{

	int T, N;
	cin>>T;
	REP(index, T)
	{
		cin>>N;
		vector<pair<int,int> > v;
		REP(i,N)
		{
			char c;
			int p;
			cin>>c>>p;
			if(c=='O') v.PB(MP(0,p));
			else v.PB(MP(1,p));
		}
		int t=F(v);
		cout<<"Case #"<<index+1<<": "<<t<<endl;
	}
	return 0;
}
