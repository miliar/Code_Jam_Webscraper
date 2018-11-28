#include<stdio.h>
#include<iostream>
using namespace std;
long long g[1020];
int h[1020];
long long far[1020][2];
int main()
{
	freopen("c:\\c22.in","r",stdin);
	freopen("c:\\outc22.txt","w",stdout);
	int number=1;
	int n;
	scanf("%d",&n);
	for (number=1;number<=n;number++)
	{
		long long r,k,n;
		
		cin>>r>>k>>n;
		int temp;
		for(temp=0;temp<n;temp++)
		{
			h[temp]=0;
			cin>>g[temp];
		}
		int point=0;
		long long he=0;
		int flag=0;
		for(temp=1;temp<=r;temp++)
		{
			long long x=0;
			int  temppoint=point;
			while(x<=k-g[point])
			{
				he+=g[point];
				x+=g[point];
				point++;
				point=point%n;
				if(point==temppoint) break;
			}
			if(h[point]==0)
			{
				far[point][0]=he;
				far[point][1]=temp;
				h[point]=1;
			}
			else if(h[point]==1)
			{
				h[point]=2;
				far[point][0]=he-far[point][0];
				far[point][1]=temp-far[point][1];

			}
			else if(h[point]==2)
			{
				int xx;
				xx=(r-temp)/far[point][1];
				he=he+far[point][0]*xx;
				temp=temp+far[point][1]*xx;
			}
			/*if((point==0)&&(flag==0))
			{
				flag=1;
				he*=(r/temp);
				temp*=(r/temp);
			}
*/
		}
		cout<<"Case #"<<number<<": "<<he<<endl;
		

	}
	return 0;
}