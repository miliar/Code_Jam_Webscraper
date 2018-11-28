#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;
int main()
{
	int i,j,m,n;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	cin>>m;
	for (i=0;i<m;i++)
	{
		cin>>n;
		int s1=1,s2=1;
		int t1=0,t2=0;
		int l,ans,d;
		char ch;
		ans = 0;
		for(j=0;j<n;j++)
		{
			cin>>ch>>l;
			if(ch=='O')
			{
				d=abs(s1-l)+1;
				if(t1>=d-1)
				{
					t1=0;
					ans++;
					t2++;
				}
				else
				{
					ans+=d-t1;
					t2+=d-t1;
					t1=0;
				}
				s1=l;
			}
			if(ch=='B')
			{
				d=abs(s2-l)+1;
				if(t2>=d-1)
				{
					t2=0;
					ans++;
					t1++;
				}
				else
				{
					ans+=d-t2;
					t1+=d-t2;
					t2=0;
				}
				s2=l;
			}
		}
		printf("Case #%d: %d\n",i+1,ans);
	}
	return 0;
}