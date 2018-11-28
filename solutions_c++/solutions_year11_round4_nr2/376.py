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

#define PB push_back
#define MP make_pair

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;

long long g[600][600],s[600][600],s1[600][600],s2[600][600];
string st;
bool flag;
int T,casenum,i,n,m,d,j,k;
int main()
{
	freopen("problem.in","r",stdin);
	freopen("problem.out","w",stdout);
	cin>>T;
	for (casenum=1;casenum<=T;casenum++)
	{
		cout<<"Case #"<<casenum<<": ";
		cin>>n>>m>>d;
		memset(s,0,sizeof(s));
		memset(s1,0,sizeof(s1));
		memset(s2,0,sizeof(s2));
		for (i=1;i<=n;i++)
		{
			cin>>st;
			for (j=1;j<=m;j++)
				g[i][j]=st[j-1]-'0'+d;
		}
		for (i=1;i<=n;i++)
			for (j=1;j<=m;j++)
			{
				s[i][j]=s[i-1][j]+s[i][j-1]-s[i-1][j-1]+g[i][j];
				s1[i][j]=s1[i-1][j]+s1[i][j-1]-s1[i-1][j-1]+i*g[i][j];
				s2[i][j]=s2[i-1][j]+s2[i][j-1]-s2[i-1][j-1]+j*g[i][j];
			}
		flag=false;
		for (k=min(n,m)-1;k>=2;k--)
		{
			if (flag) break;
			for (i=1;i+k<=n;i++)
				for (j=1;j+k<=m;j++)
				{
					if (flag) break;
					int tmp,tmp1,tmp2;
					tmp=s[i+k][j+k]-s[i-1][j+k]-s[i+k][j-1]+s[i-1][j-1];
					tmp-=g[i][j]+g[i+k][j]+g[i][j+k]+g[i+k][j+k];
					tmp1=s1[i+k][j+k]-s1[i-1][j+k]-s1[i+k][j-1]+s1[i-1][j-1];
					tmp1-=i*g[i][j]+(i+k)*g[i+k][j]+i*g[i][j+k]+(i+k)*g[i+k][j+k];
					tmp2=s2[i+k][j+k]-s2[i-1][j+k]-s2[i+k][j-1]+s2[i-1][j-1];
					tmp2-=j*g[i][j]+j*g[i+k][j]+(j+k)*g[i][j+k]+(j+k)*g[i+k][j+k];
					if ((i+k/2.0)*tmp==tmp1&&(j+k/2.0)*tmp==tmp2)
					{
						flag=true;
						cout<<k+1<<endl;
					}
				}
		}
		if (!flag) cout<<"IMPOSSIBLE"<<endl;
	}
}

