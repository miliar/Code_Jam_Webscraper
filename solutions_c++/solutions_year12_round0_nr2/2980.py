#include<iostream>
using namespace std;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t;
	cin>>t;
	int Case=0;
	while(t--)
	{
		Case++;
		int n,s,p;
		int num[101];
		int vis[101];
		cin>>n>>s>>p;
		for(int i=0;i<n;i++)
		{
			cin>>num[i];
			int x=num[i]/3;
			int y=num[i]%3;
			if(y==0)
			{
				if(x>=p)
					vis[i]=1;//both
				else if(x+1>=p)
				{
					if(x-1>=0)
					vis[i]=2;//surprising
					else 
					vis[i]=0;
				}
				else
					vis[i]=0;
			}
			if(y==1)
			{
				if(x-1>=p)
					vis[i]=1;
				else if(x>=p)
					vis[i]=1;
				else if(x+1>=p)
				{
					vis[i]=1;
				}
				else
					vis[i]=0;
			}
			if(y==2)
			{
				if(x>=p)
					vis[i]=1;
				else if(x+1>=p)
					vis[i]=1;
				else if(x+2>=p)
					vis[i]=2;
				else 
					vis[i]=0;
			}	

		}
	
		int x1=0,x2=0;
		for(int i=0;i<n;i++)
		{
			if(vis[i]==1)
				x1++;
			if(vis[i]==2)
				x2++;
		}
		//cout<<x1<<" "<<x2<<endl;
		int result=0;
		if(s>=x2)
			result=x1+x2;
		if(s<x2)
			result=x1+s;
		printf("Case #%d: %d\n",Case,result);

	}
	//system("pause");
	return 0;
}

