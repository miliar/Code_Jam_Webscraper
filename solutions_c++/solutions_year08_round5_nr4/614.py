#include <iostream>
#include <algorithm>
#include <string>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <complex>
#include <cstring>
#include <cmath>
using namespace std;
const int inf=(1<<31)-1,mn=20;
typedef pair<int,int> ipair;
#define mp(A,B) make_pair(A,B)
#define pb(X) push_back(X)
#define clr(x) memset(x,0,sizeof(x))
int d[102][102];
bool rock[102][102];

int fun(int a,int b)
{
	if(a==1&&b==1)return 1;
	if(rock[a][b])return d[a][b]=0;
	if(d[a][b]!=-1)return d[a][b];
	int sum=0;
	if(a-1>=0&&b-2>=0&&!rock[a-1][b-2])
		sum=(sum+fun(a-1,b-2))%10007;
	if(a-2>=0&&b-1>=0&&!rock[a-2][b-1])
		sum=(sum+fun(a-2,b-1))%10007;
	return d[a][b]=sum;
}
int pk,k;
int main()
{
	freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
	scanf("%d\n",&pk);
	for(k=1;k<=pk;k++)
	{

		int w,h;
		int R;
		int r,c;
		scanf("%d%d%d\n",&h,&w,&R);
		memset(d,-1,sizeof d);
		memset(rock,0,sizeof rock);
		int i;
		for(i=0;i<R;i++)
		{
			scanf("%d %d",&r,&c);
			rock[r][c]=1;
		}
		printf("Case #%d: %d\n",k,fun(h,w));
	}
	return 0;

}
