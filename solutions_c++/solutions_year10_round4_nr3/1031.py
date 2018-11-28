#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;
int m,n,tt,c,r;
int mp[400][400];
int tmp[400][400];
struct rec
{
	int x1,x2,y1,y2;
};
rec num[2000];
int main()
{
	cin>>tt;	
	for (int kk=1;kk<=tt;++kk)
	{
		memset(mp,0,sizeof(mp));
		cin>>r;
		int first=9999999,last=0;
		for (int i=1;i<=r;++i)
		{
			cin>>num[i].x1>>num[i].x2>>num[i].y1>>num[i].y2;
			first=min(first,num[i].x1+num[i].y1);
			last=max(last,num[i].x2+num[i].y2);
			for (int j=num[i].x1;j<=num[i].x2;++j)
			{
				for (int k=num[i].y1;k<=num[i].y2;++k)
				{
					mp[j][k]=1;
				}
			}
		}
		int flag=1,t=0;
		while (flag)
		{
			t++;
			flag=0;
			memset(tmp,0,sizeof(tmp));
			for (int i=1;i<=200;++i)
			{
				for (int j=1;j<=200;++j)
				{
					if (mp[i][j]==1)
					{
						flag=1;
						if (mp[i-1][j]==1 || mp[i][j-1]==1)
						{
							tmp[i][j]=1;
						}
						else
						{
							tmp[i][j]=0;
						}
					}
					else
					{
						if (mp[i-1][j]==1 && mp[i][j-1]==1)
						{
							tmp[i][j]=1;
						}
						else
						{
							tmp[i][j]=0;
						}
					}
				}
			}
			for (int i=1;i<=200;++i)
			{
				for (int j=0;j<=200;++j)
				{
					mp[i][j]=tmp[i][j];
				}
			}
		}
		printf("Case #%d: %d\n",kk,t+1);			
	}	
	return 0;	
}