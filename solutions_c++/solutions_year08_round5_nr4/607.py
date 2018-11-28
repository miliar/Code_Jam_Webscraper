#include<iostream>
#include<memory>
#include<cmath>
#include<queue>
#include<map>
#include<set>
#include<vector>
#include<stack>
#include<algorithm>
#define int64 __int64
#define DEBUG cout<<"ERROR"<<endl;


using namespace std;
const int N=10007;
int m,n;
int check(int x,int y)
{
	return 1<=x && x<=m && 1<=y && y<=n;
}
int a[128][128];

int main()
{

	
	//DEBUG;

	freopen("D-small-attempt3.in","r",stdin);
	freopen("D-small-attempt3.out","w",stdout);
	int i,j,k,seq,num,r,x,y;

	scanf("%d",&num);
	for(seq=1;seq<=num;seq++)
	{
		memset(a,0,sizeof(a));
		scanf("%d %d %d",&m,&n,&r);
		for(i=1;i<=r;i++)
		{
			scanf("%d %d",&x,&y);
			a[x][y]=-1;
		}
	//	DEBUG;
		a[1][1]=1;
		for(i=1;i<=m;i++)
		for(j=1;j<=n;j++)
		{
			if(a[i][j]<=0)
				continue;
			x=i+2;
			y=j+1;
			if(check(x,y) && a[x][y]>=0)
				a[x][y]+=a[i][j];
			if(a[x][y]>=N)
				a[x][y]-=N;
			x=i+1;
			y=j+2;
			if(check(x,y) && a[x][y]>=0)
				a[x][y]+=a[i][j];
			if(a[x][y]>=N)
				a[x][y]-=N;
		//	DEBUG;
		}
		printf("Case #%d: %d\n",seq,a[m][n]);
	}
	return 0;
}


