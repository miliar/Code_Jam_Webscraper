#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<limits.h>
#include<string.h>

//Data Structures
#include<algorithm>
#include<vector>
#include<string>
#include<set>
#include<map>
#include<utility>
#include<bitset>
#include<stack>
#include<queue>
using namespace std;

#define FOR(i,a,b) 	for(int i= (int )a ; i < (int )b ; ++i)
#define rep(i,n) 	FOR(i,0,n)
#define INF		INT_MAX
#define ALL(x) 		x.begin(),x.end()
#define LET(x,a)	__typeof(a) x(a)
#define IFOR(i,a,b) 	for(LET(i,a);i!=(b);++i)
#define EACH(it,v) 	IFOR(it,v.begin(),v.end())
#define pb 		push_back
#define sz(x) 		int(x.size())
#define mp 		make_pair
#define fill(x,v)	memset(x,v,sizeof(x))
#define max(a,b)	((a)>(b)?(a):(b))
#define min(a,b)	((a)<(b)?(a):(b))
#define	si(n)		scanf("%d",&n)
#define pi(n)		printf("%d ",n)
#define pil(n)		printf("%d\n",n)
#define sl(n)		scanf("%lld",&n)
#define sd(n)		scanf("%lf",&n)
#define ss(n)		scanf("%s",n)
#define scan(v,n)	vector<int> v;rep(i,n){ int j;si(j);v.pb(j);}
#define mod 1e9 + 7
typedef pair<int,int> PI;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;
int main()
{
	int t;
	cin >> t;
	int k = t;
	while(t--)
	{
		vector<string> v;
		int i=0,j=0;
		int cx=0,co=0;
		int flag=0,flagb=0;
		for(i=0;i<4;i++)
		{
			string s;
			cin >> s;
			v.pb(s);
		}
		for(i=0;i<4;i++)
		{
			cx = 0;
			co = 0;
			for(j=0;j<4;j++)	
			{
				if(v[i][j] == 'X')
				{
					cx++;
				}
				else if(v[i][j] == 'O')
					co++;
				else if(v[i][j] == 'T')
				{
					cx++;
					co++;
				}
				else if(v[i][j] == '.')
				{
					flagb=1;
					break;		
				}
			}
			if(cx == 4)
			{
				flag = 1;
				break;
			}
			else if(co == 4)
			{
				flag = 2;
				break;
			}
		}
		if(flag == 0)
		{
			rep(j,4)
			{
				cx = 0;
				co = 0;
				rep(i,4)	
				{
					if(v[i][j] == 'X')
						cx++;
					else if(v[i][j] == 'O')
						co++;
					else if(v[i][j] == 'T')
					{
						cx++;
						co++;
					}
				else if(v[i][j] == '.')
					{
						flagb = 1;
						break;		
					}
				}
				if(cx == 4)
				{
					flag = 1;
					break;
				}
				else if(co == 4)
				{
					flag = 2;
					break;
				}
			}
			if(flag == 0)
			{
				cx = 0;
				co = 0;
				for(i=0;i<4;i++)
				{
					if(v[i][i] == 'X')
						cx++;
					else if(v[i][i]  == 'T')
					{
						cx++;
						co++;
					}
					else if(v[i][i] == 'O')
						co++;
				else if(v[i][i] == '.')
					{
						flagb = 1;
						break;
					}
				}
				if(cx == 4)
				{
					flag = 1;
				}
				else if(co == 4)
				{
					flag = 2;
				}
			}
			if(flag == 0)
			{
				cx = 0;
				co = 0;
				for(i=0;i<4;i++)
				{
					if(v[i][3-i] == 'X')
						cx++;
					else if(v[i][3-i]  == 'T')
					{
						cx++;
						co++;
					}
					else if(v[i][3-i] == 'O')
						co++;
					else if(v[i][3-i] == '.')
					{
						flagb = 1;
						break;
					}
				}
				if(cx == 4)
				{
					flag = 1;
				}
				else if(co == 4)
				{
					flag = 2;
				}
			}
		}
		cout << "Case #" << k-t << ": ";
		if(flag == 1)
		{
			cout << "X won" << endl;
			continue;
		}
		else if(flag == 2)
		{
			cout << "O won" << endl;
			continue;
		}
		else if(flagb == 1)
		{
			cout << "Game has not completed" << endl;
			continue;
		}
		else 
		{
			cout << "Draw" << endl;
			continue;
		}

	}
	return 0;
}
