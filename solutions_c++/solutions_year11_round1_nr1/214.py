#include <iostream>
#include <queue>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;
long long m,n,tt,c,d,r,pd,pg;
int num[1010];
int used[1010];

int main()
{
	cin>>tt;	
	for (int kk=1;kk<=tt;++kk)
	{
		cin>>n>>pd>>pg;
		int ans=0;
		if (n>=100)
		{
			if (pd==0 && pg==0)
			{
				ans=1;
				break;
			}
			else if (pd==100 && pg==100)
			{
				ans=1;
				break;
			}
			else if (pg!=0 && pg!=100)
			{
				ans=1;
				break;
			}			
		}
		else
		{
			for (int i=1;i<=n;++i)
			{
				if (i*pd%100==0)
				{
					if (pd==0 && pg==0)
					{
						ans=1;
						break;
					}
					else if (pd==100 && pg==100)
					{
						ans=1;
						break;
					}
					else if (pg!=0 && pg!=100)
					{
						ans=1;
						break;
					}
				}
			}
		}
		
		if (ans==1)
		{

			printf("Case #%d: Possible\n",kk);
		}
		else
		{
			printf("Case #%d: Broken\n",kk);

		}
	
	}	
	return 0;	
}