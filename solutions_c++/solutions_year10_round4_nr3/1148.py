#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define MP make_pair
#define X first
#define Y second
#define ALL(x) x.begin(),x.end()
#define CLR(x) memset(x,0,sizeof(x))
#define FOR(i,a,b) for(int i=(a);i<(b);i++) 
#define DOR(i,a,b) for(int i=(a);i>=(b);i--) 
int DX[]={-1,0,1,0};
int DY[]={0,1,0,-1};
#define oo 0x3f3f3f3f
typedef long long LL;
typedef pair<int,int> PII;
typedef pair<double,double> PDD;
typedef pair<int,PII> PIP;
typedef vector<PII> VII;
const double eps = 1e-10;
#define N 202

int R;
int gp[N][N],tmp[N][N];
int main()
{
		freopen("data.in","r",stdin);
	freopen("data.out","w",stdout);
	int cas;
	scanf("%d",&cas);
	FOR(casid,0,cas)
	{
		scanf("%d",&R);
		CLR(gp);
		int x=5,y=5;
		int r=-1,c=-1;
		FOR(i,0,R)
		{
			int r1,r2,c1,c2;
			cin>>r1>>c1>>r2>>c2;
			r=max(r,r2);
			c=max(c,c2);
			FOR(j,r1,r2+1)
			{
				FOR(k,c1,c2+1)
				{
					gp[j+x][k+y]=1;
				}
			}
		}
		int ans;
		FOR(i,0,10000)
		{
			//FOR(j,1,r+2*x)FOR(j,1,c+2*x)tmp[i][j]=gp[i][j];
			FOR(j,1,r+2*x+1)
			{
				FOR(k,1,c+2*y+1)
				{
					if(gp[j][k]==1)
					{
						if(gp[j-1][k]==0&&gp[j][k-1]==0)tmp[j][k]=0;
						else tmp[j][k]=1;
					}
					else
					{
						if(gp[j-1][k]==1&&gp[j][k-1]==1)tmp[j][k]=1;
						else tmp[j][k]=0;
					}
				}
			}
			int key=0;
			FOR(j,1,r+2*x)FOR(k,1,c+2*y)
			{
					gp[j][k]=tmp[j][k];
					if(gp[j][k]==1)++key;
			}
			if(!key)
			{
				ans=i;
				break;
			}
		}
		printf("Case #%d: %d\n",casid+1,ans+1);
	}
}