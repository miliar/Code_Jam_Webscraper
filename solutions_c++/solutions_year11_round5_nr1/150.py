
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

void _main()
{
	int W,L,U,G;
	cin>>W>>L>>U>>G;
	vector<pair<int,int> > l,u;
	for(int i=0;i<L;i++)
	{
		int x,y;
		cin>>x>>y;
		l.push_back(mp(x,y));
	}	
	for(int i=0;i<U;i++)
	{
		int x,y;
		cin>>x>>y;
		u.push_back(mp(x,y));
	}
	vector<double> lo(W+1),up(W+1);
	for(int i=0;i<l.size()-1;i++)
	{
		for(int j=l[i].first;j<=l[i+1].first;j++)
		{
			lo[j]=l[i].second+(double)(j-l[i].first)/(l[i+1].first-l[i].first)*(l[i+1].second-l[i].second);
		}
	}	
	for(int i=0;i<u.size()-1;i++)
	{
		for(int j=u[i].first;j<=u[i+1].first;j++)
		{
			up[j]=u[i].second+(double)(j-u[i].first)/(u[i+1].first-u[i].first)*(u[i+1].second-u[i].second);
		}
	}
	vector<double> area(W+1,0);
	for(int i=0;i<W;i++)
	{
		area[i+1]=area[i]+(up[i]-lo[i]+up[i+1]-lo[i+1]);
	}
	double rd=area[W]/G;
	vector<double> ans(G-1);
	for(int i=0;i<G-1;i++)
	{
		double pp=(1+i)*rd;
		for(int j=0;j<W;j++)
		{
			if(pp>=area[j]&&pp<=area[j+1])
			{
				double ar=(pp-area[j]);
				double d2=(up[j+1]-lo[j+1]);
				double d=up[j]-lo[j];
				if(abs(d-d2)<=1e-8)
				{
					ans[i]=j+(ar)/(area[j+1]-area[j]);
				}
				else
				{
					double a=d2-d;
					double b=2*d;
					double c=-ar;
					double as=(-b+sqrt(b*b-4*a*c))/(2*a);
					ans[i]=as+j;
				}
			}
		}
	}
	cout<<endl;
	for(int i=0;i<G-1;i++)
	{
		printf("%.10f\n",ans[i]);
	}
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