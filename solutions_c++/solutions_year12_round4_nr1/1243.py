#include<stdio.h>
#include<string.h>
#define min(a,b) (a)<(b)?(a):(b)
#define maxn 10010
typedef struct nd
{
	int d;
	int l;
}nd;nd v[maxn];
int d[maxn];
int D,n;
int flag;
void dfs(int pos,int carry)
{
	int i,len;
	if((d[pos]!=0 && d[pos]>carry) || flag)return;
	d[pos]=carry;
	if(v[pos].d + carry>=D){flag=1;return;}
	for(i=pos+1;i<=n && v[i].d - v[pos].d<=carry;i++)
	{
		len=min(v[i].l,v[i].d - v[pos].d);
		dfs(i,len);
	}
}
int main()
{
	int cases,t,i;
	freopen("test.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&cases);
	for(t=1;t<=cases;t++)
	{
		printf("Case #%d: ",t);
		scanf("%d",&n);
		for(i=1;i<=n;i++)scanf("%d%d",&v[i].d,&v[i].l);
		scanf("%d",&D);
		memset(d,0,sizeof(d));
		flag=0;
		dfs(1,v[1].d);
		if(flag)printf("YES\n");
		else	printf("NO\n");
	}
	return 0;
}
