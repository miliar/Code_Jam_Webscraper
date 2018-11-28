#include <iostream>
#include <algorithm>
using namespace std;
struct TPoint
{
	int x;
	int y;
}p[1001];
int main()
{
	
	freopen("out.txt","w",stdout);
	int t;
	int n,i,j;
	cin>>t;
	int ca=0;
	int cnt;
	while(t--)
	{
		cin>>n;
		for(i=0;i<n;i++)
		{
			cin>>p[i].x>>p[i].y;
		}
		cnt=0;
		for(i=0;i<n-1;i++)
		{
			for(j=i+1;j<n;j++)
			{
				if((p[i].x-p[j].x)*(p[i].y-p[j].y)<0)
					cnt++;
			}
		}
		printf("Case #%d: %d\n",++ca,cnt);
	}
	return 0;
}


