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
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}//NOTES:checkmin(
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}//NOTES:checkmax(
#define SIZE(x) ((int)(x).size())
#define for0(i,n) for(int i=0;i<(n);i++)
#define for1(i,n) for(int i=1;i<=(n);i++)
#define for0r(i,n) for(int i=(n)-1;i>=0;i--)
#define for1r(i,n) for(int i=(n);i>=1;i--)
typedef long long ll;

int d[10010];
int l[10010];
int f[10010];

int solve()
{
	int N;
	scanf("%d",&N);
	for0(i,N)
	{
		scanf("%d %d",&d[i],&l[i]);
	}
	scanf("%d",&d[N]);l[N]=0;
	memset(f,-1,sizeof(f));
	f[0]=0;
	for0(i,N)
	{
		if(!~f[i])continue;
		for(int j=i+1;j<=N;j++)
		{
			int dl=d[i]-f[i];
			if(d[i]+dl>=d[j])
			{
				int t;
				if(d[j]-l[j]<=d[i])
				{
					t=d[i];
				}
				else
				{
					t=d[j]-l[j];
				}
				if(f[j]==-1 || f[j]>t)
				{
					f[j]=t;
				}
			}
		}
		if(~f[N])return 1;
	}
	return 0;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T,Tc=0;
	scanf("%d",&T);
	while(++Tc<=T)
	{
		printf("Case #%d: ",Tc);
		if(solve())
		{
			puts("YES");
		}
		else
		{
			puts("NO");
		}
	}
	return 0;
}