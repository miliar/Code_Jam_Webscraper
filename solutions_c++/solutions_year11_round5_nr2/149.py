
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

#define mp make_pair
#define pb push_back

int p[10001];

void _main()
{
	int n;
	cin>>n;
	if(n==0)
	{
		cout<<"0"<<endl;
		return;
	}
	memset(p,0,sizeof(p));
	for(int i=0;i<n;i++)
	{
		int a;
		cin>>a;
		p[a]++;
	}
	int N=n;
	int ans=1E9;
	while(N>0)
	{
label:
		for(int i=0;i<10001;i++)
		{
			if(p[i]>0)
			{
				int j;
				for(j=i+1;j<=10000;j++)
				{
					if(p[j]<p[j-1])break;
				}
				ans=min(ans,j-i);
				for(int k=i;k<j;k++)
				{
					p[k]--;
				}
				N-=j-i;
				goto label;
			}
		}
	}
	cout<<ans<<endl;
}

int main()
{
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