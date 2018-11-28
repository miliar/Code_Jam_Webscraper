#include<cstdio>
int main()
{
	int test;
	scanf("%d",&test);
	for(int t=1;t<=test;t++)
	{
		char ch[100]={'\0'};
		int num,a[1000]={0},pos,n[1000]={0},o[1000]={0},b[1000]={0},i,j,po=1,pb=1;
		scanf("%d",&num);
		for(i=0;i<num;i++)
		{
			scanf("%s%d",ch,&pos);
			if(ch[0]=='O')
			{
				o[po++]=pos;
				n[i]=1;
			}
			else
			{
				b[pb++]=pos;
				n[i]=2;
			}
			a[i]=pos;
		}
		int flag=0,moves=0,check=0,ans=0;
		o[0]=1;
		b[0]=1;
		int ok=1,bk=1;
		for(i=0;i<num;i++)
		{
			if(flag==0)
			{
				flag=1;
				if(n[i]==1)
				{
					moves=o[ok]-o[ok-1]+1;
					ok++;
				}
				else
				{
					moves=b[bk]-b[bk-1]+1;
					bk++;
				}
			}
			else
			{
				if(n[i]==1)
				{
					int temp;
					if(o[ok]-o[ok-1] > 0)
						temp=(o[ok]-o[ok-1]);
					else
						temp=(o[ok-1]-o[ok]);
					if(n[i-1]==1)
					{
						moves+=(temp+1);
						ok++;
					}
					else
					{
						ans+=moves;
						if(moves>=temp)
						{
							moves=1;
						}
						else
						{
							moves=temp-moves+1;
						}
						ok++;
					}
				}
				else
				{
					if(n[i-1]==2)
					{
						if(b[bk]-b[bk-1] > 0)
							moves+=(b[bk]-b[bk-1]+1);
						else
							moves+=(b[bk-1]-b[bk]+1);
						bk++;
					}
					else
					{
						ans+=moves;
						int temp;
						if(b[bk]-b[bk-1] > 0)
							temp=(b[bk]-b[bk-1]);
						else
							temp=(b[bk-1]-b[bk]);
						if(moves>=temp)
						{
							moves=1;
						}
						else
						{
						moves=temp-moves+1;
						}
						bk++;
					}					
				}
			}
		}
		ans+=moves;
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}