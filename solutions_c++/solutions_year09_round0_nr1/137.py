#include<stdio.h>
#include<string.h>

int L,D,N;
char word[5001][20];
int h[5001];
char c[10000];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int i,j,T;
	scanf("%d%d%d",&L,&D,&N);
	for(i=1;i<=D;i++)
	{
		scanf("%s",word[i]);
	}

	for(T=1;T<=N;T++)
	{
		memset(h,0,sizeof(h));
		scanf("%s",c);

		int index=0;
		for(i=0;c[i]!='\0';i++)
		{
			int state=0;
			if(c[i]=='(')
			{
				for(i++;c[i]!='\0';i++)
				{
					if(c[i]==')') break;
					else state|=(1<<(c[i]-'a'));
				}
			}
			else state=(1<<(c[i]-'a'));
			
			for(j=1;j<=D;j++)
			{
				if((state & (1<<(word[j][index]-'a')))==0) h[j]=1;
			}
			index++;
		}

		int ans=0;
		for(i=1;i<=D;i++)
		{
			if(h[i]==0) ans++;
		}
		printf("Case #%d: %d\n",T,ans);
	}
	return 0;
}