#include<stdio.h>
#include<stdlib.h>
#include<memory.h>
int cc[900],dd[900];
char temp[150];
int in[150];
int main()
{
	int t,ca=1;
	int c,d,n;
	int i,j,k;
	scanf("%d",&t);
	while(ca<=t)
	{
		memset(cc,0,sizeof(cc));
		memset(dd,0,sizeof(dd));
		scanf("%d",&c);
		for(i=0;i<c;i++)
		{
			scanf("%s",temp);
			int stemp1=0,stemp2=0;
			stemp1=(temp[0]-'A')*26+temp[1]-'A';
			stemp2=temp[0]-'A'+(temp[1]-'A')*26;
			cc[stemp1]=temp[2]-'A'+1;
			cc[stemp2]=temp[2]-'A'+1;
		}
		scanf("%d",&d);
		for(i=0;i<d;i++)
		{
			scanf("%s",temp);
			int stemp1=0,stemp2=0;
			stemp1=(temp[0]-'A')*26+temp[1]-'A';
			stemp2=temp[0]-'A'+(temp[1]-'A')*26;
			dd[stemp1]=1;
			dd[stemp2]=1;
		}
		scanf("%d",&n);
		scanf("%s",temp);
		for(i=0;i<n;i++)
		{
			in[i]=temp[i]-'A';
		}
		int curlen=2;
		int first=0;
		for(curlen=1;curlen<=n;curlen++)
		{
			int flag=0;
			for(i=curlen-2;i>=first;i--)
			{
				if(in[i]==-1)
				continue;
				else
				{
					if(cc[in[i]*26+in[curlen-1]])
					{
						in[curlen-1]=cc[in[i]*26+in[curlen-1]]-1;
						in[i]=-1;
						flag=1;
						break;
					}
					else
					{
						break;
					}
				}
			}
			if(flag)
			continue;
			for(i=first;i<curlen-1;i++)
			{
				if(dd[in[i]*26+in[curlen-1]])
				{
					first=curlen;
					break;
				}
			}
		}
		printf("Case #%d: [",ca);
		int flag=0;
		for(i=first;i<n;i++)
		{
			if(in[i]!=-1)
			{
				if(!flag)
				{
					printf("%c",in[i]+'A');
					flag++;
				}
				else
				printf(", %c",in[i]+'A');
			}
		}
		printf("]\n");
		ca++;
	}
}
