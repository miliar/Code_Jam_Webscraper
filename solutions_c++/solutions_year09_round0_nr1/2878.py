#include<stdio.h>
#include<string.h>

char str[5005][50],S[1000];
char oth[50][500],org[1000];
long L,D,N,i,k,len,t,j,l,p,kase,count,flag;



int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	while(scanf("%ld%ld%ld",&L,&D,&N)==3)
	{
		kase=1;
		for(i=0;i<D;i++)
			scanf("%s",&str[i]);

		getchar();
		for(k=0;k<N;k++)
		{
			gets(S);
			len=strlen(S);
			t=0;
			for(i=0;i<len;i++)
			{
				j=0;
				if(S[i]=='(')
				{
					i++;
					while(S[i]!=')' && i<len)
					{
						oth[t][j++]=S[i++];
					}
					oth[t++][j]=0;
				}
				else
				{
					oth[t][0]=0;
					org[t++]=S[i];
				}
			}

			flag=count=0;
			if(t < L || t > L)
			{
				printf("Case #%ld: %ld\n",kase++,count);
				continue;
			}
			for(i=0;i<D;i++)
			{
				for(j=0;j<L;j++)
				{
					l=strlen(oth[j]);
					if(l!=0)
					{
						for(p=0;p<l;p++)
							if(str[i][j]==oth[j][p])
							{
								flag=1;
								break;
							}
					}
					else
					{
						if(str[i][j]==org[j])
							flag=1;
					}
					if(flag==1)
					{
						flag=0;
						if(j==L-1)
							count++;
					}
					else
						break;
				}
			}
			printf("Case #%ld: %ld\n",kase++,count);
			memset(org,0,sizeof(org));
			memset(oth,0,sizeof(oth));
		}
	}
	return 0;
}