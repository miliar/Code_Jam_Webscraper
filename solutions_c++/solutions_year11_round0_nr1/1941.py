#include<iostream>
#include<stdio.h>
#include<stdlib.h>


using namespace std;
int O[101];
int B[101];
int OB[101];
int main()
{
	int T,N,d,curv,prev;
	int o,b,ob,j=0;
	char c;
	bool bos;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d",&N);
		o=b=ob=1;
		j++;
		for(int i=1;i<=N;i++)
		{
			scanf("%c",&c);
			scanf("%c",&c);
			scanf("%d",&d);
			//printf("check %i %c %d\n",i,c,d);
			if(c=='O')
			{
				O[o++]=d;
				OB[i]=1;
			}
			else
			{
				B[b++]=d;
				OB[i]=0;
			}
		}
		o=b=ob=1;
		O[0]=B[0]=1;
		curv=prev=0;
		bos=false;
		for(int i=1;i<=N;i++)
		{
			if(OB[i])
			{
				if(abs(O[o]-O[o-1])<=(curv-prev)&bos)
				{
					prev=curv;
					curv+=1;
				}
				else
				{
					int t;
					if(bos)
					{
						t=abs(O[o]-O[o-1])-(curv-prev);
						prev=curv;
					}
					else
						t=abs(O[o]-O[o-1]);
					//prev=curv;
					curv+=t+1;
				}
				o++;
				bos=false;
			}
			else
			{
				if(abs(B[b]-B[b-1])<=(curv-prev)&&!bos)
				{
					prev=curv;
					curv+=1;
				}
				else
				{
					int t;
					if(!bos)
					{
						t=abs(B[b]-B[b-1])-(curv-prev);
						prev=curv;
					}
					else
						t=abs(B[b]-B[b-1]);
					//prev=curv;
					//printf("%d %d %d\n",t,B[b],B[b-1]);
					curv+=t+1;
				}
				b++;
				bos=true;
			}
		}
		printf("Case #%d: %d\n",j,curv);
	}
}
