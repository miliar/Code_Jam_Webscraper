#include<cstring>
#include<cstdio>

const int mx=260;

int ca=0;
int C,D,n;
char mar[mx][mx];
bool in[mx];
bool opp[mx][mx];
char s[mx];
int len;
char list[mx];

void init()
{
	len=0;
	memset(mar,'\0',sizeof(mar));
	memset(opp,false,sizeof(opp));
	memset(in,false,sizeof(in));
}

int main()
{
	int i,j;
	int t;
	scanf("%d",&t);
	while(t--)
	{
		init();
		scanf("%d",&C);
		for(i=0;i<C;i++)
		{
			scanf("%s",s);
			mar[s[0]][s[1]]=s[2];
			mar[s[1]][s[0]]=s[2];
		}
		scanf("%d",&D);
		for(i=0;i<D;i++)
		{
			scanf("%s",s);
			opp[s[0]][s[1]]=true;
			opp[s[1]][s[0]]=true;
		}
		scanf("%d%s",&n,s);
		for(i=0;i<n;i++)
		{
			list[len]='\0';
			//printf("list=%s\n",list);
			if(len==0)
				list[len++]=s[i];
			else
			{
				if(mar[list[len-1]][s[i]]!='\0')
				{
					list[len-1]=mar[list[len-1]][s[i]];
				}
				else
				{
					for(j=0;j<len;j++)
					{
						if(opp[list[j]][s[i]])
							break;
					}
					if(j<len)
						len=0;
					else
						list[len++]=s[i];
				}
			}
		}
		printf("Case #%d: [",++ca);
		if(len!=0)
			printf("%c",list[0]);
		for(i=1;i<len;i++)
			printf(", %c",list[i]);
		printf("]\n");
	}

	return 0;
}
