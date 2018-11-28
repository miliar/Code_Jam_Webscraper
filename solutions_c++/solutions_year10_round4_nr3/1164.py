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




void calc()
{
	int R;
	cin>>R;
	set<pair<int,int> > v,w;
	REP(i,R)
	{
		int x1,x2,y1,y2;
		cin>>x1>>y1>>x2>>y2;
		for(int j=x1; j<=x2; j++) for(int k=y1; k<=y2; k++) {v.insert(MP(j,k)); }
	}
		

		int ret=0;
		while(v.sz!=0)
		{
			ret++;
			w=v;
			FORE(k,v)
			{
				int x=(*k).first;
				int y=(*k).second;
				if(x==0 or y==0 or (v.find(MP(x,y-1))==v.end() and v.find(MP(x-1,y))==v.end()))
				{
					w.erase(MP(x,y));
				}
				if( (x>0 and v.find(MP(x-1, y+1))!=v.end()) )
				{
					w.insert(MP(x, y+1));
				}	
				if( (y>0 and v.find(MP(x+1, y-1))!=v.end()) )
				{
					w.insert(MP(x+1, y));
				}
			}
			v=w;
		}
		cout<<ret;
	

}


int main()
{
	int cases;
	cin>>cases;
	string line;
	getline(cin, line);

	REP(index, cases)
	{
		cout<<"Case #"<<index+1<<": ";
		
		calc();

		cout<<endl;
	}

	return 0;
}
