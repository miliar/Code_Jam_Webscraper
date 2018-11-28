#include<stdio.h>
#include<string.h>
char pattern[5000][50][257];
char word[5000][500];
char tmp[5000];
int ans[5000];
int main()
{
	int in,im,io,n,m,o,inpar,wc;
	scanf("%d %d %d",&in,&im,&io);
	for(n=0;n<im;n++)
		scanf("%s",word[n]);
	for(n=0;n<io;n++)
	{
		scanf("%s",tmp);
		inpar=wc=0;
		for(m=0;m<strlen(tmp);m++)
		{
			if(tmp[m]=='(')
			{
				inpar=1;
			}
			else if(tmp[m]==')')
			{
				inpar=0;
				wc++;
			}
			else
			{
				pattern[n][wc][tmp[m]]=1;
				//printf("%d %d %c\n",n,wc,tmp[m]);
				if(inpar==0)
				{
					wc++;
				}
			}
		}
	}
	for(n=0;n<im;n++)
	{
		for(m=0;m<io;m++)
		{
			for(o=0;o<in;o++)
			{
				//printf("Check: %d %d %c %d\n",m,o,word[n][o],pattern[m][o][word[n][o]]);
				if(pattern[m][o][word[n][o]]==0)
					break;
			}
			if(o==in)
			{
			//	printf("right %s %d\n",word[n],m);
				ans[m]++;
			}
		}
	}
	for(n=0;n<io;n++)
		printf("Case #%d: %d\n",n+1,ans[n]);
}
