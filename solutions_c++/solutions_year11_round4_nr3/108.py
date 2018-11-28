


#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <string> 
#include <cstring> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <ctime> 
#include <fstream>
using namespace std; 
template<class T> T gcd(T a,T b){return a==0?b:gcd(b%a,a);}
template<class T> string tostring(T a){ostringstream os;os<<a;return os.str();}
int toint(string a){istringstream is(a);int p;is>>p;return p;}
long long toll(string a){istringstream is(a);long long p;is>>p;return p;}

vector<long long> prime;
int p[1000205];

void _main()
{
	long long N;
	cin>>N;
	if(N==1)
	{
		cout<<0<<endl;
		return;
	}
	int res=1;
	for(int i=0;prime[i]*prime[i]<=N;i++)
	{
		long long n=N;
		res--;
		while(n>=prime[i])
		{
			res++;
			n/=prime[i];
		}
	}
	cout<<res<<endl;
}

void init()
{
	memset(p,0,sizeof(p));
	p[0]=p[1]=1;
	for(int i=2;i*i<1000205;i++)
	{
		if(p[i])continue;
		for(int j=i;i*j<1000205;j++)
		{
			p[i*j]=1;
		}
	}
	for(int i=2;i<1000205;i++)
	{
		if(!p[i])prime.push_back(i);
	}
}

int main()
{
	init();
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		cout<<"Case #"<<i<<": ";
		_main();
		cerr<<i<<"end"<<endl;
	}
}