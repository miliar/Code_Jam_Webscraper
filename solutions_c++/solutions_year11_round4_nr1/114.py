


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

void _main()
{
	int X,S,R,t,N;
	map<int,int> ma;
	cin>>X>>S>>R>>t>>N;
	int sum=0;
	for(int i=0;i<N;i++)
	{
		int a,b,w;
		cin>>a>>b>>w;
		ma[w]+=b-a;
		sum+=b-a;
	}
	ma[0]=X-sum;
	double res=0;
	double T=t;
	for(map<int,int>::iterator  it=ma.begin();it!=ma.end();it++)
	{
		double q=min((double)T,(double)it->second/(R+it->first));
		T-=q;
		res+=q+((double)it->second-q*(R+it->first))/(S+it->first);
	}
	printf("%.9f\n",res);
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
	}
}