#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int times,n,m,d,i,mi,f[101][256],number[101];
bool end;
void mem()
{
	memset(f,-1,sizeof(f));
//	memset(mi,1,sizeof(mi));
	for (int a=0;a<=255;++a) f[0][a]=0; 
//	mi[0]=0;
}
int main()
{
	freopen("B-small-attempt2.in","r",stdin);
	freopen("B-small-attempt2.out","w",stdout);
	scanf("%d",&times);
	for (int z=1;z<=times;++z)
	{
		scanf("%d%d%d%d",&d,&i,&m,&n);
		for (int a=1;a<=n;++a) scanf("%d",&number[a]);
		mem();
		for (int a=1;a<=n;++a)
		{
			end=false;
			for (int b=0;b<=255;++b)
			{
				mi=1000;
				if (f[a-1][b]!=-1)
				{
				//	mi=min(mi,f[a-1][b]);
					for (int c=max(-m,-b);c<=min(m,255-b);++c)
					{
						
						if (f[a][b+c]==-1)
						f[a][b+c]=f[a-1][b]+abs(b+c-number[a]);
						else f[a][b+c]=min(f[a-1][b]+abs(b+c-number[a]),f[a][b+c]);//change
					//	mi
					}
					if (f[a][b]==-1) f[a][b]=f[a-1][b]+d;
					f[a][b]=min(f[a-1][b]+d,f[a][b]);//del
				}
				for (int c=max(-m,-b);c<=min(m,255-b);++c)
				if (f[a][b+c]!=-1)
				{
					mi=min(f[a-1][b+c],mi);
				}
				if ((mi!=1000)&&(mi!=-1))
				{
					if (f[a-1][b]==-1) 
					{
						f[a-1][b]=mi+i;
						end=1;
					}else 
					{
						if (mi+i<f[a-1][b]) 
						{
							f[a-1][b]=mi+i;
							end=1;
						}
					}
				}
			}
		/*	if (f[a-1][256]!=-1)
			{
				
			}*/
			if (end) a--;
		}
		mi=1000;
		for (int a=0;a<=255;++a)
		{
			if (f[n][a]!=-1)
			mi=min(f[n][a],mi);
		}
		printf("Case #%d: ",z);
		printf("%d\n",mi);
	}
}
