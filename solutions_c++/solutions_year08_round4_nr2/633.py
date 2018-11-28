#include <cstdio>
#include <iostream>
using namespace std;
const int MAXN=10000+10;
int a[MAXN];
int d[MAXN][2];
int c[MAXN];
const int INF=1<<29;
void solution(int num)
{
	printf("Case #%d: ",num);
	int A;
	int n,m;
	scanf("%d %d",&n,&m);
	scanf("%d",&A);
	
	
	int y1,y3,x1;
	for(y1=0;y1<=m;y1++)
		for(y3=0;y3<=m;y3++)
		{
			if(y1==y3) continue;
			for(x1=0;x1<=n;x1++)
			{
				if((A-x1*y3)%(y1-y3)==0&&(A-x1*y3)/(y1-y3)>=0&&(A-x1*y3)/(y1-y3)<=n)
				{
					printf("%d %d %d %d %d %d\n",x1,y1,(A-x1*y3)/(y1-y3),0,0,y3);
					return ;
				}
				if((-A-x1*y3)%(y1-y3)==0&&(-A-x1*y3)/(y1-y3)>=0&&(-A-x1*y3)/(y1-y3)<=n)
				{
					printf("%d %d %d %d %d %d\n",x1,y1,(-A-x1*y3)/(y1-y3),0,0,y3);
					return ;
				}
			}
		}
	printf("IMPOSSIBLE\n");
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int n;
	scanf("%d",&n);
	int i;
	for(i=0;i<n;i++)
		solution(i+1);
	return 0;
}
