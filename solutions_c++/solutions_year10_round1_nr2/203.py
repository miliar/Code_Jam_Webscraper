#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <string.h>
#include <math.h>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

const int inf = 1000*1000*1000;
#define CL(x,a) memset(x,a,sizeof(x));
#define ALL(v) (v).begin(),(v).end();
typedef long long LL;
int T,n,D,I,M;
vector<int> v;
unsigned int ar[128][512];
void update(int x, int y, int val)
{
	y+=256;
	if (ar[x][y] <= val)
		return;
	ar[x][y]=val;
	for(;y;y>>=1)
	{
		ar[x][y>>1]= min(ar[x][y>>1],ar[x][y]);
	}
}
int getMin(int x, int L, int R)
{
	if (x+1==0)
		return 0;
	unsigned int res = (x+1)*D;
	for (L+=256,R+=256;L<R;L>>=1,R>>=1)
	{
		if (L & 1)
			res = min(res, ar[x][L++]);
		if (R & 1)
			res = min(res, ar[x][--R]);
	}
	return res;
}
void proc(int pos)
{
	int res = 0,t;
	for (int i=0;i<256;i++)
	{
		res = abs(v[pos]-i)+getMin(pos-1,max(0,i-M),min(255,i+M)+1);
		if (M != 0)
		{
			for (int j=0;j<256;j++)
			{
				update(pos,j,(int)ceil(abs(i-j)/(M+0.0))*I+res);
			}
		}
		else
		{
			update(pos,i,res);
		}
		update(pos,i,getMin(pos-1,i,i+1)+D);
	}
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	for (int i=0;i<T;i++)
	{
		scanf("%d%d%d%d",&D,&I,&M,&n);
		v.resize(n);
		for (int j=0;j<n;j++)
		{
			scanf("%d",&v[j]);
		}
		CL(ar,-1);
		for (int j=0;j<n;j++)
			proc(j);
		int res = getMin(n-1,0,256);
		printf("Case #%d: %d\n",i+1,res);
	}
	return 0;
}