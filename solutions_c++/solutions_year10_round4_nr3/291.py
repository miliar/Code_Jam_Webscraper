#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <string.h>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

const int inf = 1000*1000*1000;
#define CL(x,a) memset(x,a,sizeof(x));
#define ALL(v) (v).begin(),(v).end()
typedef long long LL;
int T;
vector< vector<int> > ar,br;
int Count()
{
	int res = 0;
	br.clear();
	br.resize(110,vector<int>(110,0));
	for (int i=1;i<110;i++)
	{
		for (int j=1;j<110;j++)
		{
			if (ar[i][j] == 1)
			{
				if (ar[i][j-1] == 0 && ar[i-1][j] == 0)
					br[i][j]=0;
				else
				{
					res++;
					br[i][j]=1;
				}
			}
			else
				if (ar[i][j-1] == 1 && ar[i-1][j] == 1)
				{
					br[i][j]=1;
					res++;
				}
		}
	}
	return res;
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	for (int i=0;i<T;i++)
	{
		ar.clear();
		br.clear();
		ar.resize(110,vector<int>(110,0));
		br.resize(110,vector<int>(110,0));
		int n;
		scanf("%d",&n);
		for (int z=0;z<n;z++)
		{
		int x1,x2,y1,y2;
		scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
		x1++; x2++; y1++; y2++;
		if (x1 > x2)
			swap(x1,x2);
		if (y1 > y2)
			swap(y1,y2);
		for (int z = y1;z<=y2;z++)
		{
			for (int j=x1;j<=x2;j++)
				ar[z][j]=1;
		}
		}
		int S =0;
		while (1)
		{
			int t = Count();
			if (t != 0)
			{
				S++;
				swap(ar,br);
			}
			else
				break;
		}
		printf("Case #%d: %d\n",i+1,S+1);
	}
	return 0;
}