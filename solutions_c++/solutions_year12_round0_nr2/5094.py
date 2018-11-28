#include<iostream>
#include<vector>
#include<cmath>
using namespace std;
int main()
{
	int t,n,s,p,a,b,q,x,y,z;
	cin>>t;
	for(int i=0;i<t;++i)
	{
		int counter=0;
		cin>>n>>s>>p;
		for(int j=0;j<n;++j)
		{
			cin>>a;
			for(int k=p;k<11;++k)
			{
				x=a-k;
				y=x/2;
				x-=y;
				if(min(min(x,y),k)<0 || max(max(x,y),k)>10)
					continue;
				if((max(max(x,y),k)-min(min(x,y),k))<2)
				{
					counter++;
					break;
				}else if((max(max(x,y),k)-min(min(x,y),k))==2 && s>0)
				{
					s--;
					counter++;
					break;
				}


			}
		}
		cout<<"Case #"<<i+1<<": "<<counter<<endl;;
	}
	return 0;
}