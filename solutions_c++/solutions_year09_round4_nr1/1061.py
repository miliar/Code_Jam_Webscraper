#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

bool opo(const pair<int,int> &a,const pair<int,int> &b)
{
	if(a.first!=b.first)return a.first<b.first;
	return a.second<b.second;
}


int main()
{
	int t,T;
	cin>>T;
	for(t=1;t<=T;++t)
	{
		int N,i,j;
		cin>>N;
		int mat[50]={0};
		for(i=0;i<N;i++)
		{
			for(j=0;j<N;j++)
			{
				char ch;
				cin>>ch;
				if(ch=='1')
					mat[i]=j;
			}
		}
		int ans=0;
	
		for(i=0;i<N;i++)
		{
			for(j=i;j<N;j++)
			{
				if(mat[j]<=i)
					break;
			}
			ans+=j-i;
			while(j!=i)
			{
				mat[j]=mat[j-1];
				j--;
			}
		}
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
	return 0;
}