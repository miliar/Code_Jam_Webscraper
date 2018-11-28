#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<algorithm>
#include<iterator>
#include<map>
#include<vector>
#include<list>
#include<set>
#include<queue>
#include<cassert>
#include<deque>
#include<stack>
#include<bitset>
#include<functional>
#include<numeric>
#include<utility>
#include<sstream>
#include<iomanip>
#include<string>
#include<cmath>
#include<ctime>
using namespace std;
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii; 
priority_queue<ii,vector<ii>, greater<ii> > Q; //ascending order
priority_queue<ii> QQ;//normal descending order
#define mp make_pair
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define debug 0
#define FOR(i,j,k) for(int i=j;i<k;++i)	
#define RREP(i,n) for(int i=n;i>=0;--i)		
#define REP(i,n) for(int i=0;i<n;i++)
int main()
{
int _;
scanf("%d",&_);
for(int ppp=0;ppp<_;++ppp)
{
long long int p,k,l,tmp;
scanf("%lld%lld%lld",&p,&k,&l);
vector<long long int>v;
REP(i,l)scanf("%lld",&tmp),v.pb(tmp);
sort(v.begin(),v.end());
long long int cnt=0,ans=0,pp=1;
if(k*p<l){cout<<"Impossible\n";continue;}
for(int i=l-1;i>=0;--i)
{
if(cnt==k)cnt=0,pp++;
ans+=v[i]*pp;
//cout<<v[i]*pp<<" ";
cnt++;
}

cout<<"Case #"<<ppp+1<<": "<<ans<<endl;
}

	return 0;
}

