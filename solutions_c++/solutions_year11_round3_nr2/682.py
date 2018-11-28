#include<iostream>
#include<string>
#include<vector>

using namespace std;

int main()
{
	int T=0;
	cin>>T;

	for (int t=0;t<T;t++)
	{
		long long l,b,n,c;
		
		cin>>l>>b>>n>>c;
		
		long long a[c];
		
		for (int i=0;i<c;i++) cin>>a[i];
		
		long long dist[n];
		
		int tc=0;
		for (int i=0;i<n;i++)
		{
			dist[i]=a[tc++]*2;
			if (tc==c) tc =0;
		}
		
		long long s[n];
		for (int i=0;i<n;i++) s[i] = 0; 
		
		long long time=0;
		for (int i=0;i<n;i++)
		{
			if (time+dist[i]>b)
			{
				if (time>=b) s[i]=dist[i]/2;
				else s[i] = (dist[i] - b + time) /2;
			}
			time+=dist[i];
		}
		
		if (l>=1)
		{
			long long max = 0;
			long long mp;
			
			for (int i=0;i<n;i++)
			{
				if (s[i]>max)
				{
					max = s[i];
					mp = i;
				}
			}
			
			dist[mp] = dist[mp] - s[mp];
			
//			cerr<<"max "<<max<<endl; 
			
			s[mp] = 0;
		}
		
		if (l==2)
		{
			long long max = 0;
			long long mp;
			
			for (int i=0;i<n;i++)
			{
				if (s[i]>max)
				{
					max = s[i];
					mp = i;
				}
			}
			
			dist[mp] = dist[mp] - s[mp];
//						cerr<<"subtracting "<<s[mp]<<endl; 
			s[mp] = 0;
		}		
		
		long long sum=0;
		
		for (int i=0;i<n;i++)
		{
			sum+=dist[i];
		}
		
		cout<<"Case #"<<t+1<<": "<<sum<<endl;
		
		
	}//t for ends
}

