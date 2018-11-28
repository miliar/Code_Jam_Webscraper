#include<stdio.h>
#include<stdlib.h>
int n;
int go[2][100],idx[2][100],m[2];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test,i,j,k,T=1;
	char o[3];
	scanf("%d",&test);
	for(;test>0;test--)
	{
		scanf("%d",&n);
		m[0]=m[1]=0;
		for(i=0;i<n;i++)
		{
			scanf("%s%d",o,&k);
			j=(o[0]=='B');
			go[j][m[j]]=k;
			idx[j][m[j]]=i;
			m[j]++;
		}
		int po,pb,io,ib,ans=0;
		po=pb=1;
		io=ib=0;
		while(true)
		{
			if(io<m[0] && ib<m[1])
			{
				if(idx[0][io]<idx[1][ib])
				{
					ans+=abs(po-go[0][io])+1;
					if((abs(po-go[0][io])+1)<abs(pb-go[1][ib]))
					{
						if(pb<go[1][ib])
							pb+=abs(po-go[0][io])+1;
						else
							pb-=abs(po-go[0][io])+1;
					}
					else
					{
						pb=go[1][ib];
					}
					po=go[0][io];
					io++;
				}
				else
				{
					ans+=abs(pb-go[1][ib])+1;
					if(abs(po-go[0][io])>(abs(pb-go[1][ib])+1))
					{
						if(po<go[0][io])
							po+=abs(pb-go[1][ib])+1;
						else
							po-=abs(pb-go[1][ib])+1;
					}
					else
					{
						po=go[0][io];
					}
					pb=go[1][ib];
					ib++;
				}
			}
			else if(io<m[0])
			{
				ans+=abs(po-go[0][io])+1;
				po=go[0][io];
				io++;
			}
			else if(ib<m[1])
			{
				ans+=abs(pb-go[1][ib])+1;
				pb=go[1][ib];
				ib++;
			}
			else break;
			//printf("%d %d %d %d [%d\n",po,io,pb,ib,ans);
		}
		printf("Case #%d: %d\n",T++,ans);
	}
	return 0;
}
