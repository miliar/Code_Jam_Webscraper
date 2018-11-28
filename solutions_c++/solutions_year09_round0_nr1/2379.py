#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<ctype.h>
using namespace std;
char a[5000][16],b[10000],c[10000];
int main()
{
	int i,j,k,L,D,N,flag[5000],count,ch,z,fl,now;
	freopen("out.txt","w",stdout);
	scanf("%d%d%d",&L,&D,&N);
	getchar();
	for(i=0;i<D;i++)
		gets(a[i]);

	for(k=1;k<=N;k++)
	{
		count=D;
		gets(b);
		memset(flag,0,sizeof(flag));
		for(i=0,now=0;b[i];i++,now++)
		{
			if(isalpha(b[i]))
			{
				ch=b[i];
				c[0]='\0';
			}
			else
			{
				i++;
				for(j=0;b[i]!=')';i++,j++)
					c[j]=b[i];
				c[j]='\0';
			}
			for(j=0;j<D;j++)
			{
				if(flag[j]!=1)
				{
					if(strlen(c)==0)
					{
						if(a[j][now]!=ch)
						{
							flag[j]=1;
							count--;
						}
					}
					else
					{
						for(z=0,fl=1;c[z];z++)
						{
							if(a[j][now]==c[z])
							{
								fl=0;
								break;
							}
						}
						if(fl==1)
						{
							flag[j]=1;
							count--;
						}
					}
				}
			}

		}

		printf("Case #%d: %d\n",k,count);

	}

	return 0;
}