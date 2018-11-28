#include<iostream>
using namespace std;
#include<cstdio>
#include<cmath>
#define VAL(y,y1,y2,x) ((y-y1)+(y1-y2)*x)
int xx[1010],yy[1010];
int main()
{
	freopen("A-large(2).in","r",stdin);
	freopen("A-large(2).out","w",stdout);
	int T;
	cin>>T;
	int cs=0;
	while(T--)
	{
		int N,count=0;
		cs++;
		cin>>N;
		int i,j;
		for(i=0;i<N;i++)
		{
			cin>>xx[i]>>yy[i];
		}
		for(i=0;i<N-1;i++)
		{
			for(j=i+1;j<N;j++)
			{
				if((VAL(xx[j],xx[i],yy[i],0))*(VAL(yy[j],xx[i],yy[i],1))<0)
					count++;
			}
		}
		printf("Case #%d: %d\n",cs,count);
	}
	return 0;
}