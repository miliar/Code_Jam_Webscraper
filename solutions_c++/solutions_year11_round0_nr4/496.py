#include <iostream>
#include <queue>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;
int m,n,tt,c,d,r;
int num[1010];
int used[1010];

int main()
{
	cin>>tt;	
	for (int kk=1;kk<=tt;++kk)
	{	
		cin >> n;
		for (int i=1;i<=n;++i)
		{
			cin>>num[i];
		}
		int l=0;
		int ans=0;
		memset(used,0,sizeof(used));
		for (int i=1;i<=n;++i)
		{
			if (!used[i])
			{
				l=0;
				used[i]=1;
				int j=i;
				while (num[j]!=i)
				{
					
					l++;
					j=num[j];
					used[j]=1;
				}
				l++;
				if (l!=1)
				{
					ans+=l;
				}				
			}			
		}

		
		printf("Case #%d: %.6lf\n",kk,ans*1.0);
	}	
	return 0;	
}