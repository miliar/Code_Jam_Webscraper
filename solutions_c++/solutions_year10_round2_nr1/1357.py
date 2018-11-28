#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
struct node 
{
	char ch[105];
	bool b;
}a[205];
bool cmp(node x,node y)
{
	return strcmp(x.ch,y.ch)<0;
}
int find(int x,int y)
{
	int l,i,j,l1,l2,k,s,jj;
	l1=strlen(a[x].ch);
	l2=strlen(a[y].ch);
	l=(l1>l2?l2:l1);
	j=(l1>l2?l1:l2);
	k=0;
	for (i=0;i<l2;i++)
		if (a[y].ch[i]=='/')
			k++;
	if (l1==0)
		return k;
	i=0;
	while (i<=l-1&&a[x].ch[i]==a[y].ch[i])
	{
		i++;
	}
	if (i==l2&&(i==l1||a[x].ch[i]=='/'))
		return 0;
	jj=i;
	while (a[y].ch[jj]!='/')
		jj--;
	k=0;
	for (s=jj;s<l2;s++)
		if (a[y].ch[s]=='/')
			k++;
	return k;
}
int main()
{
	freopen("A-small-attempt7.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t,i,j,k,n,m,x,y,count=1,s;
	strcpy(a[0].ch,"");
	scanf("%d",&t);
	while (t--)
	{
		s=0;
		memset(a,0,sizeof(a));
		scanf("%d%d",&n,&m);
		strcpy(a[n+m+1].ch,"");
		getchar();
		for (i=1;i<=n;i++)
		{
			gets(a[i].ch);
			a[i].b=1;
		}
		for (i=1;i<=m;i++)
		{
			gets(a[i+n].ch);
			a[i+n].b=0;
		}
		sort(a+1,a+1+n+m,cmp);
//		for (i=1;i<=n+m;i++)
//			cout<<a[i].ch<<' '<<a[i].b<<endl;
		for (i=1;i<=n+m;i++)
			if (a[i].b==0)
			{
				x=i-1;
				while (x>=1&&a[x].b==0)
					x--;
				j=find(x,i);
				y=i+1;
				while (y<=n+m&&a[y].b==0)
				{
					y++;
				}
				k=find(y,i);
	//			cout<<(j>k?k:j)<<endl;
				s+=(j>k?k:j);
				a[i].b=1;
			}
		printf("Case #%d: %d\n",count++,s);
	}
	return 0;
}