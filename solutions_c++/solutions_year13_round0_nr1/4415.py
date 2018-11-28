#include<iostream>
#include<list>
#include<string>
#include<cstring>
#include<sstream>
#include<cctype>
#include<string.h>
#include<algorithm>
#include<cmath>
#include<stack>
#include<fstream>
#include<cstdlib>
#include<vector>
#include<map>
#include<set>
#include<utility>
#include<iomanip>
#include<queue>

using namespace std;

#define INF (1<<29)
#define SET(a) memset(a,-1,sizeof(a))
#define ALL(a) a.begin(),a.end()
#define CLR(a) memset(a,0,sizeof(a))
#define FILL(a,v) memset(a,v,sizeof(a))
#define PB push_back
#define FOR(i,n) for(int i = 0;i<n;i++)
#define PI acos(-1.0)
#define EPS 1e-9
#define MP(a,b) make_pair(a,b)
#define min3(a,b,c) min(a,min(b,c))
#define max3(a,b,c) max(a,max(b,c))
#define READ freopen("input.txt", "r", stdin)
#define WRITE freopen("output.txt", "w", stdout)
#define LL long long
#define MX 34000
#define MOD 1000000007

#define p(x) printf("%d",x)
#define inp(x) scanf("%d",&x)
#define inpll(x) scanf("%lld",&x)
#define getcx getchar_unlocked
/*inline void inp( int &n ) 
 {
    n=0;
    int ch=getcx();int sign=1;
    while( ch < '0' || ch > '9' ){if(ch=='-')sign=-1; ch=getcx();}
 
    while(  ch >= '0' && ch <= '9' )
            n = (n<<3)+(n<<1) + ch-'0', ch=getcx();
    n=n*sign;
  }*/


using namespace std;
int main()
{
	int t,ans,d,cs=1,e=0;
	char c,f;
	string a[4];
	inp(t);
	for(cs=1;cs<=t;cs++)
	{
		ans=d=e=0;
		for(int i=0;i<4;i++)
		cin>>a[i];
		//for(int i=0;i<4;i++)
		//cout<<a[i]<<endl;
		f=a[0][0];
		if(f=='T')
		f=a[1][1];
		if(f!='.')
		{
			for(int i=0;i<4;i++)
			{
				c=a[i][i];
				if(c==f||c=='T')
				ans=1;
				else
				{
					if(c=='.')
					d=1;
					ans=0;
					break;
				}
			}
			if(ans==1)
			{
				printf("Case #%d: %c won\n",cs,f);
				continue;
			}
		}
		else
		d=1;
		
		f=a[0][3];
		if(f=='T')
		f=a[1][2];
		if(f!='.')
		{
			for(int i=0;i<4;i++)
			{
				c=a[i][3-i];
				if(c==f||c=='T')
				ans=1;
				else
				{
					if(c=='.')
					d=1;
					ans=0;
					break;
				}
			}
			if(ans==1)
			{
				printf("Case #%d: %c won\n",cs,f);
				continue;
			}
		}
		else
		d=1;
		
		for(int j=0;j<4;j++)
		{
			f=a[j][0];
			if(f=='T')
			f=a[j][1];
			if(f!='.')
			{
				for(int i=0;i<4;i++)
				{
					c=a[j][i];
					if(c==f||c=='T')
					ans=1;
					else
					{
						if(c=='.')
						d=1;
						ans=0;
						break;
					}
				}
				if(ans==1)
				{
					e=1;
					printf("Case #%d: %c won\n",cs,f);
					break;
				}
			}
			else
			d=1;
		}
		if(e==1)
		continue;
		
		for(int j=0;j<4;j++)
		{
			f=a[0][j];
			if(f=='T')
			f=a[1][j];
			if(f!='.')
			{
				for(int i=0;i<4;i++)
				{
					c=a[i][j];
					if(c==f||c=='T')
					ans=1;
					else
					{
						if(c=='.')
						d=1;
						ans=0;
						break;
					}
				}
				if(ans==1)
				{
					e=1;
					printf("Case #%d: %c won\n",cs,f);
					break;
				}
			}
			else
			d=1;
		}
		if(e==1)
		continue;
		if(d==1)
		printf("Case #%d: Game has not completed\n",cs);
		else
		printf("Case #%d: Draw\n",cs);
		//cout<<"remain\n";
	}
	return 0;
}