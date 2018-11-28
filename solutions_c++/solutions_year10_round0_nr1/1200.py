#include <iostream>
#include <cmath>
#include <string.h>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t,cnt=0;
	cin>>t;
	int n,k;
	int i;
	int a,b;
	bool flag,find;
	while(t--)
	{
		flag=0;
		find=0;
		cin>>n>>k;
		k++;
		while(1)
		{
			for(i=1;i<=30;i++)
			{
				a=pow(2,i);b=pow(2,i+1);
				if(k<a)
				{
					flag=1;
					break;
				}
				if(k==a)
				{
					if(i>=n)
					{
						printf("Case #%d: %s\n",++cnt,"ON");
						flag=1;
						find=1;
						break;
					}
				}
				if(k<b && k>a)
				{
					k-=a;
					break;
				}
			}
			if(flag==0)
				continue;
			else
				break;
		}
		if(find==0)
			printf("Case #%d: %s\n",++cnt,"OFF");
	}
	return 0;
}




