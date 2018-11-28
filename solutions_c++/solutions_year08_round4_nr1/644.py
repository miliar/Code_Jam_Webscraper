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
	int n,v;
	int i;
	scanf("%d %d",&n,&v);
	for(i=1;i<=(n-1)/2;i++)
		scanf("%d %d",&a[i],&c[i]);
	
	for(i=((n-1)/2)+1;i<=n;i++)
	{
		scanf("%d",&a[i]);
		d[i][a[i]]=0;
		d[i][a[i]^1]=INF;
	}
	
	int e1,e2;
	for(i=(n-1)/2;i>0;i--)
	{
		//1
		e1=d[i*2][1]+d[i*2+1][1];
		e2=min(min(d[i*2][0]+d[i*2+1][1],d[i*2][1]+d[i*2+1][0]),d[i*2][1]+d[i*2+1][1]);
		
		if(a[i]) d[i][1]=e1;
		else d[i][1]=e2;
		
		if(c[i])
			d[i][1]=min(e1+(a[i]?0:1),e2+(a[i]?1:0));
		
		//0
		e1=min(min(d[i*2][1]+d[i*2+1][0],d[i*2][0]+d[i*2+1][1]),d[i*2][0]+d[i*2+1][0]);
		e2=d[i*2][0]+d[i*2+1][0];
		
		if(a[i]==1) d[i][0]=e1;
		else d[i][0]=e2;
		
		if(c[i])
			d[i][0]=min(e1+(a[i]?0:1),e2+(a[i]?1:0));
		
		if(d[i][0]>INF) d[i][0]=INF;
		if(d[i][1]>INF) d[i][1]=INF;
		
	}
	printf("Case #%d: ",num);
	if(d[1][v]==INF) printf("IMPOSSIBLE");
	else printf("%d",d[1][v]);
	printf("\n");
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
