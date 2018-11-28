#include <cstdlib> 
#include <cctype> 
#include <cstring> 
#include <cstdio> 
#include <cmath> 
#include <algorithm> 
#include <vector> 
#include <string> 
#include <iostream> 
#include <sstream> 
#include <map> 
#include <set> 
#include <queue> 
#include <stack> 
#include <fstream> 
#include <numeric> 
#include <iomanip> 
#include <bitset> 
#include <list> 
#include <stdexcept> 
#include <functional> 
#include <utility> 
#include <ctime> 
using namespace std; 

#define PB push_back 
#define MP make_pair 

#define rep(i,n) for(int i=0;i<(n);++i) 
#define FOR(i,l,h) for(int i=(l);i<=(h);++i) 
#define FORD(i,h,l) for(int i=(h);i>=(l);--i) 
#define print(expr) cout<<(#expr)<<" : "<<(expr)<<endl

typedef vector<int> VI; 
typedef vector<string> VS; 
typedef vector<double> VD; 
typedef long long int64; 
typedef pair<int,int> pii; 

const int maxp=1000050;

bool isp[maxp]={};
int64 p[maxp]={};
int v=0;

void Getprime(void)
{
	memset(isp,true,sizeof(isp));
	isp[0] = isp[1] = false;
	for(int i=2;i<maxp;i++) if(isp[i])
	{
		p[v++]=i;
		for(int j=i+i;j<maxp;j+=i)
		{
			isp[j]=false;
		}
	}
}

int Getpow(int p,int64 num)
{
	int res=0;
	int64 tmp = 1;
	while(tmp<=num) { tmp *= p; res++;}
	return res-1;
}

int main(void)
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	Getprime();
	int T; cin>>T;
	FOR(Case,1,T)
	{
		int64 n; cin>>n;
		if(n==1) { cout<<"Case #"<<Case<<": 0"<<endl; continue;}
		int ans=1;
		for(int i=0; p[i]*p[i] <= n;i++)
		{
			ans += Getpow((int)p[i],n) - 1;
		}
		cout<<"Case #"<<Case<<": "<<ans<<endl;
	}
}