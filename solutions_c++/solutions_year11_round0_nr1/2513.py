#include<iostream>
using namespace std;
int ans,times,p[2],now[1000],point[1000],n,hall[1000];
char gc()
{
	char ch;
	scanf("%c",&ch);
	while (!isalpha(ch)) scanf("%c",&ch);
	return ch;
}
void mem()
{
	ans=0;
	memset(p,0,sizeof(p));
	memset(now,0,sizeof(now));
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.out","w",stdout);
	scanf("%d",&times);
	for (int z=1;z<=times;++z)
	{
		scanf("%d",&n);
		mem();
		for (int a=1;a<=n;++a)
		{
			hall[a]=(gc()=='O');
			scanf("%d",&point[a]);
		}
		ans=point[1];
		now[hall[1]]=point[1];
		p[hall[1]]=point[1];
		now[1-hall[1]]=0;
		p[1-hall[1]]=1;
		for (int a=2;a<=n;++a)
		{
		//	printf("[%d,%d,%d,%d]",ans,now[hall[a-1]],now[hall[a]],p[hall[a]],point[a]);
			if (hall[a]==hall[a-1]) 
			{
				ans+=abs(point[a]-point[a-1])+1;
				now[hall[a]]=ans;
				p[hall[a]]=point[a];
			}
			else 
			{
			//	printf("(%d,%d)",point[a],point[p[hall[a]]]);
			//	printf("<%d,%d>",abs(point[a]-p[hall[a]]),(now[hall[a-1]]-now[hall[a]]));
				ans+=(abs(point[a]-p[hall[a]])-(now[hall[a-1]]-now[hall[a]])>0?abs(point[a]-p[hall[a]])-(now[hall[a-1]]-now[hall[a]]):0)+1;
				now[hall[a]]=ans;
				p[hall[a]]=point[a];
			}
			
		}
	//	printf("[%d,%d,%d,%d]",ans,now[hall[a-1]],now[hall[a]],p[hall[a]],point[a]);
		printf("Case #%d: %d\n",z,ans);	
	}
}
