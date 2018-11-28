#include <iostream>
#include <cstdio>
#include <cmath>
#include <set>
#include <vector>
#include <map>
#include <algorithm>


using namespace std;

char ss[505][505];
double point[505][505];

double eps=1e-9;

int check(int a,int b,int k)
{
	int i,j;
	double sumx=0,sumy=0;
	if(k%2==0)
	{
		double half=(double)k/2-0.5;
		for(i=a;i<a+k;++i)
			for(j=b;j<b+k;++j)
			{
				if((i==a&&j==b)||(i==a+k-1&&j==b)||(i==a&&j==b+k-1)||(i==a+k-1&&j==b+k-1)) continue;
				double xx=i-a-half,yy=j-b-half;
				sumx+=(double)xx*point[i][j];
				sumy+=(double)yy*point[i][j];
			}
	}
	else
	{
		int half=k/2;
		for(i=a;i<a+k;++i)
			for(j=b;j<b+k;++j)
			{
				if((i==a&&j==b)||(i==a+k-1&&j==b)||(i==a&&j==b+k-1)||(i==a+k-1&&j==b+k-1)) continue;
				int xx=i-a-half,yy=j-b-half;
				sumx+=(double)xx*point[i][j];
				sumy+=(double)yy*point[i][j];
			}
	}
	if(fabs(sumx)<eps&&fabs(sumy)<eps) return 1;
	return 0;
}

int main()
{
	freopen("B-small-attempt2.in","r",stdin);
	freopen("outb.txt","w",stdout);
	int cas=1;
	int T;scanf("%d",&T);
	while(T--)
	{
		int i,j,k,v,b;
		int r,c,d;scanf("%d%d%d",&r,&c,&d);
		for(i=0;i<r;++i)
		{
			scanf("%s",ss[i]);
			for(j=0;j<c;++j)
			{
				point[i][j]=ss[i][j]-'0'+d;
			}
		}
		int ff=0,ans=-1;
		for(i=min(r,c);i>=3;--i)
		{
			if(ff) break;
			//if(i%2==0) continue;
			for(v=0;v<=r-i;++v)
			{
				if(ff) break;
				for(b=0;b<=c-i;++b)
				{
					if(check(v,b,i))
					{
						//cout<<v<<' '<<b<<endl;
						ff=1;
						ans=i;
						break;
					}
				}
			}
		}
		printf("Case #%d: ",cas++);
		if(ff) printf("%d\n",ans);
		else printf("IMPOSSIBLE\n");
	}
}