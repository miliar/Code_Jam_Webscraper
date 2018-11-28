#include<iostream>
using namespace std;
struct node
{
		int opr;
		int v;
		int num[2];
		bool vis;
}a[10001];
int m;
int min(int x,int y){return x<y?x:y;}
void dp(int root)
{
	int b[2][2];
	a[root].vis=1; 
//	printf("node:%d v:%d num[0]:%d,num[1]:%d opr:%s\n",root,a[root].v,a[root].num[0],a[root].num[1],a[root].opr?"AND":"OR");
	if(2*root>m)return ;
	else 
	{
		if(a[root*2].vis==0)dp(root*2);
		if(a[root*2+1].vis==0)dp(root*2+1);
		b[1][0]=b[0][1]=b[0][0]=b[1][1]=1000000;
		if(a[root*2].num[0]!=-1&&a[root*2+1].num[0]!=-1)b[0][0]=min(b[0][0],a[root*2].num[0]+a[root*2+1].num[0]);
		if(a[root*2].num[0]!=-1&&a[root*2+1].num[1]!=-1)b[0][0]=min(b[0][0],a[root*2].num[0]+a[root*2+1].num[1]);
		if(a[root*2].num[1]!=-1&&a[root*2+1].num[0]!=-1)b[0][0]=min(b[0][0],a[root*2].num[1]+a[root*2+1].num[0]);
		if(a[root*2].num[1]!=-1&&a[root*2+1].num[1]!=-1)b[0][1]=min(b[0][1],a[root*2].num[1]+a[root*2+1].num[1]);
		if(a[root*2].num[0]!=-1&&a[root*2+1].num[0]!=-1)b[1][0]=min(b[1][0],a[root*2].num[0]+a[root*2+1].num[0]);
		if(a[root*2].num[1]!=-1&&a[root*2+1].num[1]!=-1)b[1][1]=min(b[1][1],a[root*2].num[1]+a[root*2+1].num[1]);
		if(a[root*2].num[1]!=-1&&a[root*2+1].num[0]!=-1)b[1][1]=min(b[1][1],a[root*2].num[1]+a[root*2+1].num[0]);
		if(a[root*2].num[0]!=-1&&a[root*2+1].num[1]!=-1)b[1][1]=min(b[1][1],a[root*2].num[0]+a[root*2+1].num[1]);
		if(a[root].opr==0)b[0][0]++,b[0][1]++;
		else b[1][0]++,b[1][1]++;
		if(a[root].v)
		{
			a[root].num[0]=min(b[0][0],b[1][0]);
			a[root].num[1]=min(b[0][1],b[1][1]);
		}
		else 
		{
			a[root].num[0]=b[1-a[root].opr][0];
			a[root].num[1]=b[1-a[root].opr][1];
		}
		if(a[root].num[0]==1000000)a[root].num[0]=-1;
		if(a[root].num[1]==1000000)a[root].num[1]=-1;
	}
//	printf("%d:%d %d\n",root,a[root].num[0],a[root].num[1]);
}
int main()
{
	int n,p=0,i,v;
	freopen("A-large.in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	for(scanf("%d",&n);n--;)
	{
		printf("Case #%d: ",++p);
		scanf("%d%d",&m,&v);
		for(i=1;i<=m;++i)
		{
			a[i].num[0]=a[i].num[1]=-1;
			if(2*i<m)
			{
				scanf("%d%d",&a[i].opr,&a[i].v);
				a[i].num[a[i].v]=0;
			}
			else
			{
				scanf("%d",&a[i].v);
				a[i].num[a[i].v]=0;
			}
			a[i].vis=0;
		}
		dp(1);
		if(a[1].num[v]==-1)printf("IMPOSSIBLE\n");
		else printf("%d\n",a[1].num[v]);
	
	}
	return 0;
}
