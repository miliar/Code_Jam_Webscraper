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
long long int a,b,c,d,x0,y0,n,m;
long long int count[4][4]={};
for(int ppp=0;ppp<_;++ppp)
{
memset(count,0,sizeof(count));
scanf("%lld%lld%lld%lld%lld%lld%lld%lld",&n,&a,&b,&c,&d,&x0,&y0,&m);
long long int x,y;
x=x0,y=y0;
for(int i=0;i<n;++i)
{
int xx=x%3,yy=y%3;
count[xx][yy]++;
//cout<<x<<" "<<y<<" "<<xx<<" "<<yy<<endl;
 x=(a*x+b)%m;
y=(c*y+d)%m;
}
//REP(i,3){REP(j,3)cout<<count[i][j]<<". ";cout<<endl;}
long long int ans=0;
for(int i=0;i<9;++i)
    for(int j=i;j<9;++j)
       for(int k=j;k<9;++k)
         {
int x1=i/3,y1=i%3;
int x2=j/3,y2=j%3;
int x3=k/3,y3=k%3;
if((x1+x2+x3)%3||(y1+y2+y3)%3)continue;
if(i==j&&count[x1][y1]<2)continue;
if(i==k&&count[x1][y1]<2)continue;
if(j==k&&count[x2][y2]<2)continue;
if(i==j&&i==k&&count[x1][y1]<3)continue;
//cout<<x1<<" "<<y1<<" "<<x2<<" "<<y2<<" "<<x3<<" "<<y3<<" "<<x1+x2+x3<<" "<<y1+y2+y3<<endl;
if(i!=j&&i!=k&&j!=k)ans+=count[x1][y1]*count[x2][y2]*count[x3][y3];
else
if(i==j&&i==k)ans+=(count[x1][y1]*(count[x1][y1]-1)*(count[x1][y1]-2))/6;
else
if(i==j)ans+=(count[x1][y1]*(count[x1][y1]-1)*(count[x3][y3]))/2;
else 
if(i==k)ans+=(count[x1][y1]*(count[x1][y1]-1)*(count[x2][y2]))/2;
else
if(k==j)ans+=(count[x2][y2]*(count[x2][y2]-1)*(count[x1][y1]))/2;
}
cout<<"Case #"<<ppp+1<<": "<<ans<<endl;
}
	return 0;
}

