#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>

#include<vector>
#include<queue>
#include<stack>
#include<map>
#include<list>
#include<set>
#include <algorithm>
using namespace std;

#define FOR(i,m,n) for(int i=m;i<n;i++)
#define FORE(i,m,n) for(int i=m;i<=n;i++)

typedef long long int int64;

int main()
{	int ch;
	cin>>ch;
	for(int z=1;z<=ch;z++)
	{
		int n,s,p;
		int arr[110]={0};
		cin>>n>>s>>p;
		for(int i=0;i<n;i++)
			cin>>arr[i];
		sort(arr,arr+n);
		int ans=0,cs=0;
		int que,rem;
		for(int i=0;i<n;i++)
		{
			que=arr[i]/3;
			rem=arr[i]%3;
			int x,y,z;
			x=y=z=que;
			if(rem==1)
			{
				z+=1;
				if(z>=p)
					ans++;
			}
			if(rem==2)
			{
				z+=1;
				if(z>=p)
				{
					cs++;
					ans++;
				}
				else if((z+1)>=p && s>0)
				{
					
					
						s--;
						ans++;
					
				}
				else
					cs++;
			}
			if(rem==0)
			{
				if(z>=p && z<arr[i])
				{
					ans++;
					cs++;
				}
				else if((z+1)>=p && s>0 && z<arr[i])
				{
					s--;
					ans++;
				}
				else
					cs++;
			}
		}
		
		if(p==0)
			ans=n;
		
		cout<<"Case #"<<z<<": "<<ans<<endl;
	}
	return 0;
}
