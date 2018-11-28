#include<cstdio>
#include<map>
using namespace std;

int main()
{
	freopen("D:\\data\\B-small-attempt0.in","r",stdin);
	freopen("D:\\data\\B-small-attempt0.out","w",stdout);
	int t=0,tt;
	scanf("%d",&tt);
	while(tt--)
	{
		int c,d,n,p=0,i,j;
		char s[105],y,stk[105]={0};
		map<char,char> q[256];
		map<char,bool> qq[256];
		scanf("%d",&c);
		for(i=0;i<c;i++)
		{
			scanf("%s",s);
			q[s[0]][s[1]]=s[2];
			q[s[1]][s[0]]=s[2];
		}
		scanf("%d",&d);
		for(i=0;i<d;i++)
		{
			scanf("%s",s);
			qq[s[0]][s[1]]=1;
			qq[s[1]][s[0]]=1;
		}
		scanf("%d%s",&n,s);
		i=1;
		stk[p++]=s[0];
		while(i<n)
		{
			y=stk[p-1];
			if(q[s[i]][y])
			{
				s[i]=q[s[i]][y];
				p--;
			}
			else
			{
				int ff=0;
				for(j=0;j<p;j++)
					if(qq[stk[j]][s[i]])
					{
						ff=1;
						break;
					}
				if(ff)
					p=j;
				else
					stk[p++]=s[i];
				i++;
			}
		}
		printf("Case #%d: [",++t);
		if(p)
			putchar(stk[0]);
		for(i=1;i<p;i++)
			printf(", %c",stk[i]);
		puts("]");
	}
}
