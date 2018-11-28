#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
using namespace std;
char ch[12000];
int cb[120][120],op[120][120],s[1200],yop,i,j,x,y,z;
int C,D,n,_,ca,top;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&_);ca=0;
	while(_--)
	{
		ca++;
		memset(cb,-1,sizeof(cb));
		scanf("%d",&C);
		for(i=0;i<C;i++)
		{
			scanf("%s",ch);
			x=ch[0]-'A';
			y=ch[1]-'A';
			z=ch[2]-'A';
			cb[x][y]=z;
			cb[y][x]=z;
		}
		scanf("%d",&D);
		memset(op,0,sizeof(op));
		for(i=0;i<D;i++)
		{
			scanf("%s",ch);
			x=ch[0]-'A';
			y=ch[1]-'A';
			op[x][y]=1;
			op[y][x]=1;
		}
		scanf("%d",&n);
		scanf("%s",ch);
		top=0;
		for(i=0;i<n;i++)
		{
		//	for(j=0;j<top;j++)printf("%c",s[j]+'A');puts("");
			s[top++]=ch[i]-'A';
			if(top==1)continue;
			while(top>1&&cb[s[top-1]][s[top-2]]!=-1)
			{
				int te=cb[s[top-1]][s[top-2]];top-=2;
				s[top++]=te;
			}
			for(j=top-2;j>=0;j--)
			{
				if(op[s[top-1]][s[j]])
				{top=0;break;}
			}
		}
		printf("Case #%d: [",ca);
		for(i=0;i<top;i++)
		{
			if(i!=0)printf(", ");
			printf("%c",s[i]+'A');
		}
		puts("]");
	}
}
