#include<iostream>
#include<string>
#include<vector>
#include<cmath>
#include<algorithm>
using namespace std;
__int64 n,A,B,C,D,M,i,j,k;

typedef struct node
{
__int64 x,y;
}node;
node f[300];
int main()
{
		freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int ca,N;
	scanf("%d",&N);
	for(ca=1;ca<=N;ca++)
	{
		__int64 ret=0;
		scanf("%I64d%I64d%I64d%I64d%I64d%I64d%I64d%I64d",&n,&A,&B,&C,&D,&f[0].x,&f[0].y,&M);
		
		//f[0].x=x0;f[0].y=y0;
		for(i=1;i<n;i++)
		{
		   f[i].x=(A*f[i-1].x+B)%M;
           f[i].y=(C*f[i-1].y+D)%M;
	//	  printf("%I64d%I64d%I64d%I64d%I64d%I64d%I64d%I64d%I64d\n",n,A,B,C,D,f[0].x,f[0].y,M,f[i].x);// cout<<f[i].x<<endl;
		}
		for(i=0;i<n;i++)
			for(j=i+1;j<n;j++)
				for(k=j+1;k<n;k++)
				{
					__int64 px=(f[i].x+f[j].x+f[k].x),py=(f[i].y+f[j].y+f[k].y);
					if(px%3==0&&py%3==0)
						ret++;

				}
				printf("Case #%d: %I64d\n",ca,ret);
	}
	return 0;
}