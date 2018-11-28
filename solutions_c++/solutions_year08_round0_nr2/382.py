#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <sstream>
#include <iostream>
#include <queue>
//#include <cmath>

#define mp make_pair
#define sz(v)((int)((v).size()))
#define all(v) v.begin(),v.end()
#define pb push_back

using namespace std;

typedef pair<int,int> ii;
typedef long long int64;
typedef vector<int> vi;

template<class T> T abs(T x){return x>0 ? x:(-x);}
template<class T> T sqr(T x){return x*x;}

int t,na,nb;
vector<pair<ii,int> > events;

void GetTime(int& x)
{
	string s;
	cin >> s;
	int h,m;
	sscanf(s.c_str(),"%d:%d",&h,&m);
	x=h*60+m;
}

int main()
{
	int tc;
	cin >> tc;
	for(int ic=0;ic<tc;ic++){
		events.clear();
		cin >> t >> na >> nb;
		for(int i=0;i<na;i++)
		{
			int t1,t2;
			GetTime(t1);
			GetTime(t2);
			events.push_back(mp(ii(t1,1),0));
			events.push_back(mp(ii(t2+t,-1),1));
		}
		for(int i=0;i<nb;i++)
		{
			int t1,t2;
			GetTime(t1);
			GetTime(t2);
			events.push_back(mp(ii(t1,1),1));
			events.push_back(mp(ii(t2+t,-1),0));
		}
		sort(all(events));
		int cur[2],res[2];
		memset(cur,0,sizeof(cur));
		memset(res,0,sizeof(res));
		for(int i=0;i<sz(events);i++)
		{
			cur[events[i].second]-=events[i].first.second;
			res[events[i].second]=max(res[events[i].second],-cur[events[i].second]);
		}
		cout << "Case #" << (ic+1) << ": " << res[0] << " " << res[1] << "\n";
	}
	return 0;
}
