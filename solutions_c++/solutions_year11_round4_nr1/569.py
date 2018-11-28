//In the name of Allah
//
//
#include <iostream>
#include <utility>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <vector>
using namespace std;
typedef pair<int,int> pie;
const int MN=1000*1000+100;
vector <pie> moves;
struct wks
{
	wks() {}
	wks(const int &_s,const int &_e,const int & _sp)
	{
		a=_s;b=_e;c=_sp;
	}
	int a,b,c;
};
bool operator < (const wks & a,const wks & b)
{
	return a.a<b.a;
}
vector <wks> wk;
int T,s,r,c,x,n;
double t;
double res;
int main()
{
	ios::sync_with_stdio(false);
	cin>>T;
	for (int cas=1;cas<=T;cas++)
	{
		res=0;
		moves.clear();
		wk.clear();
		cin>>x>>s>>r>>t>>n;
		for (int i=0;i<n;i++)
		{
			int a,b,c;
			cin>>a>>b>>c;
			wk.push_back(wks(a,b,c));
		}
		sort(wk.begin(),wk.end());
		int now=0;
		for (int i=0;i<n;i++)
		{
			if (now!=wk[i].a)
			{
				moves.push_back(pie(s,wk[i].a-now));
				res+=(wk[i].a-now)/double(s);
			}
			moves.push_back(pie(s+wk[i].c,wk[i].b-wk[i].a));
			res+=(wk[i].b-wk[i].a)/double(s+wk[i].c);
			now=wk[i].b;
		}
		if (now!=x)
		{
			moves.push_back(pie(s,x-now));
			res+=(x-now)/double(s);
		}
		sort(moves.begin(),moves.end());
		now=0;
		while (abs(t)>=1e-10 && now<moves.size())
		{
			if (moves[now].second/double(moves[now].first-s+r)<=t)
			{
				res-=moves[now].second/double(moves[now].first);
				res+=moves[now].second/double(moves[now].first-s+r);
				t-=moves[now].second/double(moves[now].first-s+r);
			}
			else
			{
				double temp=t*double(moves[now].first-s+r);
				res-=temp/double(moves[now].first);
				res+=temp/double(moves[now].first-s+r);
				t=0;
			}
			now++;
		}
		cout<<"Case #"<<cas<<": ";
		cout<<fixed<<setprecision(10)<<res<<endl;
	}
	return 0;
}
