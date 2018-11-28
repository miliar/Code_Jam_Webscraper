#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int maxx(int a,int b)
{
	return a<b?a:b;
}
int num[200][200];

int main()
{
	int case_t;
	freopen("test.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&case_t);
	int pp=1;
	while(case_t--)
	{
		int k;
		scanf("%d",&k);
		int i,j,v,b;
		int minn=100000000;
		memset(num,-1,sizeof(num));
		for(i=0;i<2*k-1;++i)
		{
			j=abs(i-k+1);
			int p=abs(k-abs(k-1-i));
			for(;p;j+=2,p--)
				scanf("%d",&num[i][j]);
		}
		for(i=0;i<2*k-1;++i)
		{
			bool up=false;
			for(v=1;;++v)
			{
				if(i-v<0||i+v>=2*k-1) break;
				for(b=0;b<2*k-1;++b)
				{
					if(num[b][i-v]!=-1&&num[b][i+v]!=-1)
					{
						if(num[b][i-v]!=num[b][i+v])
						{
							up=true;break;
						}
					}
				}
				if(up) break;
			}
			if(!up)
			{
				for(j=0;j<2*k-1;++j)
				{
					bool po=false;
					for(v=1;;++v)
					{
						if(j-v<0||j+v>=2*k-1) break;
						for(b=0;b<2*k-1;++b)
						{
							if(num[j-v][b]!=-1&&num[j+v][b]!=-1)
							{
								if(num[j-v][b]!=num[j+v][b])
								{
									po=true;break;
								}
							}
						}
						if(po) break;
					}
					if(!po)
					{
						int kk=abs(j-k+1);
						int hen=kk+k;
						
						hen=hen+abs(i-k+1);
						minn=maxx(minn,hen*(hen+1)/2+hen*(hen-1)/2-k*(k+1)/2-(k-1)*k/2);
					}
				}
			}
		}
		printf("Case #%d: %d\n",pp++,minn);
	}
}