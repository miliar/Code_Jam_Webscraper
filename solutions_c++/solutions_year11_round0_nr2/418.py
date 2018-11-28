#include <cstdio>
#include <cstring>
#include <cmath>

int t,c,d,n,i,top;
char changec[30][30],changed[30][30],list[110],str[10],ans[110];

void init()
{
		memset(changec,0,sizeof(changec));
		memset(changed,0,sizeof(changed));
		scanf("%d",&c);
		for (i=0;i<c;i++)
		{
			scanf("%s",str);
			changec[str[0]-'A'][str[1]-'A']=changec[str[1]-'A'][str[0]-'A']=str[2];
		}
		scanf("%d",&d);
		for (i=0;i<d;i++)
		{
			scanf("%s",str);
			changed[str[0]-'A'][str[1]-'A']=changed[str[1]-'A'][str[0]-'A']=1;
		}
		scanf("%d",&n);
		scanf("%s",list);
}

void solve()
{
	int i,j;
	top=0;
	for (i=0;i<n;i++)
	{
		ans[top]=list[i];
		top++;
		if (top==1) {continue;}
		if (changec[ans[top-2]-'A'][ans[top-1]-'A']!=0)
		{
			ans[top-2]=changec[ans[top-2]-'A'][ans[top-1]-'A'];
			top--;
		}
		else 
		{
			for (j=top-2;j>=0;j--)
				if (changed[ans[j]-'A'][ans[top-1]-'A']==1) 
				{top=0;break;}
		}
	}
	ans[top]=0;
}

void out()
{
	for (int i=0;i<top;i++)
	{
		if (i!=0) printf(", ");
		printf("%c",ans[i]);
	}
	printf("]\n");
}

int main()
{
	freopen("B-small-attempt0.in","r",stdin);freopen("b.out","w",stdout);
	scanf("%d",&t);
	for (int id=1;id<=t;id++)
	{
		init();
		solve();
		printf("Case #%d: [",id);
		out();
	}
	return 0;
}