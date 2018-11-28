#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <algorithm>
using namespace std;
typedef long long ll;

const int maxn=100000;
int trees[maxn][2];


int main(int argc,char *argv[])
{
    freopen("CropTriangles.in", "r", stdin);
    freopen("CropTriangles.out", "w", stdout);
    int numCases;
    scanf("%d",&numCases);
    for(int curCase=1;curCase<=numCases;curCase++)
    {
	ll n, A, B, C, D, x0, y0,M;
	scanf("%lld%lld%lld%lld%lld%lld%lld%lld",&n,&A,&B,&C,&D,&x0,&y0,&M);
	ll X = x0, Y = y0;
	trees[0][0]=X;
	trees[0][1]=Y;
	for(int i = 1;i<n;i++)
	{
	    X = (A * X + B) % M;
	    Y = (C * Y + D) % M;
	    trees[i][0]=X;
	    trees[i][1]=Y;
	}
	ll count=0;
	for(int a=0;a<n;a++)
	    for(int b=0;b<a;b++)
		for(int c=0;c<b;c++)
		    if((trees[a][0]+trees[b][0]+trees[c][0])%3==0&&(trees[a][1]+trees[b][1]+trees[c][1])%3==0)
			count++;
	printf("Case #%d: %lld\n",curCase,count);
    }
    return 0;
}
   
