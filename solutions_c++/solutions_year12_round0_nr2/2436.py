#include<iostream>
#include<cstdio>
#include<cstring>
#include<vector>

using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int q=0;q<t;q++)
	{
		int n,s,p;
		scanf("%d%d%d",&n,&s,&p);
		int ans=0;		
		int low,slow;
		if(p>1)
		{low=p+2*(p-1);slow=p+2*(p-2);}
		else if(p==1)
		{
			low=1;slow=1;
		}	
		else if(p==0)
		{
			low=0;slow=0;
		}
		for(int i=0;i<n;i++)
		{
			int r;
			scanf("%d",&r);
			if(r>=low)ans++;
			else if(r>=slow && s)
			{
				s--;ans++;
			}
		}

		cout<<"Case #"<<q+1<<": "<<ans<<"\n"; 
		
	}	
}
