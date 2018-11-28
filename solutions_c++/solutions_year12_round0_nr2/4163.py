#include<iostream>
using namespace std;
int marks()
	{
		int num;
		int s;
		int max;
        cin>>num>>s>>max;
		int count=0;
		int j=0;
		int m;
		int diff;
		for(j=0;j<num;j++)
		{
			cin>>m;
			diff=(m-max)/2;
			if(m>=max)
			{
			if(max-diff<=1)
			{
				count+=1;
			}
			if((max-diff)==2)
			{
				if(s>0)
				{
				count+=1;
				s-=1;
				}
			}
			}
		}
		return count;
	}
int main()
	{
		int n;
		cin>>n;
		int ans[100];
		int i=0;
		for(i=0;i<n;i++)
		{
			ans[i]=marks();
		}
		for(i=1;i<=n;i++)
            cout<<"Case #"<<i<<": "<<ans[i-1]<<"\n";
        return 0;
	}

