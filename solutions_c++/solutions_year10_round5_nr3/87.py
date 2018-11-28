#pragma warning(disable:4786)
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<functional>
#include<string>
#include<cstring>
#include<cstdlib>
#include<queue>
#include<utility>
#include<fstream>
#include<sstream>
#include<cmath>
#include<stack>
#include<cstdio>
#include <iomanip>


using namespace std;

#define MEM(a,b) memset(a,(b),sizeof(a))
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b)  ((a) < (b) ? (a) : (b))
#define istr(S) istringstream sin(S)
#define MP make_pair
#define pb push_back
#define inf 1000000000

typedef pair<int,int> pi;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef vector<pi> vpi;

#define inf 1000000000

//typedef long long LL;
typedef __int64 LL;

int pos[205];


int main()
{
	int i,j,k,l,tests,cs=0,n;
	

	//freopen("D:\\gcj\\A-large.in","r",stdin);
	freopen("D:\\gcj\\C0.out","w",stdout);

	scanf("%d",&tests);
	while(tests--)
	{
		map<int,int> S;
		vi all;
		scanf("%d",&n);

		for(i=0;i<n;i++)
		{
			int x,p;
			scanf("%d%d",&x,&p);
			S[x]=p;
			all.pb(x);
		}

		int ans=0;

		while(1)
		{

			int ok=1;

			//for(i=0;i<all.size();i++)
				//printf("=%d %d\n",all[i],S[all[i]]);

			for(i=0;i<all.size();i++)
			{
				int x=all[i];
				int p=S[x];
				if(p<=1) continue;

			
				ok=0;

				ans+=p/2;
			    if(S.find(x-1)==S.end())
					S[x-1]=p/2,all.pb(x-1);
				else
					S[x-1]+=(p/2);

				if(S.find(x+1)==S.end())
					S[x+1]=p/2,all.pb(x+1);
				else
					S[x+1]+=(p/2);

				S[x]%=2;

				break;
			}

			//cin>>i;

			if(ok==1) break;
		}
		
		printf("Case #%d: %d\n",++cs,ans);
	}

	return 0;
} 


