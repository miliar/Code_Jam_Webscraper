#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
#include<iterator>
using namespace std;

#define i64 __int64
#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))
#define pi acos(-1.0)
#define inf ((i64)1<<30)
#define CLR(a) memset(a,0,sizeof(a))
#define SET(a) memset(a,-1,sizeof(a))
#define pb push_back
#define eps 1e-11

set<string>s;

int main()
{
	//freopen("in.txt","r",stdin);
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int cs,n,m,i,j,k,res,t=1;
	string dir;
	cin>>cs;
	while(cs--)
	{
		s.clear();
		cin>>n>>m;
		for(i=0;i<n;i++)
		{
			cin>>dir;
			s.insert(dir);
		}
		res=0;
		for(i=0;i<m;i++)
		{
			cin>>dir;
			while(1)
			{
				if(s.find(dir)==s.end())
				{
					res++;
					s.insert(dir);
				}
				else
				{
					break;
				}
				for(j=dir.size()-1;j>=0;j--)
				{
					if(dir[j]=='/')
						break;
				}
				if(j<=0)
					break;
				dir=dir.substr(0,j);
			}
		}
		printf("Case #%d: %d\n",t++,res);
	}
	return 0;
}


