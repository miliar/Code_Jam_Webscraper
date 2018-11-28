#include<stdio.h>
#include<memory.h>

char model[]="welcome to code jam";
char c[510];
int f[20];

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);

	int T,T1,i,j;
	scanf("%d\n",&T);
	for(T1=1;T1<=T;T1++)
	{
		gets(c);
		
		memset(f,0,sizeof(f));
		for(i=0;c[i]!='\0';i++)
		{
			for(j=0;j<=18;j++)
			{
				if(c[i]==model[j])
				{
					if(j==0) f[j]++;
					else f[j]=(f[j]+f[j-1])%10000;
				}
			}
		}
		printf("Case #%d: %04d\n",T1,f[18]);
	}
	return 0;
}