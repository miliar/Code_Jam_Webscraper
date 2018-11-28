#pragma warning(disable: 4786)
#include <vector>
#include <sstream>
#include <list>
#include <bitset>
#include <set>
#include <stack>
#include <queue>
#include <functional>
#include <cmath>
#include <string>
#include <map>
#include <algorithm>
#include <iostream>
using namespace std;

double Pi =acos(-1.0);
#define oo 2147483647
#define inf 1e17
#define LL __int64
#define eps 1e-8
#define sign(x) ((x)>eps?1:((x)<-eps?-1:0)) 
#define MIN(a,b) (a)<(b)?(a):(b)
#define REP(i,N) for(i=0;i<N;++i)
#define FOR(i,a,b) for(i=(a);i<=(b);++i)
int p[41];
int main()
{
	//freopen("small_in.txt","r",stdin);
	//freopen("small_out.txt","w",stdout);	
	freopen("large_in.txt","r",stdin);	
	freopen("large_out.txt","w",stdout);

	int N,cs;
	int i,j,cur,n,ans;
	char b;
	char line[100];
	bool flag;
	cin>>N;
	FOR(cs,1,N)
	{
		cin>>n;
		cin.getline(line,100);
		REP(i,n)
		{
			p[i]=0;
			cin.getline(line,100);
			istringstream  iss;
			iss.str(line);
			REP(j,n)
			{
				iss>>b;
				if(b=='1')
					p[i]=j;
			}
		}
		REP(cur,n)
		{
			flag=false;
			REP(i,n)
			{
				if(p[i]==cur)
				{
					if(!flag)
						flag=true;
					else
						++p[i];
				}
			}
		}
		ans=0;
		for(cur=n-1;cur>=0;--cur)
		{
			REP(i,cur)
			{
				if(p[i]==cur)
				{
					FOR(j,i,cur-1)
					{
						p[j]=p[j+1];
						++ans;
					}
				}
			}
		}
		cout<<"Case #"<<cs<<": "<<ans<<endl;
		//printf("Case #%d: %I64d\n",cs,ans);
	}
	return 0;		
}
