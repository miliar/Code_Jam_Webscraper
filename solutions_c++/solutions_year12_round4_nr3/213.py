#include<iostream>
#include<fstream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cassert>
#include<cstring>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<sstream>
#include<utility>
#include<algorithm>
#include<bitset>
#include<stack>
#include<queue>

#define f(i,a,b) for(int (i)=(a);(i)<(b);++(i))
#define fiter(i,type,b) for((type)::iterator (i)=(b).begin();(i)!=(b).end();++(i))
#define pb push_back
#define mp make_pair
#define sz size()
#define x first
#define y second
#define BIG 1000000000
using namespace std;

typedef pair<int,int> pii;
typedef long long lol;
typedef unsigned long long ull;
typedef pair<int,bool> pib;
typedef pair<long long, long long> pll;
typedef pair<double,double> pdd;

ifstream fin;
ofstream fout;
int x[10010];
long long h[10010];
vector<int> kid[10010];
int main()
{
	fin.open("C_small_attempt0.in");
	fout.open("C.out");
	int num_cases;
	fin>>num_cases;
	queue<int> proc;
	int curr;
	int n;
	long long tmp;
	pll a,b;
	for(int caseno=1;caseno<=num_cases;++caseno)
	{
		fin>>n;
		cerr<<"C"<<caseno<<"\n";
		//proc.clear();
		stack<int> check;
		f(i,0,n) kid[i].clear();
		f(i,0,n-1)
		{
			fin>>x[i];
			--x[i];
			h[i]=-1;
			kid[x[i]].pb(i);
		}
		h[n-1]=BIG;
		h[n]=BIG;
		x[n-1]=n;
		bool good=true;
		check.push(n);
		f(i,0,n-1)
		{
			while(check.top()==i) check.pop();
			if(x[i]>check.top())
			{
//				cerr<<x[i]<<" "<<check.top();
				good=false;
				break;
			}
			check.push(x[i]);
		}
		if(!good)
		{
			fout<<"Case #"<<caseno<<": Impossible\n";
			continue;
		}
		proc.push(n-1);
		while(!proc.empty())
		{
			curr=proc.front();
			proc.pop();
			a=mp(curr,h[curr]);
			b=mp(x[curr],h[x[curr]]);
			f(i,0,(int)kid[curr].sz)
			{
			//	cerr<<a.x<<" "<<a.y<<" "<<b.x<<" "<<b.y<<"\n";
			//	cerr<<"p"<<kid[curr][i]<<" "<<curr<<"\n";
				
				if(kid[curr][i]<a.x)
					h[kid[curr][i]]=a.y-(b.y-a.y)*(a.x-kid[curr][i])/(b.x-a.x)-1;
				else
				{
					h[kid[curr][i]]=(b.y-a.y)*(kid[curr][i]-a.x)/(b.x-a.x)+a.y;
				if((b.y-a.y)*(kid[curr][i]-a.x)%(b.x-a.x)==0)
					h[kid[curr][i]]--;
				}
			//	cerr<<"res "<<h[kid[curr][i]]<<"\n";
			//	cerr<<(b.y-a.y)<<" "<<(kid[curr][i]-a.x)<<"\n";
			//	cerr<<(b.x-a.x)<<" "<<a.y<<"\n";
			//	cerr<<"orig "<<(b.y-a.y)*(kid[curr][i]-a.x)/(b.x-a.x)<<"\n";
			//	cerr<<"alt "<<(b.y-a.y)*(a.x-kid[curr][i])/(b.x-a.x)<<"\n";
				b=mp(curr,h[curr]);
				a=mp(kid[curr][i],h[kid[curr][i]]);
				proc.push(kid[curr][i]);

			}
		}
		bool awesome=true;
		f(i,0,n) if(h[i]<0) awesome=false;
		if(awesome)
		{
			fout<<"Case #"<<caseno<<": ";
			f(i,0,n) fout<<h[i]<<" ";
			fout<<"\n";
		}
		else
		{
			fout<<"Case #"<<caseno<<": Impossible\n";
			cerr<<"ark!\n";
		}
	}

	fin.close();
	fout.close();
	return 0;
}
