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
bool prime(ll a)
{
	if(a==2)
		return true;
	if(a%2==0)
		return false;
	for(ll i=3;i*i<=a;i+=2)
		if(a%i==0)
			return false;
	return true;
}
int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	
	
	int testcase;
	scanf("%d ",&testcase);
	vi p;
	for(ll i=2;i<=1000000LL;++i)
		if(prime(i))
			p.push_back(i);
	rep(caseID,testcase)
	{
		ll n;
		cin>>n;
		ll c=0;
		if(n==1)
		{
			printf("Case #%d: %lld\n",caseID+1,c);
			continue;
		}
		for(int i=0;i<p.size();++i)
		{
			if(p[i]>n)
				break;
			ll now=n/p[i];
			while(now>=p[i])
			{
				now/=p[i];
				c++;
			}
		}
		printf("Case #%d: %lld\n",caseID+1,c+1);
	}
	
	return 0;
}

