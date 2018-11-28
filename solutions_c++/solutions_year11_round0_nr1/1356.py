#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
using namespace std;

int main()
{
	int n,m,o,b,t,k,i,oo,bb,ca,time;
	char c;

	
	freopen("al.in","r",stdin);
	freopen("al.out","w",stdout);
	cin>>t;
	ca=0;
	while(t--)
	{
		cin>>n;
		oo=1; bb=1;
		o=0; b=0;
		time=0;
		for(i=0;i<n;i++)
		{
			cin>>c>>m;
			if (c=='O')
			{
				k=abs(m-oo);
				oo=m;
				if (o+k<=time)
				{
					o=time+1;
					time++;
				}
				else
				{
					o+=k+1;
					time=o;
				}
			}
			else
			{
				k=abs(m-bb);
				bb=m;
				if (b+k<=time)
				{
					b=time+1;
					time++;
				}
				else
				{
					b+=k+1;
					time=b;
				}
			}
		}
		ca++;
		printf("Case #%d: %d\n",ca,time);
	}
	//system("pause");
	return 0;
}