// zero.lin`s google_codejam.cpp 
//
#include "google_codejam\stdafx.h"
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vii;
typedef pair<int,int> pii;
typedef long long ll;

#define rep(i,n) for(int i=0;i<n;++i)
#define all(n) n.begin(),n.end()
#define sz(o) (int)(o.size())
#define mset(o,v) memset(o,v,sizeof(o))
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) 
#define mk(first,second) make_pair(first,second)
#define present(container, element) (container.find(element) != container.end()) 
#define cpresent(container, element) (find(all(container),element) != container.end())

const ll inf=1LL<<60;
const double eps=1e-11;
ll gcd(ll a,ll b){return b==0?a:gcd(b,a%b);};

int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	
	
	int testcase;
	scanf("%d ",&testcase);
	
	rep(caseID,testcase)
	{
		int x,s,r,t,n;
		cin>>x>>s>>r>>t>>n;
		vector<pair<pii,int> > c;
		vector<pair<int,pii > > c2;
		rep(i,n)
		{
			int s,e,v;
			cin>>s>>e>>v;
			c.push_back(pair<pii,int>(pii(s,e),v));
			c2.push_back(pair<int,pii >(v,pii(s,e)));
		}
		sort(all(c));
		sort(all(c2));
		double time=0;
		int now=0;
		r=max(r,s);
		double have=t;
		c.push_back(pair<pii,int>(pii(x,x),0));
		rep(i,n+1)
		{
			double need=1.0*(c[i].first.first-now)/r;
			if(need<have)
			{
				time+=need;
				have-=need;
			}
			else
			{
				time+=have;
				time+=(need-have)*r/s;
				have=0;
			}
			now=c[i].first.second;
			//time+=1.0*(c[i].first.second-c[i].first.first)/(s+c[i].second);
		}
		rep(i,n)
		{
			double need=1.0*(c2[i].second.second-c2[i].second.first)/(r+c2[i].first);
			if(need<have)
			{
				time+=need;
				have-=need;
			}
			else
			{
				time+=have;
				time+=(need-have)*(r+c2[i].first)/(s+c2[i].first);
				have=0;
			}
		}
		
		printf("Case #%d: %llf\n",caseID+1, time);
	}
	
	return 0;
}

